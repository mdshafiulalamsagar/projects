print("Welcome to the Chatbot! Type 'bye' to exit.\n")

responses = {
    "hello": "Hi there! How can I help you?",
    "hi": "Hello! What can I do for you?",
    "how are you": "I'm just a program, but I'm doing great! How about you?",
    "what is your name": "I am Chatbot, your virtual assistant.",
    "bye": "Goodbye! Have a great day!",
    "help": "Sure! I can answer your basic questions or just chat with you."
}

def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input in responses:
        return responses[user_input]
    else:
        return "Sorry, I don't understand that. Can you try rephrasing?"

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":  
        print("Chatbot: " + responses["bye"])
        break

    response = chatbot_response(user_input)
    print("Chatbot: " + response)
