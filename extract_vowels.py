

string_name = raw_input('Enter the String: ')
vowels = ['a','e','i','o','u']

count = 0

for s in string_name:
    
    if s in vowels:
        
        print s
        
        count = count + 1
   
print '\n The total number of vowels:' + str(count)       


