from openai import OpenAI
import re
class grokexperiment:
    def __init__(self, model, prompt_function):
        self.model = model
        self.client = OpenAI(api_key=os.getenv("GROK_API_KEY"), base_url="https://api.x.ai/v1")
        self.prompt_func = prompt_function
        self.model_name = model
    def process_sample(self, start, end):
        prompt = self.prompt_func(start, end)
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role" : "user",
                 "content" : prompt}
            ]
        )
        result = completion.choices[0].message.content
        print(f"Response: {result}")
        action_match = re.search(r"(move.{0,7})", result)
        return result, action_match