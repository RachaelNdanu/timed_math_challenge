import random
import time

OPERATORS = ["+" , "-" , "*"]

MIN_OPERAND = 5
MAX_OPERAND = 20
TOTAL_PROBLEMS = 10 

def generate_problem ():
    left = random.randint (MIN_OPERAND , MAX_OPERAND)
    right = random.randint (MIN_OPERAND, MAX_OPERAND)
    operator = random.choice (OPERATORS)

    expr = str(left) + " " + operator +" " + str(right)
    answer = eval(expr)
    return expr ,answer



'''expr, answer = generate_problem()
print(expr, answer)'''

star_time = time.time()

for i in range (TOTAL_PROBLEMS):
    expr , answer =generate_problem()

    while True:
        guess = input("problem #"+ str(i+1) + ": " + expr  + " =")
        if guess == str(answer):
            break


end_time = time.time()
total_time_taken = round( end_time-star_time ,2)

print("congrats! you finished in" , total_time_taken , "seconds!" )