import time

def cake_countdown(seconds):
    print("Cake countdown begins!")
    for i in range(seconds, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    print("Cake time! 🎂")

if __name__ == "__main__":
    cake_countdown(10)
