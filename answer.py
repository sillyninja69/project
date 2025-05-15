import openai
import os
from dotenv import load_dotenv

load_dotenv("kai.env")

openai.api_key = os.getenv("OPENAIAPIKEY")

def answer_questions(input_text):
    completion = openai.Completion()
    response = completion.create(
        model="text-davinci-002",
        prompt=input_text,
        temperature=0.5,
        max_tokens=100,
        top_p=0.3,
        frequency_penalty=0.5,
        presence_penalty=0
    )
    answer = response.choices[0].text.strip()
    return answer

while True:
    ques = input("Ask a question=>")
    if ques.lower() == 'exit':
        break
    print(answer_questions(ques))
