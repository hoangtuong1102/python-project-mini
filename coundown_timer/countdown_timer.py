import time

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer)
        time.sleep(1)
        seconds -=1
    print("Time's up")

def main():
    try:
        total_seconds = int(input("Enter the number of seconds: "))
        countdown(total_seconds)

    except ValueError:
        print("Invalid input")

if __name__ == '__main__':
    main()