import random
import time
questions = int(input("Question count: ").strip())
start_time = time.perf_counter()
count = 1
wrong = 0
right = 0
while count < questions + 1:
    first = random.randint(100,9999)
    second = random.choice([3,4,6,8,9,11])
    if random.randint(0,1) == 1:
        first = first - first % second
    question = int(input(f"{count}. {first} divisible by {second}? (1 yes, 0 no) : "))
    if first % second == 0:
        answer = 1
    else:
        answer = 0
    if question == answer:
        print("Correct.")
        right = right + 1
    else:
        print(f"Incorrect. {first} divisible by {second}? (1 yes, 0 no) is {answer}.")
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
