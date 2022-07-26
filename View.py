import Model
import Controller

def print_status():
    for i in Model.read():
        print(i)

def print_menu():
    print("번호를 입력해주세요. (1. 할일추가 2. 할일완료 0. 종료)")
    if not Controller.controller(int(input())):
        print("프로그램이 종료됩니다.")
        return True

def print_question():
    print("문구를 적어주세요.")
    return input()