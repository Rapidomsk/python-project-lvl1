import prompt
import random
from random import randint

def welcome_user():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print ('Hello,', name)

welcome_user()

print ('What is the result of the expression?')

score = 0

while score != 100:
    number1, number2, arithm, question, answer = 0, 0, '', '', 0
    arithmetic = ['+', '-', '*']
    number1 = randint(0, 100)
    number2 = randint(0, 100)
    arithm = random.choice(arithmetic)
    question = str(number1) + arithm + str(number2)
    if arithm == '+':
        answer = number1 + number2
    elif arithm == '-':
        answer = number1 - number2
    elif arithm == '*':
        answer = number1 * number2
    print('Question: ',question, answer)
    otvet = prompt.integer('Your answer: ')
    if otvet == answer:
        print('Correct!')
        score += 1
        if score == 3:
            print('Congratulations,', name,'!')
        continue
    else:
        print("""yes' is wrong answer ;(. Correct answer was 'no'.
    Let's try again,""", name, '!')
        break
