
string_name = raw_input('Enter the String: ')

name = 'bob'

start = 0
count = 0

while True:
    
    answer = string_name.find(name,start)
    
    if answer == -1:
        
        break
        
    count = count + 1
    start = answer + 1
          
print 'The number of Bob Counts are: ' + str(count)