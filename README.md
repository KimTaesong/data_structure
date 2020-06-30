# data_structure

파이썬으로 구현하는 자료구조

# 01. Stack 이란

스택은 데이터의 삽입과 삭제가 저장소의 맨 윗 부분 the top of stack에서만 일어나는 자료구조

스택은 데이터가 순서대로 저장되고 스택의 마지막에 넣은 요소가 처음으로 꺼내진다.
LIFO: Last-in, First-out
Stack은 연속으로 저장된 데이터 구조를 가지고 있고 맨 위 요소에 대한 포인터(주소값)를 가지고 있는
Array나 Sigly linked list로 구현할 수 있음.

- 장점: 참조 지역성(한번 참조된 곳은 다시 참조될 확률이 높다)을 활용
- 단점: 데이터를 탐색하기 어렵다는 점
- 활용: 함수의 콜스택, 문자열을 역순으로 출력, 연산자 후위표기법 등 사용

# 02. Stack의 ADT(abstract data type)

push(->None): 맨 위에 값 추가

pop(data): 가장 최근에 넣은 맨 위의 값을 제거

peak(-> data or -1): 스택의 변형 없이 맨 위에 값을 출력

is_empty(->boolean): 스택이 비어있는지 확인

# 03. Stack 구현하기 - List

Python의 List는 **동적 배열(Dynamic Array)**이므로 배열에 <u>새로운 원소를 삽입, 삭제</u> 가능<br>
List 변수에는 첫번째 원소(맨 아래)의 주소값이 저장되므로 맨 마지막으로 삽입한 원소(맨 위)의 주소값도<br>
바로 구할 수 있음. 이 점을 활용해서 List로 Stack을 구현할 수 있음.<br>
List를 사용하여 원소를 삽입(push), 삭제(pop) 작업을 수행했을 때는 시간복잡도는 O(1)이다.<br>

# 04. Stack 구현하기 - Signly linked list

Linked list의 head는 Stack의 가장 윗 부분을 가리킨다.<br>

> https://daimhada.tistory.com/72?category=820522 - 개발하는 다임하게님 글 참고
