import random
import time
questions = int(input("Question count: ").strip())
start_time = time.perf_counter()
count = 1
wrong = 0
right = 0
while count < questions + 1:
    first = random.randint(1,100)
    second = random.randint(1,100)
    question = float(input(f"{count}. {first} x {first} / {second} (2 decimals) : "))
    answer = round(first * first / second, 2)
    if abs(question - answer) <= 0.0051:
        print("Correct.")
        right = right + 1
    else:
        print(f"Incorrect. {first} x {first} / {second} is {answer}.")
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
