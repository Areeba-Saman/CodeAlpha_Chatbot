
def get_response(user_input):
    """Return a predefined reply based on the user's message."""
    message = user_input.strip().lower()

    if message == "hello" or message == "hi":
        return "Hi!"
    elif message == "how are you":
        return "I'm fine, thanks!"
    elif message == "bye":
        return "Goodbye!"
    elif message == "what is your name":
        return "I'm CodeBot, a simple rule-based chatbot."
    elif message == "help":
        return "Try saying: hello, how are you, what is your name, or bye."
    else:
        return "Sorry, I don't understand that. Type 'help' to see what I can answer."


def main():
    print("=== Basic Chatbot ===")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")

        if user_input.strip() == "":
            print("Bot: Please type something.")
            continue

        reply = get_response(user_input)
        print("Bot:", reply)

        if user_input.strip().lower() == "bye":
            break


if __name__ == "__main__":
    main()