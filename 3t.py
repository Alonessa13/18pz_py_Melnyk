# Завдання 3 — Паралельна обробка даних

import threading
import random

# Генеруємо список з 1000 випадкових чисел від 1 до 100
numbers = [random.randint(1, 100) for _ in range(1000)]

# Список для збереження результатів
partial_sums = [0] * 4

# Функція, яка рахує суму частини списку
def compute_sum(part_index, part_data):
    total = sum(part_data)
    partial_sums[part_index] = total
    print(f"Потік {part_index+1} завершився. Сума: {total}")

# Ділимо список на 4 частини
chunk_size = len(numbers) // 4
threads = []

for i in range(4):
    start = i * chunk_size
    end = (i + 1) * chunk_size
    part = numbers[start:end]
    thread = threading.Thread(target=compute_sum, args=(i, part))
    threads.append(thread)
    thread.start()

# Чекаємо завершення всіх потоків
for thread in threads:
    thread.join()

# Обчислюємо загальну суму
total_sum = sum(partial_sums)
print("Загальна сума:", total_sum)
