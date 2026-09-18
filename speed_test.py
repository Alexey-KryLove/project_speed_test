import sys
import time

import requests


REQUEST_COUNT = 10


def measure_speed(url):
    total_time = 0
    total_bytes = 0

    for i in range(REQUEST_COUNT):
        start = time.perf_counter()

        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Ошибка запроса: {e}")
            return

        elapsed = time.perf_counter() - start

        downloaded_bytes = len(response.content)

        total_time += elapsed
        total_bytes += downloaded_bytes

        print(
            f"Запрос {i + 1}: "
            f"{elapsed:.3f} сек, "
            f"{downloaded_bytes / 1024 / 1024:.2f} МБ"
        )

    average_time = total_time / REQUEST_COUNT

    speed_mb_s = (total_bytes / 1024 / 1024) / total_time

    print("\n--- Результат ---")
    print(f"Среднее время запроса: {average_time:.3f} сек")
    print(f"Всего скачано: {total_bytes / 1024 / 1024:.2f} МБ")
    print(f"Скорость: {speed_mb_s:.2f} МБ/с")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python speed_test.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    measure_speed(url)