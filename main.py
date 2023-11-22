from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questions_bank = []
for questions in question_data:
    question_text = questions["text"]
    questions_answer = questions["answer"]
    new_question = Question(question_text, questions_answer)
    questions_bank.append(new_question)

quiz = QuizBrain(questions_bank)

while quiz.still_has_questions():
    quiz.next_questions()

print("You have completed the quiz")
print(f"Your final is score is {quiz.score}/{quiz.question_number}")



