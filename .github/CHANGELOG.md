- 修复手动设置的播放倍速在播放结束、播放器重新准备或重复播放时回到 1 倍的问题
- 普通倍速会保存到当前视频，并在再次打开视频时恢复
- 长按临时倍速继续保持独立，不会覆盖已保存的普通倍速
- 补全远程视频稳定播放状态键的倍速迁移
- 使用独立应用 ID `io.github.kongzhilv.onlyplayer`，可与原版同时安装
- 更新检查改为读取 `kongzhilv/only_player` 的正式 Release
- 使用本 fork 的独立签名构建，不支持直接覆盖原作者签名版本

<details>
<summary>English Version</summary>

- Fix manually selected playback speed reverting to 1x after playback ends, player re-preparation, or repeated playback
- Persist normal playback speed per video and restore it when the video is opened again
- Keep long-press temporary speed independent from the saved normal speed
- Migrate playback speed to stable playback-state keys for remote videos
- Use the independent application ID `io.github.kongzhilv.onlyplayer`, allowing side-by-side installation with the upstream app
- Check updates from releases in `kongzhilv/only_player`
- Build with an independent fork signature; it does not replace an upstream-signed installation

</details>
