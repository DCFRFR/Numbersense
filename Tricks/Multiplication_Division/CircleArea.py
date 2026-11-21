import random
import time
import math
questions = int(input("Question count: ").strip())
start_time = time.perf_counter()
count = 1
wrong = 0
right = 0
while count < questions + 1:
    first = random.randint(2,20)
    question = float(input(f"{count}. Area of a circle with radius {first} (within 1%) : "))
    answer = math.pi * first * first
    if abs(question - answer) <= answer * 0.01:
        print("Correct.")
        right = right + 1
    else:
        print(f"Incorrect. Area of a circle with radius {first} is {answer:.2f}.")
        wrong = wrong + 1
    count = count + 1
end_time = time.perf_counter()
elapsed_time = end_time - start_time
time_per_question = elapsed_time / questions
print("")
print(f"Results: {round(right / questions * 100)} percent accuracy.")
print(f"{right} correct, {wrong} incorrect.")
print(f"Time: {elapsed_time:.2f} seconds")
print(f"Time per question: {time_per_question: .2f} seconds")
