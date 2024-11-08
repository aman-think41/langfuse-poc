from pydantic import BaseModel
import openai
import json
import os

class EvalFormat(BaseModel):
    score : bool
    reason : str


guidelines = None

with open('./guidelines.txt', 'r') as f:
    guidelines = f.read()

def parseJsonFromLLM(json_string:str) -> dict:
    json_string = json_string.replace('\\','').strip()
    obj = dict(json.loads(json_string))
    return obj

def eval_helper(question, answer, chat_history):
    client = openai.Client(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": f"""
We have a set of guidelines for how to respond to questions \n{guidelines}.
You have to evaluate this step by step.
Step 1 is to understand the question and the guidelines.
Step 2 is to deduce whether the answer is in compliance with the guidelines.
Step 3 is to give a boolean value True or False based on how well the answer adheres to the guidelines, True being compliant and False being non-compliant.

You can be lenient in the case of length and brevity of the answer
Give the reason for your score in the reason field.
                """
            },
            {
                "role": "user",
                "content": f"Question: {question}\Answer: {answer}\nChat History: {chat_history}"
            }
        ],
        response_format=EvalFormat

    )

    response = parseJsonFromLLM(response.choices[0].message.content)
    return response

