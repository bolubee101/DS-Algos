def superDigit(num_str):        #num_str = ['5','1','5','1']
    summer = sum(list(map(int, num_str))) # converts all element of num_str to integer and sums them up-summmer = 12
    stringer = list(str(summer)) #stringer becomes ['1','2']
    if len(stringer) == 1:  
        return stringer[0]
    else:
        return superDigit(stringer) #repeats the pattern until stringer holds only one element

detail = input('The integer and the number of repetitions: ').split()  # say input is 51 3, detail=['51','2']
detail[0] = detail[0]* int(detail[1]) #'51' becomes '51' * 2 which  is '5151'
print('Our recursive sum is ', superDigit(list(detail[0]))) #passes a list ['5','1','5','1'] to superDigit and prints