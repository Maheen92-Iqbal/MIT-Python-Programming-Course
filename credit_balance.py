
balance = 5000.00 

annual_interest_rate = 0.18

payment = 0.02

month = 0

while True:
  
    minimum_monthly_payment = balance * payment

    unpaid_balance = balance - minimum_monthly_payment 

    interest =  ( annual_interest_rate/12.0 ) * unpaid_balance

    updated_balance = unpaid_balance + interest
    
    balance = updated_balance 
    
    month = month + 1
    
    if month == 12:
        
        break
        
print 'The Remaining Balance: ' + str(round(updated_balance,2))
    
        


