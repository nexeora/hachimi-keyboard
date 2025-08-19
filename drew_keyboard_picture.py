from PIL import Image, ImageDraw, ImageFont
from keymap import keymap

# 简单布局（仅示意，按行）
layout = [
    ["1","2","3","4","5","6","7","8","9","0"],
    ["Q","W","E","R","T","Y","U","I","O","P"],
    ["A","S","D","F","G","H","J","K","L"],
    ["Z","X","C","V","B","N","M"],
    ["Space","Enter"]
]

# 画布参数
pad = 10
key_w = 75
key_h = 55
gap = 8
cols = max(len(r) for r in layout)
width = pad * 2 + cols * key_w + (cols - 1) * gap
height = pad * 2 + len(layout) * key_h + (len(layout) - 1) * gap

im = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(im)

# 使用支持中文的字体
font = None
# 尝试多种中文字体
chinese_fonts = [
    "msyh.ttc",      # 微软雅黑
    "simsun.ttc",    # 宋体
    "simhei.ttf",    # 黑体
    "arialuni.ttf",  # Arial Unicode
    "arial.ttf"      # 默认英文字体作为后备
]

for font_name in chinese_fonts:
    try:
        font = ImageFont.truetype(font_name, 14)
        print(f"使用字体: {font_name}")
        break
    except:
        continue

# 如果所有字体都失败，使用默认字体
if font is None:
    font = ImageFont.load_default()
    print("使用默认字体")

y = pad
for row in layout:
    # center row horizontally
    row_width = len(row)*key_w + (len(row)-1)*gap
    x = pad + (width - 2*pad - row_width)//2
    for k in row:
        w = key_w
        # 特殊键宽度调整（举例）
        if k == "Space": w = key_w * 4 + gap*3
        if k == "Enter": w = key_w * 2 + gap

        # 背景
        draw.rectangle([x, y, x+w, y+key_h], outline="#666", fill="#f9f9f9")
        # 键名
        draw.text((x + 6, y + 6), k, font=font, fill="#000")
        
        # 映射信息
        # 查找不带+的映射
        normal_key = k.lower()
        normal_info = keymap.get(normal_key, "")
        
        # 查找带+的映射
        plus_key = "+" + normal_key
        plus_info = keymap.get(plus_key, "")
        
        # 根据要求显示映射信息，带+的显示在上面
        if plus_info:
            # 显示带+的映射（上面）
            #tw, th = draw.textsize(plus_info, font=font)
            draw.text((x + 25, y + key_h - 50), plus_info, font=font, fill="#333")
        
        if normal_info:
            # 显示不带+的映射（下面）
            #tw, th = draw.textsize(normal_info, font=font)
            draw.text((x + 6, y + key_h - 18), normal_info, font=font, fill="#333")

        x += w + gap
    y += key_h + gap

im.save("keyboard_map.png")
print("Saved keyboard_map.png")
