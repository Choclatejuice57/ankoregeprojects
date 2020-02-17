#NOT WINDOWS XP
xp_per_level_bar = 5
xp_per_level_upgrade = 30
level_upgrades_per_vbucksReward = 6
levelsxp_perDay = int(input("Welcome to the XP to V-Bucks Calculator! Enter XP Per Day"))
#Initial XP
xp = 0
for week in range(1, 11):
    xp = levelsxp_perDay * 7 + xp
    print('Week %s = Earned %s XP Till now' % (week, xp))
