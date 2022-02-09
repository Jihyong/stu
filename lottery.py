import random
file = open("lottery_num.txt","w")
lottery_num = random.sample(range(1,46),6)
lottery_num.sort()
file.write(f'{lottery_num}')
file.close()