import time
import random
def int_to_roman(num: int) -> str:
    if not (0 < num < 4000):
        raise ValueError("Number must be between 1 and 3999")

    roman_mapping = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (10, "X"),   (9, "IX"),   (5, "V"),   (4, "IV"),
        (100, "C"),  (90, "XC"),  (50, "L"),  (40, "XL"),
        (1, "I")
    ]
    roman_mapping.sort(key=lambda x: x[0], reverse=True)
    result = []
    for value, symbol in roman_mapping:
        if num == 0:
            break
        count, num = divmod(num, value)
        result.append(symbol * count)
    return "".join(result)
number = random.randint(1,4000)
questions = int(input("Number of questions: "))
start_time = time.perf_counter()
wrong = 0
right = 0
count = 1
while count < questions+1:
    number = random.randint(1,4000)
    number_converted = int_to_roman(number)
    answer = int(input(f"{count}. Convert {number_converted}: "))
    if answer == number:
        print("Correct")
        right = right + 1
    else:
        print(f"Incorrect, {number_converted} = {number}")
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