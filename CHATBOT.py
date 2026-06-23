#This chatbot will do the most basic conversation with you
class CHATBOT:
    def respond(self,message): 
        if message.lower()=="hi":
            return 'Hello'
        elif message.lower()=="how are you":
            return 'GREAT!! What about you'
        elif message.lower() == "good"  or  message.lower() == "fine":
            return 'That sounds nice.Have a good day ahead!!'
        elif message.lower()=="not fine":
            return 'That sounds like a you problem'
        elif message.lower()=="bye":
            return 'GOODBYE ;)'
        else:
            return "Didn't get you"
        
bot1=CHATBOT()
print("WELCOMING YOU TO A SIMPLE CHATBOT")
print("Type 'Bye' to end the conversation")
while True:
    message=input("You:")
    response=bot1.respond(message)
    print("Bot:",response)
    if message.lower()=='bye': #to end the conversation 
        break

