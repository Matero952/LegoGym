def generate_action_mapping():
    counter = 0
    action_mapping = {}
    for i in range(5):
        for j in range(5):
            for k in range(5):
                for l in range(5):
                    action_mapping[counter] = f"move(r{i}, c{j}, r{k}, c{l})"
                    counter += 1

    return action_mapping
print(generate_action_mapping())