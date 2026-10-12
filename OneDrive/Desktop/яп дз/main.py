import json

# Читаем файл с пользователями
with open("users.json", "r", encoding="utf-8") as file:
    users = json.load(file)

# Cловарь городов
cities = {}

# Группируем пользователей по городам
for user in users:
    name = user["name"]
    city = user["address"]["city"]

    if city not in cities:
        cities[city] = []

    cities[city].append(name)

# Сохраняем результат в новый файл
with open("cities.json", "w", encoding="utf-8") as file:
    json.dump(cities, file, ensure_ascii=False, indent=4)

print("Готово! Файл cities.json создан.")