
import time
import threading
from threading import Thread

ACTIVE = True

def spinner():
    while ACTIVE:
        current_thread_obj = threading.current_thread()
        thread_id = current_thread_obj.ident
        print(f"The ID of the current thread is: {thread_id}")
        #pass

def main(threads):
    print("Starting 16 CPU bound Threads")
    for thread in threads:
        thread.start()

    while True:
        time.sleep(0.01)
        print(f"[{time.time():010.6f}] Main thread is still alive!")


if __name__ == "__main__":
    try:
        threads = [Thread(target=spinner) for _ in range(8)]
        main(threads)
    except KeyboardInterrupt:
        print("Stopping threads")
