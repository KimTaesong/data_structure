# List를 활용한 Stack 구현
class Stack(list):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            return -1
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False


"""
파이썬의 메인 함수
__name__이라는 변수의 값이 __main__이라면 아래의 코드를 실행

파이썬의 특징
1. 들여쓰기를 통해 코드 실행의 레벨을 결정
2. main이 존재하지 않는다.

파이썬은 다양한 정보를 담고 있는 내장변수가 존재.
__name__이라는 내장변수: 현재 모듈의 이름을 담고있는 내장 변수
직접 실행된 모듈의 경우 __main__이라는 값을 가지게 되며,
직접 실행되지 않은 import된 모듈은 모듈의 이름(파일명)을 가지게 된다.


if __name__ =="__main__" : 메인 함수의 선언, 시작을 의미
해당 코드 밑에 함수 호출 코드를 작성해서 함수의 기능을 수행
"""

if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.peek())  # 3
    print(stack.pop())  # 3
    print(stack.pop())  # 2
    print(stack.pop())  # 1
    print(stack.pop())      # -1 (스택 안에 원소가 없으므로)
