# pip install chatterbot==1.0.4 first install these package

from chatterbot import ChatBot

#naming the chatbot calculator
Bot = ChatBot(name = "Calculator",
              read_only = True,
              logic_adapters=["chatterbot.logic.MathematicalEvaluation"],
              storage_adapter='chatterbot.storage.SQLStorageAdapter'
              )

# clear tbe screen and start the calculator
print('\033c')
print("Hello, I am calculator. How may i help you ?")

while True:
    #taking input from the user
    user_input = input('me : ')

    # if user want to quit
    if user_input.lower() == 'quit':
        print("Exiting.....")
        break

    #otherwise evalaute the user input

    try:
        response = Bot.get_response(user_input)
        print("Calculator : ", response)
    except:
        print("Calculator : Please enter valid input. ")






