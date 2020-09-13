def minecraft_inventory(item1):
    print('Select %s' %item1 )

def minecraft_crafting(ct_wood):
    tables = int(ct_wood / 4)
    remaining_wood = ct_wood % 4
    return tables, remaining_wood

minecraft_inventory('Wood')
ca_tables, wood  = minecraft_crafting(7)
print("Crafting Tables",ca_tables)
print("Wood Left Over", wood)