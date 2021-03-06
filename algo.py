
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
    n개의 점들 중에서 2개의 점을 선택했을 때, 얻을 수 있는 기울기의 절댓값 중에서 가장 큰 값을 반환하는 함수를 작성하세요.

    **주의** : 소숫점 넷째자리에서 반올림하는 것은 고려할 필요가 없습니다. 이는 main()에서 출력을 할 때에 처리가 되므로, 기울기의 최댓값을 구하는 것에 집중해 주시길 바랍니다.
    '''

    return 0

def main():
    '''
    이 부분은 수정하지 마세요.
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
    이 부분은 수정하지 마세요.
    '''

    a = int(input())
    b = int(input())

    print(diffDigit(a, b))


if __name__ == "__main__":
    main()

