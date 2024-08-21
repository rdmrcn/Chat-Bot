# Simple chatbot implementation by.Reha Demircan
#Here is very simple chatbot consepts
#Chat bot these kind of game prefered to made in renpy as telltale game with endings to script
#If you want to contınue further releated converstaion add them to the code script
#with the answers you want
def chatbot_response(user_input, conversation_state):
    responses = {
        "initial": {
            "hi": "Hello! How can I help you today?",
            "hello": "Hi there! How can I assist you?",
            "how are you": "I'm just a bot, but I'm doing fine! How about you?",
            "what's your name": "I'm a chatbot created by Reha. What's your name?",
            "bye": "Goodbye! Have a great day!",
            "default": "I'm sorry, I don't understand that. Can you rephrase?"
        },
        "how_are_you": {
            "fine": "That's good to hear!",
            "well": "That's good to hear!",
            "good": "That's good to hear!",
            "bye": "Goodbye! Have a great day!",
            "default": "I'm glad to hear that! How can I assist you further?"
        }
    }

    # Normalize user input
    user_input = user_input.lower()

    if conversation_state == "initial":
        if user_input in responses["initial"]:
            response = responses["initial"][user_input]
            if user_input == "how are you":
                conversation_state = "how_are_you"
        else:
            response = responses["initial"]["default"]
    elif conversation_state == "how_are_you":
        if user_input in responses["how_are_you"]:
            response = responses["how_are_you"][user_input]
            if user_input == "bye":
                conversation_state = "initial"
        else:
            response = responses["how_are_you"]["default"]
            conversation_state = "initial"

    return response, conversation_state


def main():
    conversation_state = "initial"
    print("Chatbot: Hi there! I'm a simple chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response, conversation_state = chatbot_response(user_input, conversation_state)
        print(f"Chatbot: {response}")


if __name__ == "__main__":
    main()
