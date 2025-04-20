import re as re
import os
import anthropic
class ClaudeExperiment:
    def __init__(self, model, prompt_function):
        self.client = anthropic.Anthropic(api_key=os.getenv('CLAUDE'))
        self.model = model
        self.prompt_func = prompt_function
        self.model_name = model

    def process_sample(self, start, end):
        prompt = self.prompt_func(start, end)
        response = self.client.messages.create(
            max_tokens=1000,
            model = self.model,
            messages = [{
                "role" : "user",
                "content" : prompt}])
        print(f"Response: {response}")
        result = response.content[0].text
        print(f"Response: {result}")
        action_match = re.search(r"(move.{0,7})", result)
        return action_match
