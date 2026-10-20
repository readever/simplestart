import simplestart as ss

# ── 数据与状态：演示账号表 + 一份登录态 ──
USERS = {"guest": "123456", "test": "12345"}
auth = ss.State(logged_in=False, logged_out=True, user="", pwd="",
                msg="请输入用户名和密码", hello="")

# ── 逻辑：只读写状态，不碰任何组件 ──
def login(event):
    if USERS.get(auth.user.value) == auth.pwd.value:
        auth.logged_in, auth.logged_out = True, False
        auth.hello = f"欢迎回来，{auth.user.value}！"
        auth.msg = ""
    else:
        auth.msg = "❌ 用户名或密码错误，请重试"

def logout(event):
    auth.update(logged_in=False, logged_out=True, user="", pwd="",
                msg="已退出登录")

# ── 界面：两张卡片的显隐都绑在状态上，谁是投影一目了然 ──
with ss.row(justify="center", style="margin-top:80px;"):
    with ss.card(width=380, padding=32, visible=auth.logged_out):
        ss.write("## 登录")
        ss.space("mb-4")
        ss.input(value=auth.user, placeholder="用户名", block=True)
        ss.space("mb-4")
        ss.input(value=auth.pwd, type="password", placeholder="密码", block=True)
        ss.space("mb-4")
        ss.button("登 录", type="primary", block=True, onclick=login)
        ss.space("mt-2")
        ss.text(auth.msg, type="error")

    with ss.card(width=380, padding=32, visible=auth.logged_in):
        ss.text(auth.hello, type="success")
        ss.space("mb-4")
        ss.button("退出登录", block=True, onclick=logout)