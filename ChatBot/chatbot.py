bot_name = "Charlie"
birth_year = 2025
print("Hello! My name is " + bot_name + ".")
print("I was created in " + str(birth_year) + ".")
print("Please, remind me your name.")
user_name = input("> ")
print("What a great name you have, " + user_name + "!")
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")
remainder3 = int(input("> "))
remainder5 = int(input("> "))
remainder7 = int(input("> "))
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print("Your age is " + str(age) + ";")
print("that's a good time to start programming!")
print("Now I will prove to you that I can count to any number you want.")
count_to = int(input("> "))
for i in range(count_to + 1):
   print(str(i)+"!")
print("Completed, have a nice day!")
print("Let's test your programming knowledge.")
print("Why do we use methods?")
print("1. To repeat a statement multiple times.")
print("2. To decompose a program into several small subroutines.")
print("3. To determine the execution time of a program.")
print("4. To interrupt the execution of a program.")
correct_answer = "2"
user_answer = ""
while user_answer != correct_answer:
    user_answer = input("> ")
    if user_answer != correct_answer:
        print("Please, try again.")
print("Completed, have a nice day!")
print("Congratulations, have a nice day!")