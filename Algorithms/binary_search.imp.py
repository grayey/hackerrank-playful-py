
test_array = [10,11,12,13, 17,56, 89, 31,892,7]


def binary_search(array, needle, acc=0, index_action= 0, is_sorted=False):
    new_array = sorted(array) if not is_sorted else array
    low = 0
    high = len(new_array)
    mid_point = low + (high - low) /2
    mid = round(mid_point) + index_action
    acc = acc + mid

    left = new_array[:mid]
    right = new_array[mid:]
    middle = new_array[mid]

    if middle == needle:
        return acc
       
    
    elif middle > needle:
       print("Searching left ", left)
       return binary_search(left, needle, acc=mid, index_action=-1, is_sorted=True)

    else:
        # print('Middle is less than needle'+str(middle))
      print("Searching right ", right)
      return  binary_search(right, needle, acc=mid,  index_action=1, is_sorted=True) 


    # print("Search Index: "+str(search_index))
    # for idx, value in enumerate(new_array):
    #     pass
    
  

    # print(new_array)




print(binary_search(test_array, 892))