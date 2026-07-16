#Basic Chatbot
def chatbot_response(user_choice):
    user_choice = user_choice.lower()

    if "hello" in user_choice or "hi" in user_choice:
        return "hello! How can I help you today?"
    
    elif "how are you" in user_choice:
        return "System status is 100% healthy! Thanks for checking in."
    
    elif "your name" in user_choice:
        return "I'm a simple python chatbox created by you"
    
    elif "bye" in user_choice or "exit" in user_choice:
        return "Goodbye! Have a good day."
    
    else:
        return "Sorry, I didn't understand that."

print("----------------------------------------")    
print("Welcome to our Chatbot")
print("Type 'bye' or 'exit' whenever you want to leave.")
print("----------------------------------------")

while(True):
    user = input("You : ")

    response = chatbot_response(user)

    print("Chatbot: ", response)

    if "bye" in user.lower() or "exit" in user.lower():
        break
