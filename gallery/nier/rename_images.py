import os

# 支持的图片扩展名（不区分大小写）
IMAGE_EXTS = {'.png', '.jpg', '.jpeg', '.webp', '.gif', '.bmp', '.svg'}

print("📁 正在处理当前目录下的图片文件...")

for filename in os.listdir('.'):
    # 跳过文件夹
    if not os.path.isfile(filename):
        continue

    name, ext = os.path.splitext(filename)
    ext_lower = ext.lower()

    # 只处理图片文件
    if ext_lower not in IMAGE_EXTS:
        continue

    # 将空格（包括中文全角空格 \u3000）替换为下划线
    new_name = name.replace(' ', '_').replace('\u3000', '_')
    new_filename = new_name + ext  # 保留原扩展名大小写

    # 如果文件名有变化，才重命名
    if new_filename != filename:
        # 防止目标文件已存在（虽然概率低）
        if os.path.exists(new_filename):
            print(f"⚠️  跳过（目标已存在）: {filename}")
            continue

        os.rename(filename, new_filename)
        print(f"✅ {filename} → {new_filename}")

print("✨ 完成！")