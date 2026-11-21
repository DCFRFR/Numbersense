import random
import time
questions = int(input("Question count: ").strip())
start_time = time.perf_counter()
count = 1
wrong = 0
right = 0
while count < questions + 1:
    first = random.randint(0,1)
    second = random.randint(3,12)
    third = random.randint(10,100)
    fourth = third + random.randint(100,900)
    fifth = random.randint(1,9)
    if first == 1:
        text = f"How many 3-digit integers end in {fifth}?"
    else:
        text = f"How many multiples of {second} from {third} to {fourth} inclusive?"
    question = int(input(f"{count}. {text} : "))
    if first == 1:
        answer = 90
    else:
        answer = fourth // second - (third - 1) // second
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
