import sys
sys.setrecursionlimit(100000)

def strContain(A, B) :
    '''
    문자열 A의 알파벳이 문자열 B에 모두 포함되어 있으면 "Yes", 아니면 "No"를 반환합니다.
    '''
    if A == "":
        return "Yes"
    for i in range(0, len(B)):
        if A[0] == len(B):
            strContain(A[1:], B) 
    return "No"

'''    for i in range(0, len(A)):
        flag = 0
        for j in range(0, len(B)):
            if A[i] == B[j]:
                flag = 1
                break
        if flag == 0:
            return "No"        
    return "Yes"
'''
def main():


def GCD(x, y) :
    '''
    x, y의 최대공약수를 반환하는 함수
    '''
    div = 1
    for i in range(0, x)
    

    return 1

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = input()

    x = int(data.split()[0])
    y = int(data.split()[1])

    print(GCD(x, y))

if __name__ == "__main__":
    main()
   
