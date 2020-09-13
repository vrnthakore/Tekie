n = int(input('Enter a number : ')) 

for i in range(2, n): 
    if n%i == 0 :
        print('Number is not a Prime')
        break

if i == n-1 :
    print('Number is a Prime')
    
  