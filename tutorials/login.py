import simplestart as ss

# ── Data & state: a demo user table + one piece of login state ──
USERS = {"guest": "123456", "test": "12345"}
auth = ss.State(logged_in=False, logged_out=True, user="", pwd="",
                msg="Enter your username and password", hello="")

# ── Logic: only reads and writes state, never touches components ──
def login(event):
    if USERS.get(auth.user.value) == auth.pwd.value:
        auth.logged_in, auth.logged_out = True, False
        auth.hello = f"Welcome back, {auth.user.value}!"
        auth.msg = ""
    else:
        auth.msg = "❌ Wrong username or password, please retry"

def logout(event):
    auth.update(logged_in=False, logged_out=True, user="", pwd="",
                msg="Signed out")

# ── UI: both cards' visibility is bound to state — the projection reads at a glance ──
with ss.row(justify="center", style="margin-top:80px;"):
    with ss.card(width=380, padding=32, visible=auth.logged_out):
        ss.write("## Sign in")
        ss.space("mb-4")
        ss.input(value=auth.user, placeholder="Username", block=True)
        ss.space("mb-4")
        ss.input(value=auth.pwd, type="password", placeholder="Password", block=True)
        ss.space("mb-4")
        ss.button("Sign in", type="primary", block=True, onclick=login)
        ss.space("mt-2")
        ss.text(auth.msg, type="error")

    with ss.card(width=380, padding=32, visible=auth.logged_in):
        ss.text(auth.hello, type="success")
        ss.space("mb-4")
        ss.button("Sign out", block=True, onclick=logout)