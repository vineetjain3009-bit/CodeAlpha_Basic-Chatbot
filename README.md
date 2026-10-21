# Basic Chatbot

## Objective

Create a simple, rule-based chatbot in Python that responds to common user messages. The project includes a terminal version and a visual desktop version for project demonstrations.

## Features

- Accepts continuous user input in the terminal
- Includes a visual chatbot window built with Python's built-in Tkinter library
- Understands greetings, `how are you`, name questions, `help`, `thank you`, `bye`, `exit`, and `quit`
- Ignores extra spaces and letter case, so inputs such as ` Hello ` and `HELLO` work
- Gives a helpful default response for unknown messages
- Ends the conversation when the user types `bye`, `exit`, or `quit`

## Concepts Used

- `if` / `elif` / `else`
- Functions
- Loops
- Input and output

## How to Run

### Terminal chatbot

1. Open a terminal in the `basic_chatbot` folder.
2. Run:

   ```bash
   python chatbot.py
   ```

### Visual chatbot window

Run this command to open the visual version:

```bash
python chatbot_gui.py
```

Use the quick-reply buttons or type a message and press **Enter** or **Send**. Type `bye`, `exit`, or `quit` to finish the conversation.

For an automatic conversation that is ready to screen-record, run:

```bash
python chatbot_gui.py --demo
```

### Tests

Optionally run the included checks with:

   ```bash
   python -m unittest test_chatbot.py
   ```

## Example Conversation

```text
You: hello
Bot: Hi! How can I help you?

You: how are you
Bot: I'm fine, thanks!

You: what is your name?
Bot: I'm a simple rule-based chatbot.

You: thank you
Bot: You're welcome!

You: bye
Bot: Goodbye!
```

## How the Code Works

The `get_response(user_input)` function removes extra spaces, changes the input to lowercase, and uses `if` / `elif` / `else` conditions to choose a predefined response. The `main()` function keeps asking for input in a `while` loop and stops when the user enters `bye`, `exit`, or `quit`. The `chatbot_gui.py` file uses the same response function in a simple desktop chat window.

## Suggested Video Demonstration

1. Run `python chatbot_gui.py --demo`.
2. Record the chatbot window with Windows Snipping Tool screen recording or Xbox Game Bar (`Windows + Alt + R`).
3. The demo waits three seconds, then automatically shows: `Hello`, `How are you?`, `What is your name?`, `What can you do?`, `Thank you`, and `Bye`.
4. Stop recording and save the video as an MP4 file for submission.
