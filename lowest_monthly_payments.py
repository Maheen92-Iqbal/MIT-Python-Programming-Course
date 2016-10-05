
balance = 5000.00 

annual_interest_rate = 0.18

minimum_monthly_payment = 0

unpaid_balance = balance

while unpaid_balance > 0:
    
    minimum_monthly_payment += 10  #This happens everytime we go through a 12 month cycle and the unpaid is not zero so add 10 more to the monthly pay.
                                  #and also updated the balance
    unpaid_balance = balance

    month = 0
    
    while month < 12:
                  
        unpaid_balance = unpaid_balance - minimum_monthly_payment 
    
        interest =  ( annual_interest_rate/12.0 ) * unpaid_balance

        unpaid_balance = unpaid_balance + interest
    
        month = month + 1
    
print 'The lowest Monthly payment: ' + str(round(minimum_monthly_payment,2)) 
    
        


