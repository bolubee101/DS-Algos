# a mountain is a non-empty sequence of consecutive steps above sea level,
# starting with a step up from sea level and ending with a step down to sea level.
#this script counts how many mountains were encountered based on input in string_steps

def counting_mountains(steps, string_steps):
    mountain = 0
    valley = 0
    for i in range(0, steps):
        if string_steps[i] == 'D':
            valley += 1
            if valley == 0:
                mountain += 1
        else:
            valley -= 1
    return mountain
if __name__ == '__main__':
    steps = int(input('How many steps did Gary take: '))
    string_steps = input('Enter D for downhill or U for uphill: ')
    answer = counting_mountains(steps, string_steps)
    print('mountains are: ', answer)
