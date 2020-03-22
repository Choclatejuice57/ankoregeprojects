#NOT WINDOWS XP
xp_per_level_bar = 5
xp_per_level_upgrade = 30
level_upgrades_per_vbucksReward = 6
levelsxp_perDay = int(input("Welcome to the XP to V-Bucks Calculator! Enter XP Per Day"))
#Initial XP
xp = 0
for week in range(1, 55):
    # The part where your XP is multiplied by 7, then is added to your xp and printed.
    xp = levelsxp_perDay * 7 + xp
    print('Week %s You Earned %s XP Till now' % (week, xp))
    level_upgrades = int(xp / xp_per_level_upgrade)
    print("   %s Level Upgrades" % (level_upgrades))
    vBuck_reward = int(level_upgrades / level_upgrades_per_vbucksReward)
    print('   %s Current V-Bucks Rewards' % (vBuck_reward))
    vbucks = int(vBuck_reward * 100)
    print("  %s Current V-Bucks" % (vbucks))
