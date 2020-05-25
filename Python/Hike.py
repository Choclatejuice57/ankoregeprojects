
tired = False
badweather = False
step = 0
while step < 10001:
    print(step)
    if step == 100:
        tired = True
    if step == 500:
        badweather = True
    if tired == True:
        break
    elif badweather == True:
        break
    else:
        step = step + 1

print("Total # Of Steps =",step)