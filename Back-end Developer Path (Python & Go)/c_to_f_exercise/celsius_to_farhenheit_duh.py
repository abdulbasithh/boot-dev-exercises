def cel_to_farh(c):
    c_to_f_calc = round(c * 1.8 + 32) # i previously type casted this, now i added round here itself! :]
    print(c, "c is " , c_to_f_calc , "farenheit") # removed repeated use of rounding, fulfiled in above variable
    return c_to_f_calc
    


cel_to_farh(25) # change 25 to anything you like!, later on u can add input to get any value
