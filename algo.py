
from cmath import sqrt
import sys
import math
def getSlope(arr) :
    return abs((arr[1] - arr[3])/(arr[0] - arr[2]))
def maxSlope(points) :
    result = []
    for i in range(len(point)-2) :
        for j in range(i+1, len(points)-1) :
            result.append(pow((points[i][1] - points[j][1]), 2)+pow((points[i][0] - points[j][0]),2))
    return max(result)
    '''
    n���� ���� �߿��� 2���� ���� �������� ��, ���� �� �ִ� ������ ���� �߿��� ���� ū ���� ��ȯ�ϴ� �Լ��� �ۼ��ϼ���.

    **����** : �Ҽ��� ��°�ڸ����� �ݿø��ϴ� ���� ����� �ʿ䰡 �����ϴ�. �̴� main()���� ����� �� ���� ó���� �ǹǷ�, ������ �ִ��� ���ϴ� �Ϳ� ������ �ֽñ� �ٶ��ϴ�.
    '''

    return 0

def main():
    '''
    �� �κ��� �������� ������.
    '''

    n = int(input())
    points = []

    for i in range(n) :
        line = [int(x) for x in input().split()]
        points.append( (line[0], line[1]) )

    print("%.3lf" % maxSlope(points))

if __name__ == "__main__":
    main()


def main():
    '''
    �� �κ��� �������� ������.
    '''

    a = int(input())
    b = int(input())

    print(diffDigit(a, b))


if __name__ == "__main__":
    main()

