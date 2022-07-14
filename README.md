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

# 기록

- 2022-07-13 콘솔버전 간단한 ToDo앱 구현
- 2022-07-14 Todo앱 NOTION_DB 기능 추가 계획
  - 2022-07-14 NOTION_DB_CREATE 기능 구현
  - 2022-07-15 NOTION_DBB_READ 기능 구현
