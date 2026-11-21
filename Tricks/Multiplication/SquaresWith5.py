import random
import time
questions = int(input("Question count: "))
pool = list(range(5, 100, 10))
nums = []
while len(nums) < questions:
    nums = nums + random.sample(pool, len(pool))
start_time = time.perf_counter()
count = 1
wrong = 0
right = 0
while count < questions + 1:
    first = nums[count - 1]
    question = int(input(f"{count}. What is {first} squared?: "))
    if question == first ** 2:
        print("Correct.")
        right = right + 1
    else:
        print(f"Incorrect. {first} squared is {first ** 2}")
        wrong = wrong + 1
    count = count + 1
end_time = time.perf_counter()
elapsed_time = end_time - start_time
time_per_question = elapsed_time / questions
print("")
print(f"Results: {int(((questions - wrong) / questions) * 100)} percent accuracy.")
print(f"{right} correct, {wrong} incorrect.")
print(f"Time: {elapsed_time:.2f} seconds")
print(f"Time per question: {time_per_question:.2f} seconds")