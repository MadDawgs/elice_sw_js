import sys
sys.setrecursionlimit(100000)

def strContain(A, B) :
    '''
    ���ڿ� A�� ���ĺ��� ���ڿ� B�� ��� ���ԵǾ� ������ "Yes", �ƴϸ� "No"�� ��ȯ�մϴ�.
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
    x, y�� �ִ������� ��ȯ�ϴ� �Լ�
    '''
    div = 1
    for i in range(0, x)
    

    return 1

def main():
    '''
    �� �κ��� �������� ������.
    '''

    data = input()

    x = int(data.split()[0])
    y = int(data.split()[1])

    print(GCD(x, y))

if __name__ == "__main__":
    main()
   
