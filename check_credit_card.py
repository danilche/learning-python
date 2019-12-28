#program that checks whether CC is a valid MC, AMEX or VISA number

def break_digits_apply_luhns(my_str):
    first_list = [int(my_str[j]) for j in range(0, len(my_str), 2)]
    second_list = [int(my_str[j]) for j in range(1, len(my_str), 2)]
    for j in range(len(second_list)):
        second_list[j] = 2 * second_list[j]              
    for j in range(len(second_list)):
        if second_list[j] >= 10:
            second_list[j] = second_list[j] - 9
    return sum(first_list) + sum(second_list)       
            
def main():
    ccn = input("Enter CC number: ")
    str_ccn = str(ccn)[::-1]
    dig2 = str_ccn[-1] + str_ccn[-2]
    ####check if two digits sums modulo 10 equals zero####
    if break_digits_apply_luhns(str_ccn) % 10 != 0:
        print("INVALID")
    else:   
    ##########checking if CC is AMEX#######################   
        if dig2 in ['34', '37'] and len(str_ccn) == 15:
            print("AMEX")
    ############checking if CC is MASTERCARD###############   
        elif 51 <= int(dig2) <= 55 and len(str_ccn) == 16:
            print("MASTERCARD")
    #################checking if CC is VISA################
        elif str_ccn[-1] == '4' and len(str_ccn) in [13, 16]:
            print("VISA")
        else:
            print("INVALID")    
main()
 
