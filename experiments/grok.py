from openai import OpenAI
import re
import os
class grokexperiment:
    def __init__(self, model, prompt_function):
        self.model = model
        self.client = OpenAI(api_key=os.getenv("GROK"), base_url="https://api.x.ai/v1")
        self.prompt_func = prompt_function
        self.model_name = model
    def process_sample(self, start, end):
        prompt = self.prompt_func(start, end)
        completion = self.client.chat.completions.create(
            model=self.model,
            reasoning_effort="low",
            messages=[
                {"role" : "user",
                 "content" : prompt}
            ],
            temperature=0.7
        )
        result = completion.choices[0].message.content
        print(f"Response: {result}")
        action_matches = list(re.finditer(r'\bmove.{0,9}', result))
        if action_matches:
            action_match = (action_matches[-1]).group(0)
            return result, action_match
        else:
            return result, ' '