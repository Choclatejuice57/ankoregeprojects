def monthly(pocket_money, rewards, commission, spending):
    return pocket_money + rewards + commission - spending

def yearly(monthly):
    return monthly * 12

print(yearly(10, 15, 30, 20))