import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import re
def graph_results(input_dir):
    dir = Path(input_dir)
    files = []
    for file in dir.iterdir():
        files.append(f"{dir}/{file.name}")
    results = {}
    for file in files:
        name = re.search(r"grok|claude", file).group(0)
        correct = 0
        seen = 0
        df = pd.read_csv(file)
        print(1111)
        acceptable_col = df.iloc[:, -1].tolist()
        for col in acceptable_col:

            if col == 'True':
                correct += 1
            else:
                pass
            seen += 1
        results[name] = correct / seen
    plt.figure(figsize=(6, 6))
    plt.bar(list(results.keys()), list(results.values()), color = ["red", "green"])
    plt.title("Results of Claude and Grok in the 5x5 Lego Environment")
    plt.xlabel("Model")
    plt.ylabel("Accuracy")
    plt.savefig("graphs/results5x5.png")
    plt.show()

if __name__ == "__main__":
    graph_results('reeval_5x5')

