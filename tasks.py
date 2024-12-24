# 6. Запишите в файл формата TXT следующую информацию из JSON-файла `Sochi24.09.06.json`:
# Какие направления ветра _(wind_dir)_ встречались в данных о погоде в Сочи? Посчитайте количество каждого типа.

import json
from collections import Counter

path_data_text = 'data/Sochi24.09.06.json'
file_results = 'results.txt'


def main():
    with open(path_data_text, 'r') as f:
        data = json.load(f)

    target_key = 'wind_dir'

    list_wind_dir = get_values_by_key(data, target_key)

    count = Counter(list_wind_dir)

    with open(file_results, 'w', encoding='utf-8') as file:
        for key, value in count.items():
            file.write(f"{key}: {value}\n")

    print(f"all wind_dir '{target_key}' all counts: {len(list_wind_dir)}, data: {list_wind_dir}.")

    pass

def get_values_by_key(data, target_key):
    values = []

    if isinstance(data, dict):
        for key, value in data.items():
            if key == target_key:
                values.append(value)
            values.extend(get_values_by_key(value, target_key))
    elif isinstance(data, list):
        for item in data:
            values.extend(get_values_by_key(item, target_key))

    return values

def count_group_winds(lst, unique):
    return list(map(lambda x: (x, lst.count(x)), unique))

if __name__ == "__main__":
    main()