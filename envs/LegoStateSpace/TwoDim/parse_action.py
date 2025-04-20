import ast
def parse_action(action: str):
    action_str = list(action)
    numbers = []
    for i in action_str:
        if i.isdigit():
            numbers.append(int(i))
        else:
            continue
        if len(numbers) >= 4:
            break
    if len(numbers) < 4:
        return None , None
    else:
        start_block = (numbers[0], numbers[1])
        end_pos = (numbers[2], numbers[3])
        return start_block, end_pos
if __name__ == "__main__":
    print(parse_action("move 1 1 2 22222"))
