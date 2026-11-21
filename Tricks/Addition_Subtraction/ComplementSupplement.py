import random
import time
questions = int(input("Question count: ").strip())
start_time = time.perf_counter()
count = 1
wrong = 0
right = 0
while count < questions + 1:
    first = random.randint(10,80)
    second = random.randint(0,1)
    if second == 1:
        text = f"Complement of {first} degrees"
    else:
        text = f"Supplement of {first + 20} degrees"
    question = int(input(f"{count}. {text} : "))
    if second == 1:
        answer = 90 - first
    else:
        answer = 160 - first
    if question == answer:
        print("Correct.")
        right = right + 1
    else:
        print(f"Incorrect. {text} is {answer}.")
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
