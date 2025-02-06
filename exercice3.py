import threading
import time

def my_callback():
    print("Timer finished!")

print("Timer started")

def start_timer(seconds, callback):
    def my_sleep():
        
        for i in range(1, 6):
            print(i, "mississipi")
            time.sleep(seconds)  

        callback()  
    
    thread = threading.Thread(target=my_sleep)
    thread.start()

start_timer(1, my_callback)

