

def buildSubArrays(arr, start=0, end=0, new_list=[]):
        acc = new_list[:]  # COPY O! Memory was leaking O!..  Lesson learned: When using an accumulator for recursive functions always create a new copy of th accumulator
    
        if end == len(arr): # Return the accumulator if we have reached the end of the array 
            return acc;
        
        elif start > end: # Increment the end point and start from 0 
            end +=1;
            return buildSubArrays(arr, 0, end, acc);
        else:
            acc.append(arr[start:end+1])
            start += 1;
            return buildSubArrays(arr, start, end, acc);


# Complete the sansaXor function below.
def sansaXor(arr):
    subArraysMatrix = buildSubArrays(arr);
    outerXorOutput = 0;

    for outerXorItem in subArraysMatrix:
        for  innerXorItem in outerXorItem:
            outerXorOutput ^= innerXorItem;
    
    return outerXorOutput;



def buildXorCustom(arr, start=0, end=0, xorOutput=0):
    
        if end == len(arr): # Return the accumulator if we have reached the end of the array 
            return xorOutput;
        
        elif start > end: # Increment the end point and start from 0 
            end +=1;
            return buildSubArrays(arr, 0, end, xorOutput);
        else:
            subArr = arr[start:end+1];
            for a_x in subArr:
                xorOutput ^= a_x;
            start += 1;
            return buildSubArrays(arr, start, end, xorOutput);








sansaXor([50,13,5])