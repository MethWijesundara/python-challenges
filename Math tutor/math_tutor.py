from random import randrange as r
from time import time as t

no_questions = int(input('How many questions do you want?: '))
max_num = int(input('Highest number used in practice?: '))

score = 0
answer_list = []

start = t()

for q in range(no_questions):
    num1,num2 = r(1, max_num+1 ),r(1, max_num + 1)
    ans=num1*num2

    user_ans = int(input(f"Question {q+1}: {num1} X {num2} = "))

    #User a checkmark of cross for feebback
    mark = "✅" if user_ans == ans else "❌"
    answer_list.append(f'{num1}X{num2} = {ans} | You: {user_ans} {mark}')

    if user_ans == ans:
        score+=1

end = t() #Moved outside the loop
total_time = end - start

print(f'\nThank you for playing!')
print(f'Score: {score}/{no_questions} ({round(score/no_questions*100)}%)')
print(f'Total time: {round(total_time,1)}s ({round(total_time/no_questions,1)})')

print("\n=== Review ===")
for line in answer_list :
    print(line)