from random import randint

count = 0

for _ in range(10):

    num1 = randint(1,10)
    num2 = randint(1,10)

    question = "What is " + str(num1) + " times " + str(num2) + "? "
    user_answer = int(input(question))
    correct_answer = num1 * num2

    if user_answer == correct_answer:
        print("That's right - well done.")
        count += 1
    else:
        print("No, Im adraid the answer is " + str(correct_answer) + ".")

print("I asked you 10 questions. You got " + str(count) + " of them right. \nWell done!")
