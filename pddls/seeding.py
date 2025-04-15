from itertools import product
def generate(total_blocks, cols, max_rows):
    valid_configs = []
    for heights in product(range(max_rows + 1), repeat=cols):
        if sum(heights) == total_blocks:
            config = []
            for col, height in enumerate(heights):
                for row in range(height):
                    config.append((row, col))
            valid_configs.append(config)
    print(len(valid_configs))
    return valid_configs
if __name__ == "main":
    print(generate(5, 5, 5))
#im not gonna lie i copy and pasted this code