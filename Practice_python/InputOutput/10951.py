## test case 갯수가 주어지지 않는다.
# 참고 사이트
# 1. https://www.acmicpc.net/board/view/855
# 2. 자바의 경우도 Scanner보다 BufferedReader가 빠르다 (why?)
# 3. python -  https://soooprmx.com/archives/8242

import sys
for line in sys.stdin:
    a,b = map(int, line.split())
    print(a+b)

# lines = sys.stdin.readlines()
# a = lines.pop(0)
# b = lines.pop(1)
#

