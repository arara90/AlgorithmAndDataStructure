def binarySearch(li, key):
    left = 0
    right = len(li) - 1

    while( right > left):
        mid = int ( (right + left) /2 )
        if key == li[mid] :
            print( f'{key} is in the list with index value: {mid}')
            break;
        if key < li[mid]:
            right = mid - 1
        else:
            left = mid + 1


list = [1,2,3,4,5,6,7,8,9]
binarySearch(list, int(input('찾을 값: ' )))

