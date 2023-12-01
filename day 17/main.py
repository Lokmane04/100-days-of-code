from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(q_text=question['question'], q_answer=question['correct_answer']))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
quiz.quiz_finished()