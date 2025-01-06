hours =  input('Enter Hours :')
rate = input('Enter Rate:')
try:
    r = float(rate)
    h = float(hours)
    GrossPay = h *r
except:
    print("Enter a Numeric input")
       
if(h < 40 ):
    print('Pay:' , GrossPay)
else:
    NewPay = (h-40) *(r*0.5) +GrossPay
    print('Pay:', NewPay)