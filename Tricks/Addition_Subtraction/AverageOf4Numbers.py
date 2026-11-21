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
    third = random.randint(1,100)
    fourth = random.randint(1,100)
    question = float(input(f"{count}. Average of {first}, {second}, {third}, {fourth} (within 2%) : "))
    answer = (first + second + third + fourth) / 4
    if abs(question - answer) <= answer * 0.02:
        print("Correct.")
        right = right + 1
    else:
        print(f"Incorrect. Average of {first}, {second}, {third}, {fourth} is {answer:.2f}.")
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
