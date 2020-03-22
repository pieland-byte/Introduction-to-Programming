# This program deermines if a client is eligible for a loan when given
# parameters to take into account




while True:
    credit_score = input("Enter credit score (0-10 inclusive) or Q to quit: ")
    if credit_score == "Q" or credit_score == "q":
        print("Goodbye")
        exit()
    credit_score = int(credit_score)
    if credit_score > 10 or credit_score < 0:
        print("Invalid credit score entered")
    elif credit_score == 0 :
        print("Loan request denied")
    
        
    elif credit_score == 1 :
        address_term = float(input("Enter amount of months at current address: "))
        if address_term < 12:
            print("Loan request denied")
        elif address_term >= 12:
            income = int(input("Client income(£s): "))
            request = int(input("Loan amount requested (£s): "))

            if request <= (income * 0.2):
                print("Loan request granted")
            else:
                print("Loan request denied")
                
    elif credit_score <= 5:
        address_term = float(input("Enter amount of months at current address: "))
        if address_term < 60:
            print("Loan request denied")
        elif address_term >= 60:
            income = int(input("Client income(£s): "))
            request = int(input("Loan amount requested (£s): "))
            if request < income:
                print("Loan request granted")
            elif request < (income * 2) and credit_score == 5:
                print("Loan request granted")
            else:
                print("Loan request denied")

    elif credit_score == 6:
        address_term = float(input("Enter amount of months at current address: "))
        if address_term < 60:
            print("Loan request denied")
        elif address_term >= 60:
            income = int(input("Client income(£s): "))
            request = int(input("Loan amount requested (£s): "))
            if request < (income * 2):
                print("Loan request granted")
            else:
                print("Loan request denied")
        
            
    elif credit_score >= 7:
        address_term = float(input("Enter amount of months at current address: "))
        if address_term < 12:
            print("Loan request denied")
        elif 12 <= address_term:
            income = int(input("Client income(£s): "))
            request = int(input("Loan amount requested (£s): "))
            if request < income:
                print("Loan request granted")
            elif address_term >= 60 and request < (income * 2):
                print("Loan request granted")
        else:
            print("Loan request denied")
    
