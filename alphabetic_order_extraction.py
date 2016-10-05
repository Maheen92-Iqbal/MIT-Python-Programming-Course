
string_name = raw_input('Enter the String: ')

new_string = string_name[0]

longest = string_name[0]

for i in range(0,len(string_name)-1):
    
    if string_name[i] <= string_name[i+1]:
        
        new_string = new_string + string_name[i+1] #we previously add the first element so we can then enter all the elements after that otherwise we
                                                   #miss any character
        if len(new_string) > len(longest):
            
            longest = new_string
            
            #we update the longest string which will remain there 
    else:
        
        #if between the alphabetical order we get any disorder so we refresh the new_string and try to calculate from there on to get the latest
        #longest string
        
        new_string = string_name[i+1] #this would be the value after the value that is stored in the longest string so we can calculate the new
                                      #longest string after that
                                      
print longest