def convertBinary(n) :
    '''
    10진수 n을 2진수로 변환하여 반환합니다.

    *주의* : 변환된 2진수는 문자열이어야 합니다.

    예를 들어, 19가 입력될 경우 문자열 "10011"이 반환되어야 합니다.
    '''
    save = ""
    if 
        if  n < 1 :
            return '0'
        elif n == 1 :
            return '1'
        elif :
            if n%2 == 0:
                convertBinary(n/2) + '0'
            else :
                convertBinary(n/2) + '1'
            
        
    


def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    x = input()
    print(checkParen(x))

if __name__ == "__main__":
    main()


