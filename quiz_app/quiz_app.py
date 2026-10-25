from questions import questions

letters = ["A", "B", "C", "D"]


def show_instructions():
    print("===== QUIZ INSTRUCTIONS =====")
    print("1. The quiz contains multiple-choice questions.")
    print("2. Each question has four options: A, B, C, D.")
    print("3. Enter the letter of your chosen answer.")
    print("4. One point is awarded for each correct answer.")
    print("5. Invalid choices will not be counted.")
    print("=============================")


def ask_question(q):
    print(q["question"])
    i = 0
    while i < 4:
        print(letters[i] + ". " + q["options"][i])
        i = i + 1
    while True:
        try:
            answer = input("Enter your answer: ").strip().upper()
        except (EOFError, KeyboardInterrupt):
            return None
        if answer in letters:
            return answer
        print("Invalid choice. Please enter A, B, C, or D.")


def run_quiz():
    score = 0
    correct = 0
    incorrect = 0
    total = len(questions)

    i = 0
    while i < total:
        print("\nQuestion " + str(i + 1) + ":")
        answer = ask_question(questions[i])
        if answer is None:
            print("Quiz interrupted.")
            return
        if answer == questions[i]["answer"]:
            print("Correct answer!")
            score += 1
            correct += 1
        else:
            print("Incorrect! The correct answer was " + questions[i]["answer"] + ".")
            incorrect += 1
        i = i + 1

    percentage = (score / total) * 100
    print("\n===== QUIZ RESULTS =====")
    print("Total Questions: " + str(total))
    print("Correct Answers: " + str(correct))
    print("Incorrect Answers: " + str(incorrect))
    print("Final Score: " + str(int(percentage)) + "%")

    if percentage == 100:
        performance = "Excellent!"
    elif percentage >= 80:
        performance = "Good job!"
    elif percentage >= 50:
        performance = "Not bad, keep practicing!"
    else:
        performance = "Better luck next time!"

    print("Performance: " + performance)


def main():
    while True:
        print("\n===== QUIZ APPLICATION =====")
        print("1. Start Quiz")
        print("2. View Quiz Instructions")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        match choice:
            case "1":
                run_quiz()
                while True:
                    again = input("Would you like to play again? (yes/no): ").strip().lower()
                    if again == "yes" or again == "y" or again == "no" or again == "n":
                        break
                    print("Please enter yes or no.")
                if again == "no" or again == "n":
                    break
            case "2":
                show_instructions()
            case "3":
                print("Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")


try:
    main()
except (EOFError, KeyboardInterrupt):
    print("\nExiting. Goodbye!")
