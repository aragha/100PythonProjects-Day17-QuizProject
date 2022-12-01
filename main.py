from question_model import Question
from data import question_data1
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
# load question from data.py into a list of objects(class instances)
for i in range(0, len(question_data1)):
    q = Question(question_data1[i]['text'], question_data1[i]['answer'])
    question_bank.append(q)
for i in range(0, len(question_data)):
    q = Question(question_data[i]['question'], question_data[i]['correct_answer'])
    question_bank.append(q)

# print(len(question_bank))
# for i in range(0, len(question_bank)):
#     print(question_bank[i].text, question_bank[i].answer)

# all the questioning, checking the answers, posing the next question etc. will be done in quiz_brain file
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f"Your score was: {quiz.score}!!!")
