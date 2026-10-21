"""A simple visual user interface for the Basic Chatbot project."""

import sys
import tkinter as tk

from chatbot import get_response, should_exit


BACKGROUND = "#0f172a"
PANEL = "#1e293b"
BOT_BUBBLE = "#334155"
USER_BUBBLE = "#2563eb"
TEXT = "#f8fafc"
MUTED_TEXT = "#cbd5e1"
ACCENT = "#38bdf8"


def add_message(chat_box, sender, message):
    """Add one formatted message to the chat area."""
    tag = "user" if sender == "You" else "bot"
    chat_box.configure(state="normal")
    chat_box.insert(tk.END, f"{sender}\n", f"{tag}_name")
    chat_box.insert(tk.END, f"{message}\n\n", tag)
    chat_box.configure(state="disabled")
    chat_box.see(tk.END)


def main(demo_mode=False):
    """Create and run the visual chatbot window."""
    root = tk.Tk()
    root.title("Basic Chatbot")
    root.geometry("720x620")
    root.minsize(520, 480)
    root.configure(bg=BACKGROUND)

    header = tk.Frame(root, bg=BACKGROUND, padx=28, pady=24)
    header.pack(fill="x")

    tk.Label(
        header,
        text="Basic Chatbot",
        font=("Segoe UI", 24, "bold"),
        bg=BACKGROUND,
        fg=TEXT,
    ).pack(anchor="w")
    tk.Label(
        header,
        text="A simple rule-based Python chatbot",
        font=("Segoe UI", 11),
        bg=BACKGROUND,
        fg=ACCENT,
    ).pack(anchor="w", pady=(4, 0))

    chat_box = tk.Text(
        root,
        wrap="word",
        state="disabled",
        font=("Segoe UI", 12),
        bg=PANEL,
        fg=TEXT,
        relief="flat",
        padx=20,
        pady=18,
        cursor="arrow",
    )
    chat_box.pack(fill="both", expand=True, padx=28, pady=(0, 12))
    chat_box.tag_configure("bot_name", foreground=ACCENT, font=("Segoe UI", 10, "bold"))
    chat_box.tag_configure("bot", foreground=TEXT, background=BOT_BUBBLE, spacing1=3, spacing3=8)
    chat_box.tag_configure("user_name", foreground=MUTED_TEXT, font=("Segoe UI", 10, "bold"), justify="right")
    chat_box.tag_configure("user", foreground=TEXT, background=USER_BUBBLE, justify="right", spacing1=3, spacing3=8)

    status_label = tk.Label(
        root,
        text="Try: hello, how are you, what is your name, help, or thank you",
        font=("Segoe UI", 10),
        bg=BACKGROUND,
        fg=MUTED_TEXT,
    )
    status_label.pack(anchor="w", padx=30, pady=(0, 8))

    quick_reply_frame = tk.Frame(root, bg=BACKGROUND)
    quick_reply_frame.pack(fill="x", padx=28, pady=(0, 12))

    input_frame = tk.Frame(
    root,
    bg=BACKGROUND,
    padx=28,
    pady=0
)
    input_frame.pack(fill="x")

    user_entry = tk.Entry(
        input_frame,
        font=("Segoe UI", 12),
        bg="#e2e8f0",
        fg="#0f172a",
        insertbackground="#0f172a",
        relief="flat",
    )
    user_entry.pack(side="left", fill="x", expand=True, ipady=10)

    def end_chat():
        """Disable controls after a goodbye message."""
        user_entry.configure(state="disabled")
        send_button.configure(state="disabled")
        for button in quick_buttons:
            button.configure(state="disabled")
        status_label.configure(text="Conversation ended. Close the window when you are finished.")

    def send_message(message=None):
        """Display the user's message and the chatbot's response."""
        user_message = message if message is not None else user_entry.get()
        if not user_message.strip():
            return

        add_message(chat_box, "You", user_message.strip())
        response = get_response(user_message)
        add_message(chat_box, "Bot", response)
        user_entry.delete(0, tk.END)

        if should_exit(user_message):
            end_chat()
        else:
            user_entry.focus_set()

    def play_demo(message_index=0):
        """Play sample messages automatically for a screen-recorded demo."""
        demo_messages = (
            "Hello",
            "How are you?",
            "What is your name?",
            "What can you do?",
            "Thank you",
            "Bye",
        )

        if message_index < len(demo_messages):
            send_message(demo_messages[message_index])
            root.after(1300, lambda: play_demo(message_index + 1))

    quick_buttons = []
    for text in ("Hello", "How are you?", "What can you do?", "Bye"):
        button = tk.Button(
            quick_reply_frame,
            text=text,
            command=lambda message=text: send_message(message),
            font=("Segoe UI", 10, "bold"),
            bg=BOT_BUBBLE,
            fg=TEXT,
            activebackground="#475569",
            activeforeground=TEXT,
            relief="flat",
            padx=10,
            pady=6,
        )
        button.pack(side="left", padx=(0, 8))
        quick_buttons.append(button)

    send_button = tk.Button(
        input_frame,
        text="Send",
        command=send_message,
        font=("Segoe UI", 11, "bold"),
        bg=ACCENT,
        fg="#082f49",
        activebackground="#7dd3fc",
        activeforeground="#082f49",
        relief="flat",
        padx=22,
        pady=8,
    )
    send_button.pack(side="left", padx=(10, 0))

    user_entry.bind("<Return>", lambda event: send_message())
    add_message(chat_box, "Bot", "Hi! How can I help you?")
    user_entry.focus_set()

    if demo_mode:
        status_label.configure(text="Demo starts in 3 seconds. Get your screen recorder ready.")
        root.after(3000, play_demo)

    root.mainloop()


if __name__ == "__main__":
    main(demo_mode="--demo" in sys.argv)
