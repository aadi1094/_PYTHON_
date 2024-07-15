import random

# Predefined responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm a chatbot, so I'm always good!", "Doing great, thanks for asking!", "I'm here to help you!"],
    "what is your name": ["I'm Chatbot!", "You can call me Chatbot.", "Chatbot at your service!"],
    "bye": ["Goodbye!", "See you later!", "Have a great day!"]
}

# Function to get a response from the chatbot
def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return "Sorry, I don't understand that."

# Main chat loop
def chat():
    print("Chatbot: Hi! I'm Chatbot. You can talk to me by typing your messages below.")
    print("Chatbot: Type 'bye' to end the chat.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: " + random.choice(responses["bye"]))
            break
        response = get_response(user_input)
        print("Chatbot: " + response)

if __name__ == "__main__":
    chat()
