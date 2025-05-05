
PASS_CREDITS = 0
DEFFERED_CREDITS = 0
TRAILER_CREDITS = 0
total_credits = 0

def main_manu():
    while True:
        print(''' 
            Main Manu
            1. Student Version
            2. Staff Version
            3. Exit      
            ''')
        version = int(input("What Version Do You Want: "))
        if version == 1:
            student()
        elif version == 2:
            staff()
        elif version == 3:
            break
        else:
            while version != 1 or 2:
                main_manu()
        

def student():
    while True:
        OOR = [0,20,40,60,80,100,120]
        input_id = input("Enter ID: ")
        try:
            pass_credits = int(input("Enter the number of credits at pass: "))
            if pass_credits not in OOR:
                print("Out of range\n")
                continue
            defer_credits = int(input("Enter the number of credits at defer: "))
            if defer_credits not in OOR:
                print("Out of range\n")
                continue
            fail_credits = int(input("Enter the number of credits at fail: "))
            if fail_credits not in OOR:
                print("Out of range\n")
                continue
        except ValueError:
            print("Integer required\n")
            continue
        
        

        total_credits = pass_credits + defer_credits + fail_credits

        if total_credits != 120:
            print("Total credits is incorrect. Please try again.\n")
            continue

        progression_outcome = calculate_progression_outcome(pass_credits, defer_credits, fail_credits)
        print("Your progression outcome is:", progression_outcome)
        
        print(" ")
        forward = input('Enter "Q" to exit, or "Y" to continue: ')
        print(" ")
        forward = forward.lower()
        if forward == 'q':
            break
        while forward != 'y':
            print('Please Enter Only "Y" or "Q"')
            print(" ")
            forward = input('Enter "Q" to exit, or "Y" to continue: ')
     
    

def calculate_progression_outcome(pass_credits, defer_credits, fail_credits):
    if fail_credits >= 80:
        return 'Exclude'
    elif pass_credits == 120:
        return 'Progress'
    elif pass_credits == 100:
        return 'Progress (module trailer)'
    elif pass_credits == 80:
        if defer_credits >= 20:
            return 'Do not Progress - module retriever'
        else:
            return 'Progress (module trailer)'
    elif pass_credits == 60:
        return 'Do not Progress - module retriever'
    elif pass_credits == 40:
        return 'Do not Progress - module retriever'
    elif pass_credits == 20:
        return 'Exclude'
    else:
        return 'Do not progress - module retriever'

def generate_histogram(data):
    progress_count = data.count("Progress")
    trailer_count = data.count("Progress (module trailer)")
    retriever_count = data.count("Do not Progress - module retriever")
    exclude_count = data.count("Exclude")
    
    print(" ")
    print("Histogram")
    print(f"Progress  {progress_count}   : ", "*" * progress_count)
    print(f"Trailing {trailer_count}     : ", "*" * trailer_count)
    print(f"Retriever {retriever_count}  : ", "*" * retriever_count)
    print(f"Exclude  {exclude_count}     : ", "*" * exclude_count)

def staff():
    data = []
    input_list = []
    input_dict = {}
    while True:
        OOR = [0,20,40,60,80,100,120]
        input_id = input("Enter ID: ")
        try:
            pass_credits = int(input("Enter the number of credits at pass: "))
            if pass_credits not in OOR:
                print("Out of range\n")
                continue
            defer_credits = int(input("Enter the number of credits at defer: "))
            if defer_credits not in OOR:
                print("Out of range\n")
                continue
            fail_credits = int(input("Enter the number of credits at fail: "))
            if fail_credits not in OOR:
                print("Out of range\n")
                continue
        except ValueError:
            print("Integer required")
            continue
        
        

        total_credits = pass_credits + defer_credits + fail_credits

        if total_credits != 120:
            print("Total credits is incorrect. Please try again.")
            continue

        progression_outcome = calculate_progression_outcome(pass_credits, defer_credits, fail_credits)
        print("Your progression outcome is:", progression_outcome)
        data.append(progression_outcome)
        
        list2 = f"{progression_outcome} - {pass_credits}, {defer_credits}, {fail_credits}"
        input_list.append(list2)
        
        input_dict[input_id] = list2

        print(" ")
        forward = input('Enter "Q" to exit, or "Y" to continue: ')
        print(" ")
        forward = forward.lower()
        if forward == 'q':
            break
        while forward != 'y':
            print('Please Enter Only "Y" or "Q"')
            print(" ")
            forward = input('Enter "Q" to exit, or "Y" to continue: ')

    generate_histogram(data)
    print(" ")
    print(len(data), " outcomes in total.")
    print(" ")
    for item in input_list:
        print(item)
    print(" ")
    for key, value in input_dict.items():
        print(key, ":", value)
    
    #Text file
    with open('input_data.txt', 'w') as f:
        for item in input_list:
            f.write(item + '\n')
    
    print(" ")
    print("End")


main_manu()


