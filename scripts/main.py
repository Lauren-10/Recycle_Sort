from prompt import prompt
from langchain_core.prompts import (
    ChatPromptTemplate,
    FewShotChatMessagePromptTemplate,
)
from langchain_openai import ChatOpenAI
import RPi.GPIO as GPIO
import time

#chain the prompt to an OpenAi model
chain = prompt() | ChatOpenAI(temperature=0, model="gpt-3.5-turbo")


PIN = 18
PIN_Y = 22

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(PIN, GPIO.OUT)
GPIO.setup(PIN_Y, GPIO.OUT)

next_decision = input("Enter a description of the item: ")
instruction = eval(chain.invoke({"input": next_decision}).content)

while not next_decision == "done":
    if instruction is True:
        GPIO.output(PIN, GPIO.HIGH)
        time.sleep(5)
        print("That item is recylable!")
        GPIO.output(PIN, GPIO.LOW)
    else:
        GPIO.output(PIN_Y, GPIO.HIGH)
        time.sleep(5)
        print("That item is not recyclable")
        GPIO.output(PIN_Y, GPIO.LOW)
    
    next_decision = input("Enter a description of the item: ")
    instruction = eval(chain.invoke({"input": next_decision}).content)



