# EOF를 만날 때까지, 파일 읽기를 반복합니다.
# f = open('myfile.txt', 'r')
# while True:
#     line = f.readline()
#     if not line: break
#     raw = line.split()
#     print(raw)
# f.close()

#with-as
# 파일을 close 하지 않아도 됩니다: with - as 블록이 종료되면 파일이 자동으로 close 됩니다.
# readlines가 EOF까지만 읽으므로, while 문 안에서 EOF를 체크할 필요가 없습니다.

with open('myfile.txt') as file:
  for line in file.readlines():
    print(line.strip().split('\t'))