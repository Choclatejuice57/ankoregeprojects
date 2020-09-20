def monthly(pocket_money, rewards, commission, spending):
    return pocket_money + rewards + commission - spending


print(monthly(10, 15, 30, 20))
