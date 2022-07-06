

print('Project - Math Tutor')

#import modules
from  random import randrange as r
from time import time as t
# ask how many questions user wants
no_questions = int(input('How many questions do you want?: '))
max_num =int(input('Highest number used in practice?: '))
#set score start at zero
score = 0
answer_list = []
#loop through number of questions
start = t()
for q in range(no_questions):
    num1,num2 = r(1,max_num+1),r(1,max_num+1)
    ans = num1 * num2
    u_ans =int(input(f'{num1} X {num2} = '))
    answer_list.append(f'{num1} X {num2} = {ans} you:{u_ans}')
    if u_ans == ans:
        score += 1
    end = t()
print(f'Thank you for playing! \nYou got {score} out of {no_questions} ({round(score/no_questions*100)}%) correct in {round(end-start,1)} seconds ({round((end-start)/no_questions,1)}seconds/question)')
for a in answer_list:
    print(a)
# create two random numbers and calc answer
# show user the question
# capture answer and modify user score
# output final score





def questions(q_n):
    import random
    answer_list = []
    for i in range(q_n):
        num_a = random.randint(0, 10)
        num_b = random.randint(0, 10)
        result = num_a * num_b
        answer = input(f'Ile to jest {num_a} * {num_b} = ')
        points = 0
        if int(answer) == result:
            msg = f'{answer} to jest poprawna odpowiedź'
            print(msg)
            points += 1
        else:
            msg = f'Twoja odpowiedź {answer} jest błędna.\n Wynik z działania {num_a} * {num_b} = {result}'
            print(msg)

        answer_list += [msg, points]
    print(list(answer_list))


def math_tutor():
    questions_number = int(input('Podaj liczbę zadań do zrobienia: '))
    # print(type(questions_number))
    # print(isinstance(questions_number, int))
    if isinstance(questions_number, int):
        questions(int(questions_number))
    elif type(questions_number) is not int:
        questions(3)


# math_tutor()
