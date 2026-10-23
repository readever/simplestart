import simplestart as ss

# ── Data: a question bank. Questions, options, answers — all in one place ──
QUESTIONS = [
    {"q": "**1. Which keyword defines a function in Python?**", "options": ["func", "def", "lambda"], "answer": "def"},
    {"q": "**2. Which of these types is immutable?**", "options": ["list", "dict", "tuple"], "answer": "tuple"},
    {"q": "**3. What does `len('abc')` return?**", "options": ["2", "3", "4"], "answer": "3"},
]

# ── State: two slots per question — the answer (qN) and the grading color (cN); the UI is their projection ──
quiz = ss.State(q1="", q2="", q3="", c1="", c2="", c3="",
                summary="Pick your answers — the score shows up here")

# ── Logic: grading only reads and writes data, never touches UI components ──
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
    quiz.summary = f"Answered {done}/3 · {score} correct" + (" — all correct 🎉" if score == 3 else "")

def on_answer(event):
    quiz.update(**{f"q{event.data['idx']}": event.value})   # component -> State: write the choice back
    grade()

def on_reset(event):
    quiz.update(q1="", q2="", q3="", c1="", c2="", c3="",
                summary="Reset — have another go")   # one update: clear all radio groups and reset colors

# ── UI: value and color are both bound to State — components reflect data changes automatically ──
ss.write("## 📝 Python Quiz")
ss.text(quiz.summary, type="info")

for i, q in enumerate(QUESTIONS, start=1):
    with ss.card(style="max-width:560px"):
        ss.write(q["q"])
        ss.radio(q["options"], value=getattr(quiz, f"q{i}"), color=getattr(quiz, f"c{i}"),
                 onchange=on_answer, eventData={"idx": i}, inline=True)

ss.space("mt-4")
ss.button("Retry", icon="mdi-refresh", type="success",  onclick=on_reset)
