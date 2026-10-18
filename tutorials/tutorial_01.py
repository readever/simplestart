import simplestart as ss

# ── 数据：一份题库。题目、选项、答案，全部在这里 ──
QUESTIONS = [
    {"q": "**1. Python 中定义函数用哪个关键字？**", "options": ["func", "def", "lambda"], "answer": "def"},
    {"q": "**2. 下面哪个类型是不可变的？**", "options": ["list", "dict", "tuple"], "answer": "tuple"},
    {"q": "**3. `len('abc')` 的返回值是？**", "options": ["2", "3", "4"], "answer": "3"},
]

# ── 状态：每题两个状态位——答案(qN)与判分颜色(cN)，界面是它们的投影 ──
quiz = ss.State(q1="", q2="", q3="", c1="", c2="", c3="",
                summary="选好答案，这里自动出分")

# ── 逻辑：判分只读写数据，不碰任何界面组件 ──
def grade():
    done = score = 0
    for i, q in enumerate(QUESTIONS, start=1):
        picked = getattr(quiz, f"q{i}").value
        if not picked:
            continue
        done += 1
        ok = picked == q["answer"]
        score += ok
        quiz.update(**{f"c{i}": "success" if ok else "error"})   # State -> 组件颜色
    quiz.summary = f"已答 {done}/3 · 答对 {score} 题" + ("，全部正确 🎉" if score == 3 else "")

def on_answer(event):
    quiz.update(**{f"q{event.data['idx']}": event.value})   # 组件 -> State：把选择写回
    grade()

def on_reset(event):
    quiz.update(q1="", q2="", q3="", c1="", c2="", c3="",
                summary="已重置，再来一轮")   # 一次 update：三个单选组清空、颜色全部复位

# ── 界面：value 和 color 都绑 State，组件自动反映数据变化 ──
ss.write("## 📝 Python 小测验")
ss.text(quiz.summary, type="info")

for i, q in enumerate(QUESTIONS, start=1):
    with ss.card(style="max-width:560px"):
        ss.write(q["q"])
        ss.radio(q["options"], value=getattr(quiz, f"q{i}"), color=getattr(quiz, f"c{i}"),
                 onchange=on_answer, eventData={"idx": i}, inline=True)

ss.space("mt-4")
ss.button("重新作答", icon="mdi-refresh", type="success",  onclick=on_reset)
