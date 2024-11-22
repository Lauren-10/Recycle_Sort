from langchain_core.prompts import (
    ChatPromptTemplate,
    FewShotChatMessagePromptTemplate,
)
from langchain_openai import ChatOpenAI

def prompt():
    
    # This is a prompt template used to format each individual example.
    example_prompt = ChatPromptTemplate.from_messages(
        [
            ("human", "{input}"),
            ("ai", "{output}"),
        ]
    )
    
    few_shot_prompt = FewShotChatMessagePromptTemplate(
        example_prompt=example_prompt,
        examples=[]
    )
    
    #want to return final prompt
    #print(few_shot_prompt.format())
    final_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", """You are an AI assistant designed to take in photos of items to be recycled or placed into trash.
            You will given a description of the object to be recycled/trashed and classify whether or not the item can be placed to trash or recycling.
            If the item has a clear label, utilize your knowledge base to decide whether or not that product is recyclable
            If the item does not have a cleaar label (ie. candy wrapper, glass bottle, newspaper, etc.), make an educated guess as to what category the item is in.
            Once you have completed your classification, write True if the item is recyclable, False if the item is not recycleable
            """),
            few_shot_prompt,
            ("human", "{input}"),
        ]
    )
    return final_prompt


"""

chain = prompt() | ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

print(chain.invoke({"input": """"""}).content)

"""