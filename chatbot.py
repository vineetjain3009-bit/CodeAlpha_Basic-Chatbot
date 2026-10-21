"""A simple rule-based chatbot for a Python internship assignment."""


EXIT_WORDS = ("bye", "exit", "quit")


def get_response(user_input):
    """Return a predefined response for the user's message."""
    normalized_input = user_input.strip().lower()
    clean_input = normalized_input.strip(".!?,")

    if not clean_input:
        return "Please type a message so I can help you."
    elif clean_input in ("hello", "hi", "hey", "hello chatbot", "hi chatbot"):
        return "Hi! How can I help you?"
    elif "how are you" in clean_input or clean_input == "how r u":
        return "I'm fine, thanks!"
    elif "what is your name" in clean_input or "who are you" in clean_input:
        return "I'm a simple rule-based chatbot."
    elif "what can you do" in clean_input or clean_input == "help":
        return "I can respond to greetings and a few basic conversation questions."
    elif clean_input in ("thanks", "thank you", "thank you chatbot"):
        return "You're welcome!"
    elif clean_input in ("good morning", "good afternoon", "good evening"):
        return "Hello! How can I help you today?"
    elif clean_input == "nice to meet you":
        return "Nice to meet you too!"
    elif clean_input in EXIT_WORDS:
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."


def should_exit(user_input):
    """Return True when the user chooses to end the conversation."""
    return user_input.strip().lower().strip(".!?,") in EXIT_WORDS


def main():
    """Run the chatbot until the user chooses to end the conversation."""
    print("Basic Chatbot")
    print("Try: hello, how are you, what is your name, help, or thank you.")
    print("Type 'bye', 'exit', or 'quit' to end the conversation.")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Bot:", response)

        if should_exit(user_input):
            break


if __name__ == "__main__":
    main()
