# python program to count number of 
# steps to reach a point 
import sys 
  
# Function to count number of steps 
# required to reach a destination 
      
# source -> source vertex 
# step -> value of last step taken 
# dest -> destination vertex 
def steps(source, step, dest): 
      
    #base cases 
    if (abs(source) > (dest)) : 
        return sys.maxsize  
      
    if (source == dest): 
        return step 
  
    # at each point we can go  
    # either way 
  
    # if we go on positive side 
    pos = steps(source + step + 1, 
                    step + 1, dest) 
  
    # if we go on negative side 
    neg = steps(source - step - 1,  
                    step + 1, dest) 
  
    # minimum of both cases 
    return min(pos, neg) 
