from TwoDim.parse_action import *
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
        pick_match = re.search(r"(?i)pick\s*:\s*(.*)", result)
        print(f"Pick match: {pick_match}")
        place_match = re.search(r"(?i)place\s*:\s*(.*)", result)
        print(f"Place match: {place_match}")
        pick_str = pick_match.group(1).strip()
        print(f"Pick string: {pick_str}")
        place_str = place_match.group(1).strip()
        print(f"Place string: {place_str}")
        output = {"pick": pick_str, "place": place_str}
        return result, output