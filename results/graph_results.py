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
        print(acceptable_col)
        print(111)
        for col in acceptable_col:

            if col == 'True':
                correct += 1
            else:
                pass
            seen += 1
        results[name] = correct / seen
    print(222)
    plt.figure(figsize=(6, 6))
    print(333)
    print(results.values())
    print(results.keys())
    plt.bar(list(results.keys()), list(results.values()), color = ["red", "green"])
    print(44)
    plt.title("Results of Claude and Grok in the 5x5 Lego Environment")
    plt.xlabel("Model")
    plt.ylabel("Accuracy")
    plt.savefig("graphs/results5x5.png")
    plt.show()

        



#
#
# def graph_csvs(input_file_dir):
#     # Step 1: Read the CSV file
#     df = pd.read_csv(input_csv_path)
#
#     # Step 2: Clean the data
#     # We'll need to convert "Invalid Move" to NaN for numerical analysis
#     df = df.replace("Invalid Move", pd.NA)
#
#     # Step 3: Convert columns that should be numeric
#     df['best_plan_length'] = pd.to_numeric(df['best_plan_length'], errors='coerce')
#     df['agent_plan_length'] = pd.to_numeric(df['agent_plan_length'], errors='coerce')
#     df['actual_plan_length_difference'] = pd.to_numeric(df['actual_plan_length_difference'], errors='coerce')
#
#     # Step 4: Create the plot
#
#     # Plot 1: Histogram of the 'actual_plan_length_difference' (for visualization of plan lengths)
#     plt.figure(figsize=(10, 6))
#     plt.hist(df['actual_plan_length_difference'].dropna(), bins=20, color='skyblue', edgecolor='black')
#     plt.title('Distribution of Actual Plan Length Differences')
#     plt.xlabel('Difference')
#     plt.ylabel('Frequency')
#     plt.grid(True)
#     plt.tight_layout()
#     plt.savefig(output_figure_path)  # Save the figure
#     plt.show()
#
#     # Step 5: You could also plot a count plot of "acceptable" to see the performance
#     plt.figure(figsize=(8, 6))
#     df['acceptable'].value_counts().plot(kind='bar', color='lightcoral')
#     plt.title('Count of Acceptable vs Non-Acceptable Results')
#     plt.xlabel('Acceptable')
#     plt.ylabel('Count')
#     plt.xticks(rotation=0)
#     plt.tight_layout()
#     plt.savefig(output_figure_path.replace('.png', '_acceptable.png'))
#     plt.show()
#
# # Example usage:
if __name__ == "__main__":
    graph_results('reeval_5x5')

