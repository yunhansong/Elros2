from Dictionary import *
import random


class Question:
    my_dic = Dictionary()

    def __init__(self):
        print('initialize Question')
        self.my_dic.read_from_dictionary()

    def add_dic_to_question(self):
        chose = random.randrange(1, 3)  # 한글 or 영어 문제 골라주는 변수

        en_words = self.my_dic.get_dictionary(2)  # Dictionary class에서 get_dictionary함수를 통해 en_list 빼오기
        kr_words = self.my_dic.get_dictionary(1)  # Dictionary class에서 get_dictionary함수를 통해 kr_list 빼오기
        if chose == 1:
            kr_ask = random.randint(0, kr_words.__len__() -1)  # 문제 낼 kr 단어 번호를 정하기
            kr_question = kr_words.pop(kr_ask)  # kr_words에서 pop으로 문제낼 단어를 빼와 kr_question에 저장
            answer = input('[Q]' + kr_question + ' -> ')
            en_answer = en_words.pop(kr_ask)
            test = en_answer.split(",")
            if test.__len__() > 1:
                print("1st :" + test[0] + "2nd: " + test[1])
            is_correct = False
            for i in test:
                if i == answer:
                    is_correct = True
                    break
            if is_correct:
                print('[Bingo!] good job')
                print("정답:",test) 
            else:
                print('[XXX] study harder!!')
                print("정답",test) 

        else:
            en_ask = random.randint(0, en_words.__len__() -1)  # 문제 낼 en 단어 번호를 정하기
            en_question = en_words.pop(en_ask)  # en_words에서 pop으로 문제낼 단어를 빼와 en_question에 저장
            answer = input('[Q]' + en_question + ' -> ')
            kr_answer = kr_words.pop(en_ask)
            test = kr_answer.split(",")# 이 코드와 
            if test.__len__() > 1:# 이 코드 때문에(정확히는 모르겠지만 아래 코드들도 포함)뜻이 2개인 단어의 정답이 적용됨
                number = 1 # 문제의 뜻의 개수를 담는 변수
                for word in test:
                    print("정답:", number , word)
                    number = number + 1   
            is_correct = False
            for i in test:
                if i == answer:
                    is_correct = True
                    break
            if is_correct:
                print('[Bingo!] good job!!')
                print("정답:",test) 
            else:
                print('[XXX] study harder!!')
                print("정답",test) 
        return is_correct
