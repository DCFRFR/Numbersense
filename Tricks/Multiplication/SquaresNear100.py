import random
import time
questions = int(input("Question count: "))
nums = []
while len(nums) < questions:
    nums = nums + random.sample(range(-15, 16), 31)
start_time = time.perf_counter()
count = 1
wrong = 0
right = 0
while count < questions + 1:
    first = nums[count - 1]
    difference = 100 + first
    question = int(input(f"{count}. What is {difference} squared?: "))
    if question == difference ** 2:
        print("Correct.")
        right = right + 1
    else:
        print(f"Incorrect. {difference} squared is {difference**2}")
        wrong = wrong + 1
    count = count + 1
end_time = time.perf_counter()
elapsed_time = end_time - start_time
time_per_question = elapsed_time / questions
print("")
print(f"Results: {int(((questions - wrong)/questions) * 100)} percent accuracy.")
print(f"{right} correct, {wrong} incorrect.")
print(f"Time: {elapsed_time:.2f} seconds")
print(f"Time per question: {time_per_question: .2f} seconds")
