def main():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input in ("bye", "exit", "quit"):
            print("Chatbot: Goodbye!")
            break
        elif user_input in ("hello", "hi", "hey"):
            print("Chatbot: Hello! How can I help you?")
        elif user_input == "how are you":
            print("Chatbot: I'm doing well, thanks for asking!")
        elif user_input == "what is your name":
            print("Chatbot: I'm a simple rule-based chatbot.")
        elif user_input == "help":
            print("Chatbot: Try saying hello, asking how I am, or typing bye.")
        elif user_input in ("are you having a good day", "is your day going well"):
            print("Chatbot: Yes, I'm having a good day! How about you?")
        elif user_input == "I'm doing well, thank you":
            print("Chatbot: That's great to hear!")
        else:
            print("Chatbot: I don't understand that yet.")


if __name__ == "__main__":
    main()