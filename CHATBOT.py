import random   # Used to pick random replies

# Function to process user message and return a reply
def get_bot_response(message):
    user_text = message.lower().strip()

    # Predefined replies
    greetings = ["Hi!", "Hello!", "Hey there!"]
    feelings = ["I'm fine, thanks!", "Doing great, how about you?", "All good here!"]
    farewells = ["Goodbye!", "See you later!", "Take care!"]

    # Logic using if-elif-else
    if "hello" in user_text or "hi" in user_text:   # If user says hello/hi
        return random.choice(greetings)            # Reply with a random greeting
    elif "how are you" in user_text:               # If user asks how are you
        return random.choice(feelings)             # Reply with a random feeling
    elif "bye" in user_text:                       # If user says bye
        return random.choice(farewells)            # Reply with a random farewell
    else:                                          # For any other input
        return "Hmm, I didn’t get that. Try saying hello, how are you, or bye."

print("--- Chatbot (Type 'bye' to exit) ---")

while True:
    user_input = input("You: ")
    reply = get_bot_response(user_input)
    print(f"Bot: {reply}")

    if "bye" in user_input.lower():
        break