weaponDropDict = {}
weaponNameDict = {}
armorDropDict = {}
armorNameDict = {}
hpPotionDropDict = {}
hpPotionNameDict = {}
itemNameDict = {}
inventory = {}
enemyAppearRateDict = {}
enemyNameDict = {}


'''
CLASSES
'''
class items():
    pass

class hpPotion(items):
    def __init__(self, name, **kwargs):
        self.name = name
        if kwargs:
            for i in kwargs:
                setattr(self, i, kwargs[i])
                if i == "dropRate":
                    hpPotionDropDict[name] = kwargs[i]
        hpPotionNameDict[name] = self
        itemNameDict[name] = self

none = hpPotion('none', hpHeal = 0, dropRate = 5000, level = 1)
minorPotion = hpPotion('minor potion', hpHeal = 15, dropRate = 5000, level = 1)
lesserPotion = hpPotion('lesser potion', hpHeal = 25, dropRate = 3500, level = 2)
smallPotion = hpPotion('small potion', hpHeal = 35, dropRate = 2750, level = 4)
potion = hpPotion('potion', hpHeal = 50, dropRate = 2250, level = 5)
strongPotion = hpPotion('strong potion', hpHeal = 75, dropRate = 1625, level = 7)
largePotion = hpPotion('large potion', hpHeal = 100, dropRate = 1250, level = 8)
elixir = hpPotion('elixir', hpHeal = 1000000, dropRate = 100, level = 1)

class weapons(items):
    def __init__(self, name, **kwargs):
        self.name = name
        if kwargs:
            for i in kwargs:
                setattr(self, i, kwargs[i])
                if i == "dropRate":
                    weaponDropDict[name] = kwargs[i]
        weaponNameDict[name] = self
        itemNameDict[name] = self

none = weapons('none', dropRate = 10000, level = 0)
stick = weapons('stick', attack = 1, dropRate = 4000, level = 1)
wand = weapons('wand', attack = 1, specialEffect = 'magic1', dropRate = 1800, level = 3)
oakWand = weapons('oak wand', attack = 1, specialEffect = 'magic2', dropRate = 400, level = 6)
rustySword = weapons('rusty sword', attack = 2, defence = 1, dropRate = 3000, level = 2)
ironSword = weapons('iron sword', attack = 5, defence = 1, specialEffect = 'block', dropRate = 1000, level = 4)
steelSword = weapons('steel sword', attack = 6, defence = 2, specialEffect = 'block', dropRate = 400, level = 6)
rustyDagger = weapons('rusty dagger', attack = 2, dropRate = 2000, level = 3)
ironDagger = weapons('iron dagger', attack = 3, specialEffect = 'assassination', dropRate = 1000, level = 4)
steelDagger = weapons('steel dagger', attack = 4, specialEffect = 'assassination', dropRate = 450, level = 6)
hatchet = weapons('hatchet', attack = 4, dropRate = 1800, level = 3)
ironAxe = weapons('iron axe', attack = 6, dropRate = 700, level = 5)
steelAxe = weapons('steel axe', attack = 8, dropRate = 300, level = 7)
ironGreatsword = weapons('iron greatsword', attack = 6, defence = 2, specialEffect = 'block', dropRate = 800, level = 5)
steelGreatsword = weapons('steel greatsword', attack = 8, defence = 3, specialEffect = 'block', dropRate = 200, level = 8)
shortBow = weapons('short bow', attack = 3, specialEffect = 'ranged attack', dropRate = 3000, level = 2)
huntingBow = weapons('hunting bow', attack = 5, specialEffect = 'ranged attack', dropRate = 800, level = 5)
compositeBow = weapons('composite bow', attack = 7, specialEffect = 'ranged attack', dropRate = 250, level = 8)
longBow = weapons('long bow', attack = 10, specialEffect = 'ranged attack', dropRate = 150, level = 9)
recurveBow = weapons('recurve bow', attack = 13, specialEffect = 'ranged attack', dropRate = 100, level = 10)
hammer = weapons('hammer', attack = 6, dropRate = 1000, level = 4)
sledgeHammer = weapons('sledge hammer', attack = 10, specialEffect = 'stagger', dropRate = 350, level = 7)
giantHammer = weapons('giant hammer', attack = 15, specialEffect = 'stunning attack', dropRate = 100, level = 10)
pitchfork = weapons('pitchfork', attack = 1, defence = 1, dropRate = 3333, level = 1)
ironSpear = weapons ('iron spear', attack = 4, defence = 1, dropRate = 2000, level = 3)
staff = weapons('staff', attack = 3, defence = 2, specialEffect = 'magic1', dropRate = 1600, level = 4)

class armor(items):
    def __init__(self, name, **kwargs):
        self.name = name
        if kwargs:
            for i in kwargs:
                setattr(self, i, kwargs[i])
                if i == "dropRate":
                    armorDropDict[name] = kwargs[i]
        armorNameDict[name] = self
        itemNameDict[name] = self
        
none = armor('none', dropRate = 10000, level = 0)
rags = armor('rags', defence = 0, level = 1)

class stats():
    def __init__(self, name, **kwargs):
        self.name = name
        if kwargs:
            for i in kwargs:
                setattr(self, i, kwargs[i])
                if i == "maxHP":
                    self.currentHP = kwargs[i]
                if i == "appearRate":
                    enemyAppearRateDict[name] = kwargs[i]
                    enemyNameDict[name] = self                    
                
hero = stats('PLACEHOLDER', maxHP = 100, attack = 10, defence = 0, speed = 1, exp = 0, maxExp = 100, level = 1, weapon = none, armor = none)
dummy = stats('COMBAT PLACEHOLDER')

greenSlime = stats('green slime', maxHP = 20, attack = 5, defence = 0, speed = 0.66, exp = 33, level = 1, appearRate = 2000)
bat = stats('bat', maxHP = 25, attack = 7, defence = 1, speed = 1.19, exp = 40, level = 1, appearRate = 1000)
yellowSlime = stats('yellow slime', maxHP = 35, attack = 10, defence = 1, speed = 0.69, exp = 60, level = 2, appearRate = 1000)
giantCrab = stats('giant crab', maxHP = 60, attack = 15, defence = 4, speed = 0.49, exp = 120, level = 4, appearRate = 1000)
wolf = stats('wolf', maxHP = 50, attack = 12, defence = 1, speed = 1.6, exp = 150, level = 5, appearRate = 1000)
redSlime = stats('red slime', maxHP = 80, attack = 22, defence = 2, speed = 0.76, exp = 210, level = 6, appearRate = 1000)
direWolf = stats('dire wolf', maxHP = 75, attack = 14, defence = 1, speed = 1.7, exp = 280, level = 7, appearRate = 1000)
vampire = stats('vampire', maxHP = 130, attack = 21, defence = 3, speed = 1.3, exp = 350, level = 8, appearRate = 1000)
greenDragon = stats('green dragon', maxHP = 100, attack = 30, defence = 6, speed = 0.901, exp = 490, level = 9, appearRate = 1000)
kingSlime = stats('king slime', maxHP = 300, attack = 40, defence = 2, speed = 0.81, exp = 800, level = 9, appearRate = 1000)
redDragon = stats('red dragon', maxHP = 200, attack = 60, defence = 12, speed = 0.921, exp = 1500, level = 10, appearRate = 1000)

