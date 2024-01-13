import os
import datetime
import subprocess

def chatbot(Query):
    if "What is your Name" in Query:
        return "I am Chatbot, How can i Help you"
    elif "open chrome"in Query or "google chrome"in Query:
        os.system("open /Applications/Google\ Chrome.app")
        print("Opening. Google Chrome")
    elif "open photo booth" in Query:
        os.system("open /System/Applications/Photos.app")
        print("Opening Photo booth")
    elif "open safari" in Query:
        os.system("open /Applications/Safari.app ")
        print("Opening Safari")
    elif "date" in Query:
        print(datetime.date())
    elif "" in Query:
        print ("is there anything i can help you with?")
    elif "bye" in Query:
        print("Have a good day, see you soon ")
    else:
        print("I didn't understood, is there anything else I can help you with")
def main():
    Continue=True
    while (Continue):
        Query=input("Ask Chatbot: ")
        chatbot(Query.lower())
        if "bye" in Query.lower():
            Continue=False
if __name__=="__main__":
    main()
    
