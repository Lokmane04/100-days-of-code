class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number + 1} : {current_question.text} (True/False)?: ")
        self.check_answer(answer, current_question)

    def check_answer(self, answer, question):
        if question.answer.lower() == answer.lower():
            print("You got it right !!")
            self.score += 1
        else:
            print("That's wrong !")
        print(f"The correct answer was {question.answer}")
        print(f'Your  current score is : {self.score}/{self.question_number}\n')

    def quiz_finished(self):
        emoji = ""
        if self.score == 12:
            emoji += "🏆🏆"
        elif self.score > 10:
            emoji += "🥳"
        elif self.score > 6:
            emoji += "🎉"
        elif self.score > 4:
            emoji += "👍"
        elif self.score > 2:
            emoji += "😊"
        elif self.score > 0:
            emoji += "😅"
        else:
            emoji += "😢"
        print("You've completed the quiz !!")
        print(f"You're final score is : {self.score}/{self.question_number}  {emoji} {emoji}\n")
