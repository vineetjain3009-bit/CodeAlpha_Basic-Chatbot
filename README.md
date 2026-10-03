# Basic Chatbot

## Objective

Create a simple, rule-based chatbot in Python that responds to a few common user messages.

## Features

- Accepts continuous user input in the terminal
- Understands `hello`, `hi`, `how are you`, `bye`, `exit`, and `quit`
- Ignores extra spaces and letter case, so inputs such as ` Hello ` and `HELLO` work
- Gives a helpful default response for unknown messages
- Ends the conversation when the user types `bye`, `exit`, or `quit`

## Concepts Used

- `if` / `elif` / `else`
- Functions
- Loops
- Input and output

## How to Run

1. Open a terminal in the `basic_chatbot` folder.
2. Run the following command:

   ```bash
   python chatbot.py
   ```

3. Optionally run the included checks with:

   ```bash
   python -m unittest test_chatbot.py
   ```

## Example Conversation

```text
You: hello
Bot: Hi! How can I help you?

You: how are you
Bot: I'm fine, thanks!

You: what is your name
Bot: Sorry, I don't understand that.

You: bye
Bot: Goodbye!
```

## How the Code Works

The `get_response(user_input)` function removes extra spaces and changes the input to lowercase. It then uses `if` / `elif` / `else` conditions to select a predefined response. The `main()` function keeps asking for input in a `while` loop and stops when the user enters `bye`, `exit`, or `quit`.
