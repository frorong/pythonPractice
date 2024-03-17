def selectType():
    num =  int(input('1. 입력한 수식 계산, 2. 두 수 사이의 합계 : '))
    if num == 1: calcNum()
    elif num == 2: plusNum()

def calcNum():
    target =  str(input('수식을 입력하세요 : '))
    result = eval(target)
    print("{} 결과는 {} 입니다.".format(target, result))

def plusNum():
    num1 =  int(input('첫 번째 숫자를 입력하세요 : '))
    num2 =  int(input('두 번째 숫자를 입력하세요 : '))
    
    cnt = 0;

    for i in range (num1, num2 +1): cnt += i

    print("{} +..+ {} 은(는) {} 입니다.".format(num1, num2, cnt))


selectType();