# countdown clock and counter 
import time
def ask_number():
    while True:
            tm = input("please enter a number \n >")
            global tms
            try:
                tms = int(tm)
            except ValueError:
                time.sleep(5)
                print("Please enter a valid number ! \n")
            else:
                break

def counter():
    for seconds in range(tms):
        seconds = seconds + 1
        print(seconds)
        time.sleep(1)
        if seconds == tms:
            print("Time has finished")
            time.sleep(5)
def countdown():
    for seconds in range(tms):        
        count_down = tms - seconds
        print(count_down)
        time.sleep(1)

ask_number()

ask_user = input(" Do you want counter or count down ? ")
print("/counter /countdown ")
if ask_user == "counter":
    counter()
elif ask_user == "countdown":
    countdown()


