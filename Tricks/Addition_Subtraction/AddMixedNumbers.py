import random
import time
from fractions import Fraction

def parse(text):
    text = text.strip()
    if " " in text:
        whole, part = text.split(" ", 1)
        sign = -1 if whole.startswith("-") else 1
        return Fraction(whole) + sign * Fraction(part)
    return Fraction(text)


def mixed(f):
    whole = f.numerator // f.denominator
    rest = f - whole
    if rest == 0:
        return str(whole)
    if whole == 0:
        return f"{rest.numerator}/{rest.denominator}"
    return f"{whole} {rest.numerator}/{rest.denominator}"


questions = int(input("Question count: ").strip())
start_time = time.perf_counter()
count = 1
wrong = 0
right = 0
while count < questions + 1:
    first = random.randint(1,9)
    second = random.randint(10,30)
    third = random.choice([2,3,4,5])
    fourth = random.choice([2,3,4,5,6])
    fifth = random.randint(1,third - 1)
    sixth = random.randint(1,fourth - 1)
    question = parse(input(f"{count}. {first} {fifth}/{third} + {second} {sixth}/{fourth} (mixed number) : "))
    answer = Fraction(first) + Fraction(fifth, third) + Fraction(second) + Fraction(sixth, fourth)
    if question == answer:
        print("Correct.")
        right = right + 1
    else:
        print(f"Incorrect. {first} {fifth}/{third} + {second} {sixth}/{fourth} is {mixed(answer)}.")
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
