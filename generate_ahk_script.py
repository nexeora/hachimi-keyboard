#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

def generate_ahk_script(keymap, output_file='custom_typing_mode.ahk'):
    """
    生成AutoHotkey脚本，实现按下Shift+CapsLock切换输入模式
    
    参数:
    keymap: 字典，键为按键（如'a', 'b'），值为对应的文本
    output_file: 输出的AutoHotkey脚本文件名
    """
    # 脚本内容模板
    script_template = """
; 自定义输入模式脚本
; 按下Shift+CapsLock切换模式

; 初始模式设置为普通模式
CustomMode := false

; 切换模式的热键
+CapsLock::
    CustomMode := !CustomMode
    if (CustomMode) {
        ToolTip, 自定义输入模式已启用
    } else {
        ToolTip, 自定义输入模式已禁用
    }
    SetTimer, RemoveToolTip, -1500  ; 1.5秒后调用RemoveToolTip标签
return

; 用于移除提示的标签
RemoveToolTip:
    ToolTip
return

; 定义按键映射
#If (CustomMode)  ; 只有在自定义模式下才生效
"""
    template_back = """


#If  ; 结束条件块
    """

     #生成按键映射代码
    keymappings = ""
    for key, text in keymap.items():
        # 转义特殊字符
        replacements = {
            "\n": "`n",
            "\"": "\"\""
        }
        escaped_text = text
        for old, new in replacements.items():
            escaped_text = escaped_text.replace(old, new)
        keymappings += f"{key}::Send, {escaped_text}\n"

    # 替换模板中的占位符
    script_content = script_template+ keymappings + template_back


    # 写入文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(script_content)

    print(f"AutoHotkey脚本已生成: {output_file}")
    print("使用方法:")
    print("1. 安装AutoHotkey (https://www.autohotkey.com/)")
    print("2. 双击生成的脚本文件运行")
    print("3. 按下Shift+CapsLock切换到自定义输入模式")
    print("4. 再次按下Shift+CapsLock切换回普通模式")

if __name__ == "__main__":
    # 示例按键映射，可根据需求修改
    example_keymap = {
        'h': '哈',
        'j': '基',
        'm': '米',
        '+m': '没录多',
        'b': '曼波',
        'n': '南北绿豆',
        '+n':'那',
        'a': '阿',
        's': '西',
        'x': '噶',
        'y': '呀',
        'u': '库',
        '8':'椰奶',
        '9':'椰果',
        'l': '奶龙',
        'o':'哦玛吉里',
        'd':'大',
        'g':'狗',
        't':'叫',
        'w':'我',
        'e':'叮咚',
        'c':'不',

    }

    print("=== AutoHotkey自定义输入模式脚本生成器 ===")
    print("此脚本将生成一个AutoHotkey脚本，实现按下Shift+CapsLock切换输入模式")
    print("在自定义模式下，按下指定按键会输出预设文本")
    print("当前示例按键映射:")
    for key, text in example_keymap.items():
        print(f"  按下 '{key}' → 输出 '{text}'")

    # 使用示例映射生成脚本
    generate_ahk_script(example_keymap)

    # 提示用户可以修改映射
    print("提示: 你可以修改脚本中的example_keymap字典来自定义按键映射")
