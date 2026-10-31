def get_bot_response(user_input):
    """Function to process user input using if-elif rules and return a response."""
    # Convert input to lowercase and remove outer spaces for clean matching
    clean_input = user_input.strip().lower()

    if clean_input in ["hello", "hi", "hey"]:
        return "Hi!"
    elif clean_input in ["how are you", "how are you?", "how is it going"]:
        return "I'm fine, thanks!"
    elif clean_input in ["what is your name", "what's your name"]:
        return "I'm a simple rule-based chatbot."
    elif clean_input in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that command yet."


def start_chatbot():
    """Main loop function to run the interactive chat session."""
    print("--- Basic Chatbot ---")
    print("Type 'bye' to exit the chat.\n")

    # Main interaction loop
    while True:
        user_message = input("You: ")
        
        # Get response from function
        response = get_bot_response(user_message)
        
        print(f"Bot: {response}\n")
        
        # Loop control: exit condition
        if user_message.strip().lower() in ["bye", "goodbye", "exit", "quit"]:
            break


# Entry point
if __name__ == "__main__":
    start_chatbot()

