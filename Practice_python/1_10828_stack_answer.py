stack=[]
num=int(input())

for i in range(0,num):

    str=input()

    if str=="pop":
        if len(stack)==0:
            print("-1")
        else:
            print(stack[0])
            del stack[0]

    elif str=="size":
        print(len(stack))
    elif str=="empty":
        if len(stack)==0:
            print("1")
        else:
        #아니면
            print("0")
    elif str=="top":
        if len(stack)==0:
            print("-1")
        else:#아니면
            print(stack[0])
    elif str[0:4]=="push":
    #이제 push x명령어를 쓸 차례입니다 입력하게 될 push 4는 숫자와 문자의 혼합형태입니다 하지만 우리는 숫자만 뽑아서 리스트에 추가해야합니다. 또한 push명령어를 인식해야 할 필요성도 있습니다 따라서 만약 사용자가 push x라는 명령어를 입력하면 4글자까지 슬라이싱하여 push만 인식하도록 합시다.
        stack.insert(0,str[5:])
        #그럼 띄어쓰기를 제외한 5번째 글자(push x면 x(문자형 숫자))를 리스트의 맨 앞쪽으로 추가합시다 insert를 쓴 이유는 append는 맨 마지막에 추가합니다 insert는 자기가 추가할 위치를 지정할 수 있습니다. 이 문제는 리스트의 맨 앞에 숫자를 추가해야하므로 0,str[5:]를 이용해 숫자를 추가하면 됩니다.