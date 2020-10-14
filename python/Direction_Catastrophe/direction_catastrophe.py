opposite = {'north': 'south', 'east': 'west', 'south': 'north', 'west': 'east'} 

# Function to find the reduced direction 

def reduced_direction(givenDirections): 
	finalDirections = [] 
	
	for d in range(0, len(givenDirections)): 
		
		if finalDirections: 
		
			if finalDirections[-1] == opposite[givenDirections[d]]: 
				finalDirections.pop() 
			else: 
				finalDirections.append(givenDirections[d]) 
				
		else: 
			finalDirections.append(givenDirections[d]) 
			
	return finalDirections 

# creating an empty list for storing directions
directions = [] 
  
# number of directions as an input 
n = int(input("Enter number of directions : ")) 
  
# taking directions as input 
for i in range(0, n): 
    dir = input() 
    directions.append(dir) # adding the directions 
      
print(reduced_direction(directions)) 
