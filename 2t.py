

import threading
import time
import random

# Функція, яка імітує завантаження
def download_file(file_number):
    seconds = random.randint(3, 5)  # Випадкова затримка
    print(f"Файл {file_number} завантажується ({seconds} сек)...")
    time.sleep(seconds)
    print(f"Файл {file_number} успішно завантажено!")

# Створення 3 потоків
threads = []
for i in range(1, 4):
    thread = threading.Thread(target=download_file, args=(i,))
    threads.append(thread)
    thread.start()

# Очікуємо завершення всіх потоків
for thread in threads:
    thread.join()

print("Усі файли завантажено!")
