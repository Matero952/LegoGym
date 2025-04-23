from openai import OpenAI
import os
import re
from dotenv import load_dotenv
load_dotenv()
class or_experiment:
    def __init__(self, model, prompt_func):
        self.model = model
        self.prompt_func = prompt_func
        self.client = OpenAI(api_key=os.getenv("OPENROUTER"), base_url="https://openrouter.ai/api/v1")
        self.model_name = model
    def process_sample(self, start, end):
        prompt = self.prompt_func(start, end)
        completion = self.client.chat.completions.create(
        model="deepseek/deepseek-r1-distill-qwen-32b:free",
        messages=[
            {
            "role": "user",
            "content": prompt
            }
        ]
        )
        result = completion.choices[0].message.content
        print(result)
        action_matches = list(re.finditer(r'\bmove.{0,9}', result))
        if action_matches:
            action_match = (action_matches[-1]).group(0)
            return result, action_match
        else:
            return result, ' '

