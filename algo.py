def convertBinary(n) :
    '''
    10���� n�� 2������ ��ȯ�Ͽ� ��ȯ�մϴ�.

    *����* : ��ȯ�� 2������ ���ڿ��̾�� �մϴ�.

    ���� ���, 19�� �Էµ� ��� ���ڿ� "10011"�� ��ȯ�Ǿ�� �մϴ�.
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
    �� �κ��� �������� ������.
    '''

    x = input()
    print(checkParen(x))

if __name__ == "__main__":
    main()


