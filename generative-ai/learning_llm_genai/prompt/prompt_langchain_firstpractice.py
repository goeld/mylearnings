import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")

from langchain_openai import ChatOpenAI


chat = ChatOpenAI( temperature= 0.0)

# chat.invoke("What is 1 + 1?")

# Define the prompt
from langchain_core.prompts import ChatPromptTemplate


prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a professional progammer and mentor to junior developers."),
    ("user", "{input}"),
])

from langchain_core.output_parsers import StrOutputParser
output_parser = StrOutputParser()

# chain = prompt | chat | output_parser
# response = chain.invoke("What is 1 + 19?")
# print(" The addition of 1 and 1 is: ", response)

response_style = """Hindi Language \
    in a respectful tone, and with a formal style.
"""

input_query = "What is the sume of number from 1 to 100?"

customer_query = ChatPromptTemplate.from_messages([
    ("system",  response_style),
    ("user", "{input_query}")
])

chain = customer_query | chat | output_parser
response = chain.invoke(input_query)

print(" The addition of 1 to 100 is: ", response)




