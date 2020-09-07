def solution(brown, yellow):
    answer = []
    total = brown + yellow
    height = 3
    width = total
    case_li = []
                
    while(total / height >= height):
        
        if(total % height == 0):
            width = total // height
            case_li.append((width, height))
        height+=1
    # print(case_li)
    
    
    y_height = 1
    y_width = yellow
    case_y = []
    
    while(yellow / y_height >= y_height):
        if(yellow % y_height == 0):
            y_width = yellow // y_height
            case_y.append((y_width, y_height))
            
        y_height+=1
    
#     print(case_y)def solution(brown, yellow):
    answer = []
    total = brown + yellow
    height = 3
    width = total
    case_li = []
                
    while(total / height >= height):
        
        if(total % height == 0):
            width = total // height
            case_li.append((width, height))
        height+=1
    # print(case_li)
    
    
    y_height = 1
    y_width = yellow
    case_y = []
    
    while(yellow / y_height >= y_height):
        if(yellow % y_height == 0):
            y_width = yellow // y_height
            case_y.append((y_width, y_height))
            
        y_height+=1
    
#     print(case_y)
    
    for case in case_li:
        w, h = case
        for yy in case_y:
            yw, yh = yy
            if(yw > w) : continue
            elif(yh>=h) : break
            elif(yw < w and yh <= h-2 ):
                return [w,h]
            # else:
            #     print('else', case, yy)
        
        
    
    
    return answer
    
    for case in case_li:
        w, h = case
        for yy in case_y:
            yw, yh = yy
            if(yw > w) : continue
            elif(yh>=h) : break
            elif(yw < w and yh <= h-2 ):
                return [w,h]
            # else:
            #     print('else', case, yy)
        
        
    return answer