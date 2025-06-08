

import threading
import time

# Функція для зворотного відліку
def countdown():
    for i in range(10, 0, -1):
        print("Зворотний відлік:", i)
        time.sleep(1)  # Пауза 1 секунда

# Створюємо потік
count_thread = threading.Thread(target=countdown)

# Запускаємо потік
count_thread.start()

# Чекаємо завершення потоку
count_thread.join()

print("Відлік завершено!")
