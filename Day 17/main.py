from question_model import Question
from data import question_data
from quiz_brain import Quiz
import html

question_bank = []
for question in question_data:
    question_text = html.unescape(question["question"])
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = Quiz(question_bank)
while quiz.has_questions():
    quiz.next_question()

print("\n\nYou've completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
