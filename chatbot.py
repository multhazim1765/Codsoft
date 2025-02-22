def chatbot_Multo():
    print("Hello! I'm your friendly chatbot 'Multo'. How can I assist you today?")
    
    while True:
        people = input("You: ").lower() 
        
        if "hello" in people or "hi" in people:
            print("Multo: Hi there! How can I help you?")
        elif "how are you" in people:
            print("Multo: I'm just a bot, but I'm doing great! How about you?")
        elif "your name" in people:
            print("Multo: I'm a simple rule-based chatbot. You can call me Chatty!")
        elif "time" in people:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"Multo: The current time is {current_time}.")
        elif "date" in people:
            from datetime import datetime
            current_date = datetime.now().strftime("%Y-%m-%d")
            print(f"Multo: Today's date is {current_date}.")
        elif "bye" in people or "goodbye" in people:
            print("Multo: Goodbye! Have a great day!")
            break
        elif "help" in people:
            print("Multo: I can help with the following:")
            print("- Say hello or hi")
            print("- Tell you the current time or date")
            print("- Say goodbye")
        else:
            print("Multo: I'm sorry, I don't understand that. Can you rephrase or ask something else?")


chatbot_Multo()
