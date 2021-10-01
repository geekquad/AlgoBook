# Minimum Bullets required to penetrate the bricks

def MinBullet(points): 
  
    # Sort the points in ascending order 
    for i in range(len(points)): 
        points[i] = points[i][::-1] 
  
    points = sorted(points) 
  
    for i in range(len(points)): 
        points[i] = points[i][::-1] 
  
    # Check if there are no points 
    if (len(points) == 0): 
        return 0
  
    cnt = 1
    curr = points[0][1] 
  
    # Iterate through all the points 
    for j in range(1, len(points)): 
        if (curr < points[j][0]): 
  
            # Increase the count 
            cnt += 1
            curr = points[j][1] 
              
    # Return the count 
    return cnt 
  
# sample brick
if __name__ == '__main__': 
      
    bricks = [ [ 10, 16 ], 
               [ 2, 8 ], 
               [ 1, 6 ],
               [ 7, 12 ]]
  
    # Function call 
    print(MinBullet(bricks)) 