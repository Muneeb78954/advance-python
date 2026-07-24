"""Quiz Game"""

questions = ("Who Is The Founder Of Python Programming Language? ",
             "In Which Year Python Programming Was First Released ?",
             "In Which Of The Followings Python Is Used? ",
             "Which Of The Following are Python Libraries? ",
             "Are You Expert Python Programmer? ")

options = (("A.Imran Khan ", "B.Nawaz Sharif ", "C.Asim Munir ", "D.Pinki Peerni "),
           ("A.1947 ", "B.2020 ", "C.1998 ", "D.1902 "),
           ("A.Web Development ", "B.AI ", "C.Data Science ", "D.All of these "),
           ("A.Java ", "B.Kotlin ", "C.C# ", "D.None Of these "),
           ("A.NO ", "B.Absolutly NO ", "C.Yes ", "D.100% Yes "))

answers = ("C","A","D","D","C")

guesses = []
score = 0
question_num = 0

for question in questions:
    print("___________________________")
    print(question)

    for option in options[question_num]:
        print(option)

    guess = input("Enter Your Anwser (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect")
        print(f"{answers[question_num]} is the correct answer.")
    question_num += 1


print("______________________________")
print("         RESULTS              ")
print("______________________________")

print("Correct Answers: ", end = " ")
for answer in answers:
    print("Answers: ", end = " ")

print()

print("Your Guesses: ", end = " ")
for answer in answers:
    print("Guesses: ", end = " ")
print()

score = int(len(questions) * 100 )
print(f"Your Score is:{score}%")