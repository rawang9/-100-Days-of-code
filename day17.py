# =============================================================================
# class User:
#     def __init__(self,id,usename):
#         self.id=id
#         self.uname=usename
#         self.follow=0
#         self.following=0
#     def followr(self,user):
#         user.following+=1
#         self.follow+=1
# u1=User("001","Akarshit")
# u2=User("002","Rakesh")
# print(u1.following)
# print(u1.follow)
# u1.followr(u2)
# print(u2.following)
# print(u1.follow)
# =============================================================================
question_data = [{"category":"Science: Computers","type":"boolean","difficulty":"easy","question":"Linus Torvalds created Linux and Git.","correct_answer":"True","incorrect_answers":["False"]},{"category":"Science: Computers","type":"boolean","difficulty":"easy","question":"The programming language &quot;Python&quot; is based off a modified version of &quot;JavaScript&quot;.","correct_answer":"False","incorrect_answers":["True"]},{"category":"Science: Computers","type":"boolean","difficulty":"easy","question":"The logo for Snapchat is a Bell.","correct_answer":"False","incorrect_answers":["True"]},{"category":"Science: Computers","type":"boolean","difficulty":"easy","question":"Pointers were not used in the original C programming language; they were added later on in C++.","correct_answer":"False","incorrect_answers":["True"]},{"category":"Science: Computers","type":"boolean","difficulty":"easy","question":"&quot;HTML&quot; stands for Hypertext Markup Language.","correct_answer":"True","incorrect_answers":["False"]},{"category":"Science: Computers","type":"boolean","difficulty":"easy","question":"Time on Computers is measured via the EPOX System.","correct_answer":"False","incorrect_answers":["True"]},{"category":"Science: Computers","type":"boolean","difficulty":"easy","question":"The Windows 7 operating system has six main editions.","correct_answer":"True","incorrect_answers":["False"]},{"category":"Science: Computers","type":"boolean","difficulty":"easy","question":"The Windows ME operating system was released in the year 2000.","correct_answer":"True","incorrect_answers":["False"]},{"category":"Science: Computers","type":"boolean","difficulty":"easy","question":"Linux was first created as an alternative to Windows XP.","correct_answer":"False","incorrect_answers":["True"]},{"category":"Science: Computers","type":"boolean","difficulty":"easy","question":"The Python programming language gets its name from the British comedy group &quot;Monty Python.&quot;","correct_answer":"True","incorrect_answers":["False"]}]
class Ques:
    def __init__(self,ques,ans):
        self.text=ques
        self.ans=ans
    def check(self,chosen):
        return self.ans==chosen
    
question_bank=[]
for data in question_data:
    ques=data["question"]
    answ=data["correct_answer"]
    merge=Ques(ques,answ)
    question_bank.append(merge)
    
class QuesBrain:
    def __init__(self,lst):
        self.no=0
        self.qbank=lst
        self.score=0
    def still_have_ques(self):
        return len(self.qbank)>self.no
    def next_question(self):
        current_ques=self.qbank[self.no]
        self.no+=1
        ask=input(f"Q.{self.no}: {current_ques.text}. (True/False)?: ")
        self.check_ans(ask,current_ques.ans)
    def check_ans(self,ask,correct):
        if ask.lower()==correct.lower():
            self.score+=1
            print("you got it")
        else:
            print("its wrong")
        print(f"the corrent ans was {correct}")
        print(f" your score is {self.score}/{self.no}")
    def final(self):
        print("You've completed the quiz! ")
        print(f"Your final score was {self.score}/{self.no}")
        
quiz=QuesBrain(question_bank)
while quiz.still_have_ques():
    quiz.next_question()
quiz.final()
print(quiz.score,'/',quiz.no)