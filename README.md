# BAT to TXT Converter

这是一个开源库，用于将 Windows 的 .bat 文件转换为可读的 .txt 文件，并在 Termux 和 Linux 环境下运行。

## 使用方法

1. 克隆此仓库到本地机器。
2. 确保你的系统上安装了 Python 3。
3. 运行 `bin/run_converter.sh` 脚本。

### 在 Termux 中运行

在 Termux 中，你可以直接运行 `run_converter.sh` 脚本。

```bash
sh path/to/bat-to-txt-converter/bin/run_converter.sh
```

### 在 Linux 中运行

在 Linux 中，确保脚本有执行权限，然后运行它。

```bash
chmod +x path/to/bat-to-txt-converter/bin/run_converter.sh
./path/to/bat-to-txt-converter/bin/run_converter.sh
