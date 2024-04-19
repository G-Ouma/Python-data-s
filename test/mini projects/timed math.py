import random
import time

OPERATORS = ['+', '-', '*']
MIN_OPERAND = 2
MAX_OPERAND = 12
MAX_QUIZ = 10


def gen_quiz():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operand = random.choice(OPERATORS)
    exp = str(left) + " " + operand + " " + str(right)
    ans = eval(exp)
    return exp, ans


strt = input("Press Enter to start!")
print("-----------------------------")

strt_time = time.time()

wrong = 0
attempt = 0
for i in range(MAX_QUIZ):
    quiz, answer = gen_quiz()
    while True:
        attempt += 1 
        user = input("Quiz #" + str(i + 1) + ": " + quiz + " = ")
        if user == str(answer):
            break
        wrong += 1

end_time = time.time()
duration = round(end_time - strt_time, 2)
print("-----------------------------")
print("Nice work! You completed in", duration, "seconds!")
print("You completed in", attempt, "attempts.")