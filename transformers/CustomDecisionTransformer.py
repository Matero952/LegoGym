from transformers import DecisionTransformerModel
from transformers import AutoTokenizer, AutoModelde
model = AutoModel.from_pretrained("edbeeching/decision-transformer-gym-hopper-medium")
tokenizer = AutoTokenizer.from_pretrained("edbeeching/decision-transformer-gym-hopper-medium")
# class CustomDecisionTransformer:
#     def __init__(self, name: str):
#         self.name = name
#     def load_model(self) -> None:
#         model = DecisionTransformerModel.from_pretrained(self.name)
# if __name__ == "__main__":
#     cdt = CustomDecisionTransformer("edbeeching/decision-transformer-gym")
#     cdt.load_model()
#I dont really know waht this file does it kinda is just here temporarily for figuring how to download and fine tune
#transformers from hugging face.