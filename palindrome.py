# -*- coding: utf-8 -*-

def is_palindrome(test_string):
        return test_string == test_string[::-1]

def check_all_bases(dec_input):
    
    dec_string = str(dec_input)
    
    hex_string = f"{dec_input:x}"
    
    bin_string = f"{dec_input:b}"
    
    result_bin = is_palindrome(bin_string)
    
    result_dec = is_palindrome(dec_string)
            
    result_hex = is_palindrome(hex_string)
        
    if result_dec and result_bin and result_hex == True:
        
        return("Match Found! ","dec:", dec_string,"bin:", bin_string,"hex:", hex_string)
    
    else:
    
        return False

# last checked to 343563319060913365343

dec_start = 34356331907

while True:
    
    dec_input = int(str(dec_start)[:-1] + str(dec_start)[::-1])
        
    dec_input_alt = int(str(dec_start) + str(dec_start)[::-1])
    
    answer = check_all_bases(dec_input)
    
    answer_alt = check_all_bases(dec_input_alt)
    
    if answer != False:
    
        print(dec_input, int(dec_start), answer)
    
    if answer_alt != False:
    
        print(dec_input_alt, int(dec_start), answer_alt)

    dec_start += 1 