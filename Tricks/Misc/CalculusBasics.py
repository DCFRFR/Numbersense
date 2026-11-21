import random
import time

def poly_text(co):
    sup = ["", "", "^2", "^3", "^4"]
    s = ""
    for p in range(len(co) - 1, -1, -1):
        c = co[p]
        if c == 0:
            continue
        a = abs(c)
        t = (str(a) if a != 1 or p == 0 else "") + ("x" + sup[p] if p > 0 else "")
        if s == "":
            s = ("-" if c < 0 else "") + t
        else:
            s = s + (" - " if c < 0 else " + ") + t
    return s


questions = int(input("Question count: ").strip())
start_time = time.perf_counter()
count = 1
wrong = 0
right = 0
while count < questions + 1:
    first = random.randint(0,3)
    second = random.randint(-5,5)
    third = random.randint(-5,5)
    fourth = random.randint(1,6)
    fifth = random.randint(1,4)
    if first == 0:
        text = f"Slope of the tangent to y = {poly_text([third, second, 1])} at x = {fourth}"
    elif first == 1:
        text = f"Limit of (x^2 - {fourth * fourth}) / (x - {fourth}) as x approaches {fourth}"
    elif first == 2:
        text = f"Integral of x dx from 0 to {fourth * 2}"
    else:
        text = f"f'({fourth}) if f(x) = {poly_text([0, 0, second, fifth])}"
    question = int(input(f"{count}. {text} : "))
    if first == 0:
        answer = 2 * fourth + second
    elif first == 1:
        answer = 2 * fourth
    elif first == 2:
        answer = 2 * fourth * fourth
    else:
        answer = 3 * fifth * fourth * fourth + 2 * second * fourth
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
