import random
import time
questions = int(input("Question count: ").strip())
start_time = time.perf_counter()
count = 1
wrong = 0
right = 0
while count < questions + 1:
    first  = random.randint(1,1000000000)
    question = int(input(f"{count}. {first} / 7 (remainder) : "))
    answer = first  % 7
    if question == answer:
        print("Correct.")
        right = right + 1
    else:
        print(f"Incorrect. {first} / 7 (remainder) is {answer}.")
        wrong = wrong + 1
    count = count + 1
end_time = time.perf_counter()
elapsed_time = end_time - start_time
time_per_question = elapsed_time / questions
print("")
print(f"Results: {(int((questions - wrong)/questions)) * 100} percent accuracy.")
print(f"{right} correct, {wrong} incorrect.")
print(f"Time: {elapsed_time:.2f} seconds")
