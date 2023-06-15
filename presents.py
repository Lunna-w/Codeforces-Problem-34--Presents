n = int(input())
numbers = list(map(int, input().split()))

new_numbers = [0] * n

for i in range(n):
    pos = numbers[i] - 1  
    new_numbers[pos] = i + 1

for num in new_numbers:
    print(num, end=' ')
        
        
            
  
                
   
        


    
