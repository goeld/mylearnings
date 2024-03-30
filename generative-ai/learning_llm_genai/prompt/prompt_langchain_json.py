import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.prompts import PromptTemplate
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import ResponseSchema
# from langchain_core.output_parsers import StructuredOutputParser


class Summation(BaseModel):
    input_number_1: int = Field(description= "The first number to be added.")
    input_number_2: int = Field(description= "The second number to be added.")
    sum_number: int = Field(description= "The sum of the two numbers.") 


def get_prompt_response(user_input: str):
    chat = ChatOpenAI( temperature= 0.0)

    output_parser = JsonOutputParser(pydantic_object= Summation)
    prompt = PromptTemplate(
        template="Answer the user query.\n{format_instructions}\n{user_input}\n",
        input_variables=["query"],
        partial_variables={"format_instructions": output_parser.get_format_instructions()},
    )

    chain = prompt | chat | output_parser
    response = chain.invoke(user_input)
    print(" {user_input} is: ", response)

    return response.get("sum_number")


total = get_prompt_response("What is the sum of 1 to 100 ?")
print (" The sum of 1 and 1 is: ", total)




