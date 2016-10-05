
import math 

def f(x):#we get the height through this curve function by entering the time duration
    
    return 10*math.e**(math.log(0.5)/5.27 * x)
    

def RadiationExposure(start,stop,step):
    
    count = 0
    
    while start < stop:
        
        area = step * f(start)
        
        count = count + area #through approximation we count the number of area rectangles under the curve and find the total radiation that is exposed
        
        start = start + step

    print count
        
