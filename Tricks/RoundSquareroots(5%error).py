import random
import time
questions = int(input("Question count: ").strip())
start_time = time.perf_counter()
count = 1
wrong = 0
right = 0
while count < questions + 1:
    first  = random.randint(169,1400)
    question = int(input(f"{count}. What is the square root of {first}? (Integer answer): "))
    root = (first)**0.5
    lowerbound = root*0.95
    upperbound = root*1.05
    if  lowerbound <= question <= upperbound:
        print("Correct. ")
        print(f"Bounds:{lowerbound:.3f} <= {root:.3f} <= {upperbound:.3f} ")
        right = right + 1
    else:
        print("Incorrect")
        print(f"Bounds:{lowerbound:.3f} <= {root:.3f} <= {upperbound:.3f}")
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
