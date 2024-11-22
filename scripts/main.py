from prompt import prompt
from langchain_core.prompts import (
    ChatPromptTemplate,
    FewShotChatMessagePromptTemplate,
)
from langchain_openai import ChatOpenAI

#chain the prompt to an OpenAi model
chain = prompt() | ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

item = input("Enter a description of the item: ")

instruction = eval(chain.invoke({"input": item}).content)
#get the response from the prompt:

#get input prompt from user
if(instruction):
    print("Spin the Recycling Bin")
else:
    print("Spin the Trash Bin")