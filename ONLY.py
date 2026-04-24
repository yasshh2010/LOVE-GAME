import tkinter as tk
import random

root = tk.Tk()
root.title("For You ❤️")
root.geometry("450x550")
root.configure(bg="#ffb6c1")

score = 0
game_active = True
heart = None
answered_yes = False

messages = [
    "You make me smile 😊",
    "You're my favorite person ❤️",
    "I’m lucky to have you 💖",
    "You are amazing 🌸",
    "I love you 💕",
    "You are cute 🥺",
    "You are my mousee 🐭❤️",
    "You are mine onlyy 😤❤️",
    "My day = you 😄",
    "बस तू चाहिए 💞",
    "I am proud of you 🥹❤️",
    "I am always with you 🤝❤️",
    "Thank you for being mine 🥰",
    "You are my happiness 🌈❤️",
    "Forever with you 💍❤️",
    "Only mine 😌❤️"
]

# UI
tk.Label(root, text="Catch My Heart ❤️", font=("Arial", 18, "bold"), bg="#ffb6c1").pack(pady=10)

score_label = tk.Label(root, text="Score: 0", font=("Arial", 14), bg="#ffb6c1")
score_label.pack()

msg_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#ffb6c1")
msg_label.pack(pady=10)

canvas = tk.Canvas(root, width=380, height=300, bg="white", highlightthickness=0)
canvas.pack(pady=10)

# Create heart
def create_heart():
    global heart
    heart = canvas.create_text(100, 100, text="❤️", font=("Arial", 22))
    canvas.tag_bind(heart, "<Button-1>", catch_heart)

def move_heart():
    if game_active and heart:
        x = random.randint(30, 350)
        y = random.randint(30, 270)
        canvas.coords(heart, x, y)

# Sparkles
def show_sparkles():
    items = []
    for _ in range(12):
        x = random.randint(50, 330)
        y = random.randint(50, 250)
        items.append(canvas.create_text(x, y, text="✨", font=("Arial", 16)))
    return items

# Love Question
def love_question():
    global game_active, heart

    if answered_yes:
        return

    game_active = False
    canvas.delete(heart)

    popup = tk.Toplevel(root)
    popup.title("Important Question 😏")
    popup.geometry("300x200")
    popup.configure(bg="#ffe4e1")

    tk.Label(popup, text="Do you love me? ❤️",
             font=("Arial", 14, "bold"), bg="#ffe4e1").pack(pady=20)

    # YES
    def yes_action():
        global answered_yes
        answered_yes = True
        popup.destroy()

        msg_label.config(text="I knew it! ❤️🥰")

        big = canvas.create_text(190, 150, text="💖", font=("Arial", 50))
        sparkles = show_sparkles()
        root.bell()

        root.after(3000, lambda: [canvas.delete(i) for i in sparkles + [big]])
        root.after(3200, win_game)

    # NO (runs away)
    def move_no(e):
        x = random.randint(50, 200)
        y = random.randint(80, 150)
        no_btn.place(x=x, y=y)

    def no_action():
        global game_active
        popup.destroy()

        msg_label.config(text="😡 Not acceptable!! Try again 😂")

        game_active = True
        create_heart()
        move_heart()

    tk.Button(popup, text="❤️ YES ❤️", bg="lightgreen", command=yes_action).pack(pady=5)

    no_btn = tk.Button(popup, text="💔 NO 💔", bg="salmon", command=no_action)
    no_btn.place(x=100, y=120)
    no_btn.bind("<Enter>", move_no)

# Win
def win_game():
    canvas.delete("all")
    canvas.create_text(190, 150, text="💖 YOU WIN 💖", font=("Arial", 26, "bold"))
    msg_label.config(text="You won my heart forever ❤️🏆")

    try:
        import pyttsx3
        engine = pyttsx3.init()
        engine.say("I love you")
        engine.runAndWait()
    except:
        root.bell()

# Catch heart
def catch_heart(event):
    global score

    if not game_active or answered_yes:
        return

    score += 1
    score_label.config(text=f"Score: {score}")

    msg_label.config(text=random.choice(messages))
    move_heart()

    # Repeat question again and again until YES
    if score >= 15 and score % 5 == 0:
        love_question()

    if score >= 50:
        win_game()

# Start
create_heart()
move_heart()

root.mainloop()
