# import google.generativeai as genai
from google.ai.generativelanguage_v1 import GenerateContentResponse
import re
import os
from google import genai
class gemini:
    def __init__(self, model, prompt_function):
        self.model = genai.GenerativeModel(model)
        self.client = genai.Client(api_key=os.getenv("GEMINI"))
        self.prompt_func = prompt_function
        self.model_name = model

    def process_sample(self, start, end):
        prompt = self.prompt_func(start, end)
        response = self.client.models.generate_content(
            model = self.model,
            contents=prompt
            # messages = [
            #     {
            #         "role": "user",
            #         "content": [
            #             {"type": "text", "text": prompt},
            #         ]
            #     },
            # ],
        )
        result = response.candidates[0].content.parts[0].text
        action_matches = list(re.finditer(r'\bmove.{0,9}', result))
        if action_matches:
            action_match = (action_matches[-1]).group(0)
            return result, action_match
        else:
            return result, ' '