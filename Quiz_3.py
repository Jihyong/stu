# for a in range(1,21): # for a in range(1,21)[::2]도 가능
#     if a % 2 == 1:
#         print("A{}".format(a),end = " ")

## 신조어 퀴즈 클래스 작성

class Word():
    def __init__(self,word,ex_1,ex_2,ans):
        self.word = word
        self.ex_1 = ex_1
        self.ex_2 = ex_2
        self.ans = ans
    def show_question(self):
        print(f"\"{self.word}\"의 뜻은?")
        print("1."+ self.ex_1)
        print("2."+ self.ex_2)

    def check_answer(self,user_input):
        if user_input == self.ans:
            print("정답입니다.")
        else:
            print("틀렸습니다.")
word = Word("애빼시","애교 빼면 시체","애들은 빼빼로 시시해",1)
word.show_question()
word.check_answer(int(input("=> ")))

#
def three():
    print("three",end=" ")
    return 3
def five():
    print("five",end=" ")
    return 5
def seven():
    print("seven",end=" ")
    return 7
three()>five()>seven()
# 윗줄의 구조는 three()> five() and five() > seven()
# 따라서       이 부분은 False 이기 때문에 and 뒷 부분은 출력 대상이 아님
#             그러므로 함수 실행시 three five 만 출력


