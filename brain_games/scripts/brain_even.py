import prompt
from random import randint

def welcome_user():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print ('Hello,', name)

welcome_user()

print ('Answer "yes" if the number is even, otherwise answer "no".')
score = 0
while score != 3:
    number = randint(1, 100)
    print('Question: ',number)
    otvet = prompt.string('Your answer: ')
    if otvet == 'yes' and number % 2 == 0 or otvet == 'no' and number % 2 != 0:
        print('Correct!')
        score += 1
        if score == 3:
            print('Congratulations,', name,'!')
        continue
        
    else:
        print("""yes' is wrong answer ;(. Correct answer was 'no'.
    Let's try again,""", name, '!')
        break
        
def main():

    if __name__ == '__main__':

        main()
