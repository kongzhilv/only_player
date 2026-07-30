<div align="center">

# Only Player Fork

**现代化、简洁且功能完整的 Android 本地视频播放器**

[![Android 11+](https://img.shields.io/badge/Android-11%2B-34A853?logo=android&logoColor=white)](https://developer.android.com)
[![Kotlin](https://img.shields.io/badge/Kotlin-2.4-7F52FF?logo=kotlin&logoColor=white)](https://kotlinlang.org)
[![测试检查](https://github.com/kongzhilv/only_player/actions/workflows/test.yaml/badge.svg)](https://github.com/kongzhilv/only_player/actions/workflows/test.yaml)
[![最新版本](https://img.shields.io/github/v/release/kongzhilv/only_player?display_name=tag)](https://github.com/kongzhilv/only_player/releases/latest)
[![许可证](https://img.shields.io/badge/许可证-GPL--3.0-blue)](LICENSE)

[下载最新版](https://github.com/kongzhilv/only_player/releases/latest) ·
[查看全部版本](https://github.com/kongzhilv/only_player/releases) ·
[提交问题](https://github.com/kongzhilv/only_player/issues) ·
[查看构建](https://github.com/kongzhilv/only_player/actions)

</div>

---

## 项目简介

Only Player Fork 是一款面向 Android 的本地视频播放器，使用 **Kotlin、Jetpack Compose、Hilt 和 Media3 / ExoPlayer** 构建。

本仓库基于 [Kindness-Kismet/only_player](https://github.com/Kindness-Kismet/only_player) 继续维护；其上游项目延续自 [Next Player](https://github.com/anilbeesetti/nextplayer)。感谢原项目与所有贡献者提供的基础能力。

当前 fork 的重要信息：

| 项目 | 内容 |
|---|---|
| 应用名称 | Only Player Fork |
| 应用 ID | `io.github.kongzhilv.onlyplayer` |
| 最低系统版本 | Android 11（API 30） |
| 更新来源 | `kongzhilv/only_player` 的正式 Release |
| 发布架构 | `arm64-v8a`、`x86_64` |
| 签名方式 | fork 自有长期固定签名 |

由于应用 ID 与上游的 `one.only.player` 不同，本 fork 可以和上游版本同时安装，但不会覆盖上游版本。

---

## 本 fork 的主要改动

- 修复手动设置的播放倍速在播放结束、播放器重新准备或重复播放时回到 1 倍的问题。
- 普通倍速会保存到当前视频，并在再次打开视频时恢复。
- 长按临时倍速保持独立，松手后恢复，不会覆盖已保存的普通倍速。
- 补全远程视频稳定播放状态键的倍速迁移。
- 使用独立应用 ID，可与上游版本并存。
- 更新检查改为读取本仓库的正式 Release。
- 正式版使用固定长期签名，并在发布流程中核验两个架构的证书一致性。

当前版本的完整变化见 [.github/CHANGELOG.md](.github/CHANGELOG.md)。

---

## 核心功能

| 分类 | 功能 |
|---|---|
| 媒体库 | 文件夹、树状目录、视频列表、搜索、网格与列表布局、排序、目录排除 |
| 播放 | 断点续播、自动连播、画中画、后台播放、播放队列、循环播放 |
| 操作 | 横滑快进快退、竖滑亮度与音量、双击跳转、双指缩放、长按临时倍速 |
| 倍速 | 普通倍速按视频保存；长按倍速只临时生效，松手后恢复 |
| 字幕 | 内嵌字幕、外挂字幕、ASS 特效、编码、字体、字号、背景、延迟与速度调整 |
| 音频 | 音轨选择、首选语言、跳过静音、音量增强与音量标准化 |
| 个性化 | Material 3、动态取色、应用内语言切换、播放器控件与手势配置 |
| 数据 | 播放进度、音轨、字幕轨、缩放和播放速度记忆，设置备份与恢复 |
| 构建 | GitHub Actions 自动测试、分架构正式构建、长期签名与 Release 核验 |

---

## 下载与安装

从 [Releases](https://github.com/kongzhilv/only_player/releases/latest) 下载最新版 APK。

| 文件名 | 适用设备 |
|---|---|
| `Only-Player-Fork-arm64-v8a-版本号.apk` | 绝大多数 Android 手机和平板，通常选择这个 |
| `Only-Player-Fork-x86_64-版本号.apk` | x86_64 Android 模拟器或少数特殊设备 |

安装步骤：

1. 下载与设备架构相符的 APK。
2. 在系统设置中允许浏览器或文件管理器“安装未知应用”。
3. 安装并启动 Only Player Fork。
4. 按提示授予视频或媒体访问权限。
5. 使用“忽略 `.nomedia`”功能时，系统可能还会要求所有文件访问权限。

### 签名与升级说明

正式版包名为：

```text
io.github.kongzhilv.onlyplayer
```

长期签名证书 SHA-256：

```text
b216ded82a850a9a55d885b8cbf1b8398bbd13b9c511fc3501f3595af89717b7
```

- 当前 Release 及后续版本将继续使用同一枚长期签名，可正常覆盖升级。
- 本 fork 不能直接覆盖上游签名的 `one.only.player`，两者应作为不同应用安装。
- 如果设备安装的是早期临时签名的 `v1.0.146`，需要先卸载一次，再安装当前 Release；安装当前长期签名版后，后续版本即可覆盖升级。
- 卸载应用通常会清除应用数据，必要时请先在应用内导出设置备份。

### 校验下载文件

每个正式 Release 同时提供：

```text
SHA256SUMS.txt
SHA256-CERT-FINGERPRINT.txt
only-player-fork-signing-certificate.pem
```

Windows PowerShell 校验 APK 文件哈希：

```powershell
Get-FileHash .\Only-Player-Fork-arm64-v8a-1.0.146.apk -Algorithm SHA256
```

查看 APK 签名证书：

```powershell
apksigner verify --verbose --print-certs .\Only-Player-Fork-arm64-v8a-1.0.146.apk
```

APK 显示的证书 SHA-256 应与上面的长期签名指纹及 `SHA256-CERT-FINGERPRINT.txt` 一致。

---

## 基本使用

### 浏览视频

- 首页可切换文件夹、树状目录和视频列表视图。
- 使用搜索快速定位视频。
- 在快捷设置中调整排序、布局和显示方式。
- 可在设置中排除不需要扫描的目录。

### 播放与手势

- 横向滑动：快进或快退。
- 屏幕左侧竖滑：调节亮度。
- 屏幕右侧竖滑：调节音量。
- 双击：执行设置中配置的跳转操作。
- 双指缩放：缩放视频画面。
- 长按：临时切换到设定倍速，松手后恢复原速度。

### 播放速度

播放器中的普通倍速菜单用于设置当前视频的正式播放速度：

- 选择或拖动到目标速度后立即生效。
- 速度会保存到当前视频的播放状态中。
- 再次打开该视频时会恢复已保存的速度。
- 长按临时倍速与普通倍速互相独立。

### 字幕

- 在播放器内切换内嵌字幕轨。
- 通过系统文件选择器添加外挂字幕。
- ASS 字幕支持样式和特效渲染。
- 字体、字号、粗体、背景、延迟、字幕速度和文字编码可在设置中调整。

### 备份与恢复

进入“设置 → 通用”：

- 导出当前应用与播放器设置。
- 在当前设备或其他设备中导入备份。
- 需要重新配置时可重置设置。

---

## 本地构建

### 环境要求

- Android Studio 或 Android SDK 命令行工具
- JDK 25
- Android SDK 37
- Python 3（使用 `scripts/build.py` 时需要）

### 克隆项目

```bash
git clone https://github.com/kongzhilv/only_player.git
cd only_player
```

### Debug 构建

Windows：

```powershell
.\gradlew.bat assembleDebug
```

Linux / macOS：

```bash
./gradlew assembleDebug
```

完整检查：

```bash
./gradlew ktlintCheck test assembleDebug --warning-mode=fail
```

使用项目构建脚本生成 arm64 Debug APK：

```bash
python scripts/build.py build-apk --build-type debug --abi arm64-v8a --clean
```

使用项目构建脚本生成分架构 APK：

```bash
python scripts/build.py build-apk --abi arm64-v8a --clean
python scripts/build.py build-apk --abi x86_64
```

构建脚本输出目录：

```text
build/apk/
```

正式签名构建需要配置对应的密钥库环境变量；日常开发应优先使用 Debug 构建，不要把签名文件或密码写入仓库。

---

## GitHub Actions

### 测试检查

工作流：[`test.yaml`](.github/workflows/test.yaml)

触发条件：

- 推送到 `main`。
- 新建或更新 Pull Request。
- 在 Actions 页面手动运行。

执行内容：

1. 读取并校验应用 ID、版本名称和版本号。
2. 配置 JDK 25、Gradle 和 Python。
3. 执行 Ktlint 与全部单元测试。
4. 构建 arm64 Debug APK。
5. 核验 Debug APK 的应用 ID。
6. 上传构建报告。
7. `main` 上满足版本和更新日志条件时，触发正式发布工作流。

### Android 正式版发布

工作流：[`publish.yaml`](.github/workflows/publish.yaml)

正式发布流程：

1. 校验版本号、应用 ID 和目标标签。
2. 检查对应 Release 是否已经具有完整资产和正确长期签名。
3. 执行 Ktlint 与单元测试。
4. 从 Actions Secrets 恢复固定 PKCS12 密钥库。
5. 将密钥库证书与 `SIGNING_CERT_SHA256` 对照。
6. 分别构建 `arm64-v8a` 和 `x86_64` 正式 APK。
7. 核验两个 APK 的包名、签名有效性和证书一致性。
8. 生成 APK SHA-256、签名指纹和公开证书文件。
9. 创建或更新 GitHub Release。
10. 从 Release 重新读取资产并执行最终完整性检查。

### 长期签名配置

仓库“Settings → Secrets and variables → Actions”中使用：

| 类型 | 名称 | 用途 |
|---|---|---|
| Secret | `KEYSTORE` | PKCS12 / JKS 密钥库的 Base64 完整内容 |
| Secret | `KEYSTORE_PASSWORD` | 密钥库密码 |
| Secret | `KEY_ALIAS` | 私钥别名 |
| Secret | `KEY_PASSWORD` | 私钥密码 |
| Variable | `SIGNING_CERT_SHA256` | 预期长期签名证书 SHA-256 |

安全要求：

- 不要把 `.p12`、`.jks`、密码、恢复文件或 Base64 内容提交到 Git。
- GitHub Secrets 只用于自动构建，不能替代离线私钥备份。
- 长期密钥库与恢复信息至少保存两份加密离线副本。
- 修改 `SIGNING_CERT_SHA256` 或替换密钥前，必须确认是否会破坏现有升级链。

---

## 发布新版本

1. 完成功能修改和真机验证。
2. 运行 Ktlint、单元测试和 Debug 构建。
3. 更新 `app/build.gradle.kts`：
   - `versionCode` 必须递增。
   - `versionName` 更新为目标版本。
4. 更新 `.github/CHANGELOG.md`，只保留本次版本面向用户的变化。
5. 合并到 `main`。
6. 等待“测试检查”通过并自动触发“Android 正式版发布”。
7. 在 Releases 页面确认两个 APK 和三项校验资产齐全。
8. 确认 Release 中的证书指纹仍为长期签名指纹。

也可以在 Actions 页面手动运行“Android 正式版发布”，输入与 `versionName` 一致的版本号。

---

## 项目结构

```text
app/                  应用入口、Manifest、构建类型与版本信息
core/common/          日志、调度器和通用工具
core/data/            Repository 实现与数据映射
core/database/        Room 数据库、DAO 与 Schema
core/datastore/       DataStore 数据源和序列化
core/domain/          业务用例
core/media/           媒体扫描与播放相关基础能力
core/model/           公共数据模型
core/ui/              公共 Compose UI、字符串和主题
feature/player/       播放器 UI、状态和播放服务
feature/settings/     设置页面与偏好逻辑
feature/videopicker/  媒体库、搜索和快捷设置
scripts/              构建与维护脚本
.github/workflows/    自动测试和发布工作流
.github/CHANGELOG.md  当前版本发布说明
```

---

## 问题排查

### 新 APK 提示签名不一致

- 确认安装的是 `io.github.kongzhilv.onlyplayer`，而不是上游的 `one.only.player`。
- 如果安装过早期临时签名版 `v1.0.146`，先备份设置，然后卸载旧版再安装当前 Release。
- 使用 `apksigner --print-certs` 检查证书 SHA-256。

### 媒体库内容不完整

- 检查媒体权限。
- 检查是否排除了对应目录。
- 检查目录中的 `.nomedia` 文件及相关设置。

### 字幕乱码或样式异常

- 尝试切换字幕文字编码。
- 确认选择的是正确字幕轨。
- ASS 字幕异常时检查字体和样式设置。

### Actions 正式版构建失败

按顺序查看：

1. 版本、应用 ID 和目标标签校验。
2. 长期签名 Secrets 与 `SIGNING_CERT_SHA256`。
3. Ktlint、单元测试和 Gradle 编译日志。
4. 两个架构 APK 的包名与签名核验。
5. Release 创建、资产上传和最终下载核验。

---

## 参与开发

提交修改前建议：

- 将功能修改限制在必要范围内。
- 播放器行为修改需要同时检查 UI 状态、播放服务、媒体状态持久化和临时手势行为。
- 新增界面文字时同步维护多语言资源。
- 提交前运行 Ktlint、单元测试和 Debug 构建。
- 在真机或模拟器上验证实际播放行为。

---

## 上游与许可

本仓库基于以下项目继续维护：

- [Kindness-Kismet/only_player](https://github.com/Kindness-Kismet/only_player)
- [anilbeesetti/nextplayer](https://github.com/anilbeesetti/nextplayer)

本项目使用 [GNU General Public License v3.0](LICENSE) 开源。修改、分发或再发布本项目时，请遵守 GPL-3.0 的相关要求。
