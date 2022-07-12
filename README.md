# todo

# 콘솔버전 todo

```py
todoList = []


def main():
    while True:
        print("번호를 입력해주세요. (1. 할일추가 2. 할일보기 3. 할일완료 0. 종로)")
        num = int(input())
        if not num:
            break
        elif num == 1:
            print("할일이 무엇인가요? ")
            todoList.append(input())
        elif num == 2:
            for todo in todoList:
                print(todo)
        elif num == 3:
            print("무슨일을 완료했나요?")
            todoList.remove(input())


if __name__ == "__main__":
    main()

```