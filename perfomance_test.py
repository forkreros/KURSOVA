import time
import psutil
import pyautogui


def test_game_controls():
    # Вимір навантаження на систему
    initial_cpu_usage = psutil.cpu_percent()
    initial_memory_usage = psutil.virtual_memory().percent

    # Запуск гри
    pyautogui.press('win')
    time.sleep(2)
    pyautogui.write('game.exe')
    time.sleep(1)
    pyautogui.press('enter')

    time.sleep(5)

    start_time = time.perf_counter()
    pyautogui.press('right', 2)
    time.sleep(1)
    pyautogui.press('space', 2, 1)
    time.sleep(1)
    pyautogui.press('left')
    time.sleep(1)
    pyautogui.press('space')
    time.sleep(1)
    pyautogui.press('z', 3, 1)
    time.sleep(1)

    end_time = time.perf_counter()

    #Вимір навантаження на систему

    final_cpu_usage = psutil.cpu_percent()
    final_memory_usage = psutil.virtual_memory().percent

    print(f"\nCPU usage before: {initial_cpu_usage}%")
    print(f"Memory usage before: {initial_memory_usage}%")
    print(f"Time elapsed: {end_time - start_time} seconds")
    print(f"CPU usage after: {final_cpu_usage}%")
    print(f"Memory usage after: {final_memory_usage}%")

    assert True


if __name__ == "__main__":
    test_game_controls()