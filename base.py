import pyautogui
import time




time_str = input("How many minutes would you like to run this command?")

run_str = "0"
run_base = int(run_str)

x = True

print("You have chosen " + time_str + " minutes.")
print("Rerun this code if you have typed incorrectly.")

time_int = int(time_str)

time_var = time_int * 60

print(time_var)

while x == True:

    run_var = run_base + 1
    run_base = run_var
    print(run_var)
    time.sleep(1)


pyautogui.dragRel(0, 100, duration = 0.5)