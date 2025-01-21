from question_model import Question
from data import question_data
from quiz_brain import  QuizBrain
question_bank = []
for ques in question_data:
    question_bank.append(Question(ques["text"], ques["answer"]))

# for item in question_bank:
#     print(item.print_question_data())

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print(f"you answered {quiz.correct_answers} right")