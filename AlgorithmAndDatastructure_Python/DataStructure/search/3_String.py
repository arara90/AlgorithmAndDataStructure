# 문자열 검색 알고리즘

org_str = 'abchijdefghijk'
s_str = 'hi'
count = 0

for start in range(len(org_str)):
    for i in range(len(s_str)):
        if org_str[start] == s_str[i]:          # 각 단어의 첫번째 단어 비교
            if org_str[start+1] == s_str[i+1]:  # 두번째 단어 비교
                count += 1                         # 두 개의 단어가 같으면 하나 증가

        else:
            break

print(f'몇개?: {count}')