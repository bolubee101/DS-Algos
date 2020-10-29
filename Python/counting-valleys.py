#A valley is a non-empty sequence of consecutive steps below sea level,
#  starting with a step down from sea level and ending with a step up to sea level

def counting_valleys(steps, string_steps):
    mountain = 0
    valley = 0
    for i in range(0, steps):
        if string_steps[i] == 'U':
            mountain += 1
            if mountain == 0:
                valley += 1
        else:
            mountain -= 1
    return valley
if __name__ == '__main__':
    steps = int(input('How many steps did Gary take: '))
    string_steps = input('Enter D for downhill or U for uphill: ')
    answer = counting_valleys(steps, string_steps)
    print('valleys are: ', answer)
