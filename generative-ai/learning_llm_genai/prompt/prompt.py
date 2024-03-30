# Add import for openai, load and find envs

from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

def get_chat_response(user_message):
    response = client.chat.completions.create(
        model=os.getenv('MODEL_NAME', 'gpt-3.5-turbo'),  # Default to 'gpt-3.5-turbo' if the environment variable is not set
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message},
        ],
    )
    return response.choices[0].message.content


# write a python __main__ function that will run the chatbot

if __name__ == "__main__":
    print("Welcome to the chatbot!")
    while True:
        user_message = input("You: ")
        response = get_chat_response(user_message)
        print(f"Bot: {response}")

