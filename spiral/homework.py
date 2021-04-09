def spiralize(number):
    size = 21
    increment = 0
    diag_one = 1
    diag_two = 1
    diag_three = 1
    diag_four = 1
    old_sum =[]
    for x in range(0,size,2):
        diag_one = diag_one+8*increment
        diag_two = diag_one-6*increment
        diag_three = diag_one-4*increment
        diag_four = diag_one-2*increment
        current_sum = diag_one + diag_two + diag_three + diag_four
        old_sum.append(current_sum)
        increment = increment+1
    return(sum(old_sum)-3)