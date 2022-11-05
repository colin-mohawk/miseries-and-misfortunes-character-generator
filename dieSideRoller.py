import random
#this is a fuction that rolls n-sided die(dice) n-rolls and totals the result of the rolls
#example  roll_d(6,2) would most likely result in 6,7,8 but it should be possible to get 2-12 as a result
#by colin 2022
def roll_d(side, rolls):

    roll_result = 0

    for _ in range(rolls):

        roll = random.randint(1, side)

        roll_result = roll_result + roll

    return int(roll_result)