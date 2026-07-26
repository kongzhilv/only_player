from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, content: str) -> None:
    (ROOT / path).write_text(content, encoding="utf-8")


def replace_once(content: str, old: str, new: str, label: str) -> str:
    count = content.count(old)
    if count != 1:
        raise RuntimeError(f"{label}：期望命中 1 次，实际命中 {count} 次")
    return content.replace(old, new, 1)


def update_player_service() -> None:
    path = "feature/player/src/main/java/one/only/player/feature/player/service/PlayerService.kt"
    content = read(path)

    repeat_pattern = re.compile(
        r"(Player\.MEDIA_ITEM_TRANSITION_REASON_REPEAT,\s*\n\s*-> )playerPreferences\.defaultPlaybackSpeed"
    )
    content, count = repeat_pattern.subn(
        r"\1storedPlaybackSpeed ?: playerPreferences.defaultPlaybackSpeed",
        content,
        count=1,
    )
    if count != 1 and "Player.MEDIA_ITEM_TRANSITION_REASON_REPEAT,\n        -> storedPlaybackSpeed ?: playerPreferences.defaultPlaybackSpeed" not in content:
        raise RuntimeError(f"重复播放倍速恢复：期望修改 1 处，实际修改 {count} 处")

    helper = """    private fun Player.persistedPlaybackSpeedOrDefault(): Float =
        currentMediaItem?.mediaMetadata?.playbackSpeed ?: playerPreferences.defaultPlaybackSpeed

"""
    if helper not in content:
        anchor = "    private fun Player.isEndOfQueuePauseEnabled"
        index = content.find(anchor)
        if index < 0:
            raise RuntimeError("未找到倍速恢复辅助函数的插入位置")
        content = content[:index] + helper + content[index:]

    old_reset = "player.setPlaybackSpeed(playerPreferences.defaultPlaybackSpeed)"
    new_reset = "player.setPlaybackSpeed(player.persistedPlaybackSpeedOrDefault())"
    old_count = content.count(old_reset)
    new_count = content.count(new_reset)
    if old_count == 4:
        content = content.replace(old_reset, new_reset)
    elif old_count == 0 and new_count == 4:
        pass
    else:
        raise RuntimeError(
            f"默认倍速回退语句数量异常：旧语句 {old_count} 处，已修复语句 {new_count} 处"
        )

    write(path, content)
    print("已修复重复播放、空闲、播放结束和队列末尾的倍速回退。")


def update_playback_state_coordinator() -> None:
    path = "feature/player/src/main/java/one/only/player/feature/player/service/playback/PlaybackStateCoordinator.kt"
    content = read(path)
    block = """        if (primaryVideoState?.playbackSpeed == null) {
            fallbackVideoState.playbackSpeed?.let { playbackSpeed ->
                mediaRepository.updateMediumPlaybackSpeed(
                    uri = playbackStateUri,
                    playbackSpeed = playbackSpeed,
                )
            }
        }
"""
    if block not in content:
        anchor = "        if (primaryVideoState?.audioTrackIndex == null) {"
        content = replace_once(content, anchor, block + anchor, "远程倍速迁移插入点")
    write(path, content)
    print("已补全远程视频稳定状态键的倍速迁移。")


def update_fake_repository() -> None:
    path = "core/data/src/main/java/one/only/player/core/data/repository/fake/FakeMediaRepository.kt"
    content = read(path)

    field = "    val updatedPlaybackSpeeds = mutableMapOf<String, Float>()\n"
    if field not in content:
        anchor = "    val directories = mutableListOf<Folder>()\n"
        content = replace_once(content, anchor, anchor + field, "测试仓库倍速记录字段")

    old_method = """    override suspend fun updateMediumPlaybackSpeed(uri: String, playbackSpeed: Float) {
    }
"""
    new_method = """    override suspend fun updateMediumPlaybackSpeed(uri: String, playbackSpeed: Float) {
        updatedPlaybackSpeeds[uri] = playbackSpeed
    }
"""
    if new_method not in content:
        content = replace_once(content, old_method, new_method, "测试仓库倍速更新方法")

    write(path, content)
    print("已让测试仓库记录倍速迁移结果。")


def update_tests() -> None:
    path = "feature/player/src/test/java/one/only/player/feature/player/service/playback/PlaybackStateCoordinatorTest.kt"
    content = read(path)

    if "import kotlinx.coroutines.runBlocking\n" not in content:
        content = replace_once(
            content,
            "package one.only.player.feature.player.service.playback\n\n",
            "package one.only.player.feature.player.service.playback\n\nimport kotlinx.coroutines.runBlocking\n",
            "协程测试导入",
        )

    test_name = "migrateFallbackStateToPlaybackStateUri_copiesPlaybackSpeedWhenPrimaryMissing"
    if test_name not in content:
        new_test = """    @Test
    fun migrateFallbackStateToPlaybackStateUri_copiesPlaybackSpeedWhenPrimaryMissing() = runBlocking {
        val repository = FakeMediaRepository()
        val coordinator = PlaybackStateCoordinator(repository)
        val playbackStateUri = "remote:smb:1:/Movies/Episode.mkv"
        val primaryState = videoState(
            path = playbackStateUri,
            position = null,
            audioTrackIndex = null,
            subtitleTrackIndex = null,
            playbackSpeed = null,
            videoScale = 1f,
            subtitleDelayMilliseconds = 0L,
            subtitleSpeed = 1f,
        )
        val fallbackState = videoState(
            path = "content://media/external/video/media/42",
            position = null,
            audioTrackIndex = null,
            subtitleTrackIndex = null,
            playbackSpeed = 1.5f,
            videoScale = 1f,
            subtitleDelayMilliseconds = 0L,
            subtitleSpeed = 1f,
        )

        coordinator.migrateFallbackStateToPlaybackStateUri(
            playbackStateUri = playbackStateUri,
            primaryVideoState = primaryState,
            fallbackVideoState = fallbackState,
        )

        assertEquals(1.5f, repository.updatedPlaybackSpeeds[playbackStateUri] ?: 0f, 0.0001f)
    }

"""
        anchor = "    private fun videoState("
        content = replace_once(content, anchor, new_test + anchor, "倍速迁移回归测试插入点")

    write(path, content)
    print("已增加远程视频倍速迁移回归测试。")


def update_release_metadata() -> None:
    gradle_path = "app/build.gradle.kts"
    gradle = read(gradle_path)
    if 'versionCode = 146' in gradle:
        gradle = gradle.replace('versionCode = 146', 'versionCode = 147', 1)
    elif 'versionCode = 147' not in gradle:
        raise RuntimeError("versionCode 不是预期的 146 或 147")

    if 'versionName = "1.0.145"' in gradle:
        gradle = gradle.replace('versionName = "1.0.145"', 'versionName = "1.0.146"', 1)
    elif 'versionName = "1.0.146"' not in gradle:
        raise RuntimeError("versionName 不是预期的 1.0.145 或 1.0.146")
    write(gradle_path, gradle)

    changelog = """- 修复手动设置的播放倍速在播放结束、播放器重新准备或重复播放时回到 1 倍的问题
- 普通倍速会保存到当前视频，并在再次打开视频时恢复
- 长按临时倍速继续保持独立，不会覆盖已保存的普通倍速
- 补全远程视频稳定播放状态键的倍速迁移
- 重写中文 README，并补充中文 GitHub Actions 与发布说明

<details>
<summary>English Version</summary>

- Fix manually selected playback speed reverting to 1x after playback ends, player re-preparation, or repeated playback
- Persist normal playback speed per video and restore it when the video is opened again
- Keep long-press temporary speed independent from the saved normal speed
- Migrate playback speed to stable playback-state keys for remote videos
- Rewrite the Chinese README and document GitHub Actions and release usage

</details>
"""
    write(".github/CHANGELOG.md", changelog)
    print("已将发行版本更新为 1.0.146。")


def main() -> None:
    update_player_service()
    update_playback_state_coordinator()
    update_fake_repository()
    update_tests()
    update_release_metadata()
    print("发行候选源码整理完成。")


if __name__ == "__main__":
    main()
