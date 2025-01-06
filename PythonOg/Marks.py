
while True:
        marks = input('Enter Score:')
        
        try:
            marks = float(marks)
            if marks< 0 or marks>1 :
                 print("Bad Score , Please enter value between 0 to 1")
                 continue
        except:
             print('Bad Score')
             continue
    
        if( marks < 0.6):
            print('F')
        elif(marks >= 0.9):
            print('A')
        elif(marks >= 0.8):
            print('B')
        elif(marks>= 0.7):
            print('C')
        elif(marks>= 0.6):
            print('D')
        break