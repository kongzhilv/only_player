<div align="center">

# Only Player

**现代化、简洁且功能完整的 Android 视频播放器**

[![Android 11+](https://img.shields.io/badge/Android-11%2B-34A853?logo=android&logoColor=white)](https://developer.android.com)
[![Kotlin](https://img.shields.io/badge/Kotlin-2.4-7F52FF?logo=kotlin&logoColor=white)](https://kotlinlang.org)
[![Jetpack Compose](https://img.shields.io/badge/Jetpack%20Compose-Material%203-4285F4?logo=jetpackcompose&logoColor=white)](https://developer.android.com/compose)
[![Media3](https://img.shields.io/badge/Media3-ExoPlayer-FF6F00?logo=android&logoColor=white)](https://developer.android.com/media/media3)
[![许可证](https://img.shields.io/badge/许可证-GPL--3.0-blue)](LICENSE)

[下载正式版](https://github.com/kongzhilv/only_player/releases) ·
[提交问题](https://github.com/kongzhilv/only_player/issues) ·
[查看构建](https://github.com/kongzhilv/only_player/actions)

</div>

---

## 项目简介

Only Player 是一款面向 Android 的本地视频播放器，使用 **Kotlin、Jetpack Compose、Hilt、Media3 / ExoPlayer** 构建。

本仓库基于 [Kindness-Kismet/only_player](https://github.com/Kindness-Kismet/only_player) 继续维护；其上游项目延续自 [Next Player](https://github.com/anilbeesetti/nextplayer)。感谢原项目与所有贡献者提供的基础能力。

当前最低系统版本为 **Android 11（API 30）**。

---

## 核心功能

| 分类 | 功能 |
|---|---|
| 媒体库 | 文件夹、树状目录、视频列表、搜索、网格与列表布局、排序、目录排除 |
| 播放 | 断点续播、自动连播、画中画、后台播放、播放队列、循环播放 |
| 操作 | 横滑快进快退、竖滑亮度与音量、双击跳转、双指缩放、长按临时倍速 |
| 倍速 | 普通倍速选择会保存到当前视频；长按倍速仅临时生效，松手后恢复 |
| 字幕 | 内嵌字幕、外挂字幕、ASS 特效、编码、字体、字号、背景、延迟与速度调整 |
| 音频 | 音轨选择、首选语言、跳过静音、音量增强与音量标准化 |
| 个性化 | Material 3、动态取色、应用内语言切换、播放器控件与手势配置 |
| 数据 | 单文件播放进度、音轨、字幕轨、缩放和播放速度记忆，设置备份与恢复 |
| 构建 | GitHub Actions 自动检查、分架构签名构建、自动生成 GitHub Release |

---

## 下载与安装

前往 [Releases](https://github.com/kongzhilv/only_player/releases) 下载最新版 APK。

| 文件 | 适用设备 |
|---|---|
| `Only-Player-arm64-v8a-版本号.apk` | 绝大多数 Android 手机和平板，优先选择 |
| `Only-Player-x86_64-版本号.apk` | x86_64 模拟器或少数特殊设备 |

安装步骤：

1. 下载与设备架构相符的 APK。
2. 在系统设置中允许浏览器或文件管理器“安装未知应用”。
3. 安装并启动 Only Player。
4. 按提示授予视频或媒体访问权限。
5. 使用“忽略 `.nomedia`”功能时，系统可能还会要求所有文件访问权限。

> 正式版 APK 由 GitHub Actions 使用仓库配置的签名密钥构建。安装新版本时应保持签名一致，否则 Android 会要求先卸载旧版本。

---

## 基本使用

### 浏览视频

- 首页可切换文件夹、树状目录和视频列表视图。
- 使用搜索快速定位视频。
- 在快捷设置中调整排序、布局和显示方式。
- 可在设置中排除不需要扫描的目录。

### 播放与手势

- 点击视频进入播放器。
- 横向滑动：快进或快退。
- 屏幕左侧竖滑：调节亮度。
- 屏幕右侧竖滑：调节音量。
- 双击：执行设置中配置的跳转操作。
- 双指缩放：缩放视频画面。
- 长按：临时切换到设定倍速，松手后恢复原速度。

### 设置播放速度

播放器中的普通倍速菜单用于设置当前视频的正式播放速度：

- 选择或拖动到目标速度后立即生效。
- 该速度会保存到当前视频的播放状态中。
- 再次打开该视频时会恢复已保存的速度。
- 长按临时倍速与普通倍速互相独立，不会覆盖已保存速度。

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

## GitHub Actions 自动构建

本仓库的工作流、任务和步骤名称均使用中文，便于直接在 GitHub 的 **Actions** 页面查看进度和错误位置。

GitHub 页面自身的固定按钮文字会跟随账号或浏览器语言；仓库可以控制的工作流名称、任务名称、步骤名称和日志提示均使用中文。

### 测试检查

工作流文件：`.github/workflows/test.yaml`

显示名称：**测试检查**

触发方式：

- 向 `main` 分支推送代码。
- 新建或更新 Pull Request。
- 在 Actions 页面手动运行。

主要步骤：

1. 准备构建信息。
2. 读取应用 ID、版本名称、版本号、分支和提交哈希。
3. 配置 JDK 25。
4. 配置 Gradle。
5. 执行 Ktlint 格式化与检查。
6. 检查格式化后是否产生未提交差异。
7. 上传构建报告。
8. 满足版本与更新日志条件时，自动触发正式版发布。

手动运行方法：

1. 打开仓库顶部的 **Actions**。
2. 左侧选择 **测试检查**。
3. 点击 **Run workflow / 运行工作流**。
4. 选择分支并确认运行。

### Android 正式版发布

工作流文件：`.github/workflows/publish.yaml`

显示名称：**Android 正式版发布**

支持两种触发方式：

#### 自动发布

当代码合并到 `main` 后，“测试检查”会验证：

- `versionName` 对应的标签尚未存在。
- `.github/CHANGELOG.md` 自上次发布后已更新。
- 格式与代码检查已通过。

条件满足后会自动调用正式版发布工作流。

#### 手动发布

1. 打开 **Actions**。
2. 选择 **Android 正式版发布**。
3. 点击 **Run workflow / 运行工作流**。
4. 在“发布版本号”中填写如 `1.0.146`。
5. “是否创建 GitHub 发布”保持开启。
6. 确认运行。

发布流程会执行：

1. 读取并校验应用版本。
2. 校验发布版本与 `app/build.gradle.kts` 中的 `versionName` 一致。
3. 检查签名配置。
4. 读取 `.github/CHANGELOG.md` 作为发布说明。
5. 分别构建 `arm64-v8a` 和 `x86_64` 正式版 APK。
6. 校验 APK 是否存在。
7. 上传 Actions 构建产物。
8. 创建版本标签。
9. 创建 GitHub Release 并附加 APK。

### 正式版签名 Secrets

在仓库“Settings → Secrets and variables → Actions”中配置：

| Secret | 说明 |
|---|---|
| `KEYSTORE` | JKS / Keystore 文件经过 Base64 编码后的完整内容 |
| `KEYSTORE_PASSWORD` | Keystore 密码 |
| `KEY_ALIAS` | 签名密钥别名 |
| `KEY_PASSWORD` | 签名密钥密码 |

PowerShell 生成 Base64：

```powershell
[Convert]::ToBase64String([IO.File]::ReadAllBytes("D:\path\release.jks")) | Set-Clipboard
```

Linux / macOS 生成 Base64：

```bash
base64 -w 0 release.jks
```

> Secrets 仅用于 Actions 运行。不要把签名文件、密码或 Base64 内容提交到仓库。

---

## 本地构建

### 环境要求

- Android Studio 或 Android SDK 命令行工具
- JDK 25
- Android SDK 37

### 克隆项目

```bash
git clone https://github.com/kongzhilv/only_player.git
cd only_player
```

### Windows

```powershell
.\gradlew.bat assembleDebug
```

### Linux / macOS

```bash
./gradlew assembleDebug
```

Debug APK 通常位于：

```text
app/build/outputs/apk/debug/
```

### 完整验证

Windows：

```powershell
.\gradlew.bat ktlintCheck test assembleDebug --warning-mode=fail
```

Linux / macOS：

```bash
./gradlew ktlintCheck test assembleDebug --warning-mode=fail
```

### 使用项目构建脚本

构建 arm64-v8a：

```bash
python scripts/build.py build-apk --abi arm64-v8a --clean
```

构建 x86_64：

```bash
python scripts/build.py build-apk --abi x86_64 --clean
```

生成的正式构建产物位于：

```text
build/apk/
```

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

## 发布新版本

1. 完成功能修改与真机验证。
2. 运行完整格式、测试和 Debug 构建检查。
3. 更新 `app/build.gradle.kts`：
   - `versionCode` 增加。
   - `versionName` 更新为目标版本。
4. 更新 `.github/CHANGELOG.md`，只保留本次版本面向用户的变化。
5. 合并到 `main`。
6. 等待“测试检查”通过并自动触发“Android 正式版发布”。
7. 在 Releases 页面确认版本标签、发布说明和两个架构的 APK。

也可手动推送标签：

```bash
git tag v1.0.146
git push origin v1.0.146
```

标签版本必须与 `app/build.gradle.kts` 中的 `versionName` 一致。

---

## 问题排查

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

1. **准备发布信息**：版本号读取与格式是否正确。
2. **验证签名配置**：四个 Secrets 是否齐全且可解码。
3. **签名构建**：Gradle、依赖或代码编译错误。
4. **校验构建产物**：目标 APK 路径与名称是否正确。
5. **创建 GitHub 发布**：标签权限、Release 权限或产物下载问题。

---

## 参与开发

提交修改前建议：

- 将功能修改限制在必要范围内。
- 播放器行为修改需要同时检查 UI 状态、播放服务、媒体状态持久化和临时手势行为。
- 新增界面文字时同步维护多语言资源。
- 提交前运行 Ktlint、单元测试和 Debug 构建。
- 在真机或模拟器上验证实际播放行为。

---

## 开源许可

本项目使用 [GNU General Public License v3.0](LICENSE) 开源。

修改、分发或再发布本项目时，请遵守 GPL-3.0 的相关要求。
