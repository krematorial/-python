# TODO решите задачу
import json
def task() -> float:
    INPUT_FILENAME = "input.json"

    with open(INPUT_FILENAME, 'r') as file:
        data = json.load(file)
        total_product = sum(float(item["score"]) * float(item["weight"]) for item in data)

    return round(total_product, 3)
print(task())