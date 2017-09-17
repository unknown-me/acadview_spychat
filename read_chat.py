from select_friend import select_friend
from globals import friends
from steganography.steganography import Steganography
from termcolor import colored
import re
def read_chat():
    #function logic
    friend_choice = select_friend()
    #Checking if Friend List is not empty
    if friend_choice!=-1:
        spyobject=friends[friend_choice]
        #Display Spy Details
        print colored(spyobject.Name,'blue'), " ", colored(spyobject.Age,'blue')
        #Average Words
        spyobject.calcAverageWords()
        #Checking If Chat History Is Not Empty
        if(len(spyobject.chat)>0):
            for chatobject in spyobject.chat:
                tempstr=chatobject.Message
                chatobject.Message=Steganography.decode(chatobject.Message)
                # Display Chat
                chatobject.displayMessage()
                chatobject.Message=tempstr
        else:
            print colored("Sorry\nU dont have any Chat History!!!",'red')
    else:
        print colored("Ur friend list is empty.",'red')