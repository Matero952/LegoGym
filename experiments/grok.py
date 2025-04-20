from openai import OpenAI
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
        pick_match = re.search(r"(?i)pick\s*:\s*(.*)", result)
        place_match = re.search(r"(?i)place\s*:\s*(.*)", result)
        pick_str = pick_match.group(1).strip()
        place_str = place_match.group(1).strip()
        output = {"pick": pick_str, "place": place_str}
        return result, output