"""A simple rule-based chatbot for a Python internship assignment."""


def get_response(user_input):
    """Return a predefined response for the user's message."""
    normalized_input = user_input.strip().lower()

    if normalized_input == "hello" or normalized_input == "hi":
        return "Hi! How can I help you?"
    elif normalized_input == "how are you":
        return "I'm fine, thanks!"
    elif normalized_input == "bye":
        return "Goodbye!"
    elif normalized_input == "exit" or normalized_input == "quit":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."


def main():
    """Run the chatbot until the user chooses to end the conversation."""
    print("Basic Chatbot")
    print("Type 'bye', 'exit', or 'quit' to end the conversation.")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Bot:", response)

        # Check the normalized input to decide whether to stop the loop.
        if user_input.strip().lower() == "bye" or user_input.strip().lower() == "exit" or user_input.strip().lower() == "quit":
            break


if __name__ == "__main__":
    main()
