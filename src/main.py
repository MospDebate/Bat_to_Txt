import os
import sys

def convert_bat_to_txt(bat_file_path):
    if not os.path.isfile(bat_file_path):
        print("抱歉，没有找到此文件。")
        sys.exit(1)
    
    with open(bat_file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
    
    txt_file_path = os.path.splitext(bat_file_path)[0] + '.txt'
    with open(txt_file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print(f"转换成功，请查看 {txt_file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使用方法: python main.py <bat_file_path>")
        sys.exit(1)
    
    bat_file_path = sys.argv[1]
    convert_bat_to_txt(bat_file_path)
