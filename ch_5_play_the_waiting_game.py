import time
from random import random


def waiting_game():
    target_time = (random() * 2) + 2
    print(f"Your target time is {target_time} seconds")

    input("---Press Enter to Begin---")
    start_time = time.perf_counter()

    input("...Press Enter again after 4 seconds...")
    stop_time = time.perf_counter()

    elapsed = stop_time - start_time
    print(f"Elapsed time: {elapsed} seconds")

    if (elapsed > target_time + 0.1):
        print("Too slow!")
    elif (elapsed < target_time - 0.1):
        print("Too fast!")
    else:
        print("Great timing!")
    print(f"Target time was {target_time}, elapsed time was {elapsed}")


waiting_game()
