class QuizBrain:
    def __init__(self, qlist):
        self.question_number = 0
        self.question_list = qlist
        self.score = 0
    def check_answer(self, response):
        if response == (self.question_list[self.question_number].answer).lower():
            self.score += 1
            print("That's great! You got it right!!!")
            print(f"Your current score is: {self.score}")
        else:
            print("try again!")
        print(f"The correct answer was:{self.question_list[self.question_number].answer}")
        print("\n")
    def next_question(self):
        # self.question_number += 1
        response = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text}. Enter True/False: ")
        response = response.lower()
        self.check_answer(response)
        self.question_number += 1

    def still_has_questions(self):
        return(self.question_number < len(self.question_list))