import pyautogui, time

time.sleep(5)
for word in range(100):
    pyautogui.typewrite("Marxism does not work")
    pyautogui.press('enter')