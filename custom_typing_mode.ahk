
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
h::Send, 哈
j::Send, 基
m::Send, 米
+m::Send, 没录多
b::Send, 曼波
n::Send, 南北绿豆
+n::Send, 那
a::Send, 阿
s::Send, 西
x::Send, 噶
y::Send, 呀
u::Send, 库
8::Send, 椰奶
9::Send, 椰果
l::Send, 奶龙
o::Send, 哦玛吉里
d::Send, 大
g::Send, 狗
t::Send, 叫
w::Send, 我
e::Send, 叮咚
c::Send, 不



#If  ; 结束条件块
    