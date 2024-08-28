#!/bin/bash

echo "你确定要运行吗? (y/n)"
read -p "输入: " confirm

if [[ "$confirm" != "y" ]]; then
    echo "操作已取消。"
    exit 0
fi

echo "请输入.bat文件的完整路径:"
read batFilePath

python3 path/to/bat-to-txt-converter/src/main.py "$batFilePath"
