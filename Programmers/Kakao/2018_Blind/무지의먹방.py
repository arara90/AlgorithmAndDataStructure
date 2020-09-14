#  시간이 적은 애부터 처리하는 그리디 알고리즘
#  음식의 수를 최대한 줄이 ㄴ뒤에 k시간이후에 어떤 음식을 먹으면 되는지


def solution(food_times=[3, 1, 2], k = 5):
    answer = 0
    
    cnt = 0
    time = 0
    length = len(food_times)
    mask = [ 1 for _ in range(len(food_times))] 
    
    while(k > cnt):
        print(food_times, mask)
        i = cnt%length
        
        if(mask[i]):
            time+=1
            food_times[i] -= 1
            
            if(food_times[i]==0):
                mask[i] = 0
        
            if(k==time):             
                while(mask[i] == 0):
                    cnt+=1
                    i = cnt % length
    
                    
         
        cnt+=1

    return answer

print(solution())