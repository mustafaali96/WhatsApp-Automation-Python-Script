import time
import pyautogui
import keyboard

text = '''Hello Whatsapp Automated text'''

f = open("numberList.txt", "r")
numberLst = f.readlines()
f.close()

numbers = []
for number in numberLst:
    if number.startswith("03"):
        numbers.append(int('92' + number[1:]))
    elif number.startswith("+92"):
        numbers.append(int(number[1:]))
    else:
        numbers.append(number)

while numbers:
    number = numbers[0]
    webbrowser.open(f'https://web.whatsapp.com/send?phone={number}&text="{text}"')
    time.sleep(10)
    keyboard.press_and_release('enter')      # Press Enter to send msg
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'w')            # Close window
    numbers.remove(number)
    print("Msg Sent to: ", number)

print("All Msgs sent")
