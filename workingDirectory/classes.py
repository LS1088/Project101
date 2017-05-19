weaponDropDict = {}
weaponNameDict = {}
hpPotionDropDict = {}
hpPotionNameDict = {}
itemNameDict = {}
inventory = {}
enemyAppearRateDict = {}
enemyNameDict = {}


'''
CLASSES
'''
class hpPotion():
    def __init__(self, name, hpHeal, dropRate, level):
        self.name = name
        self.hpHeal = hpHeal
        self.dropRate = dropRate
        self.level = level
        hpPotionDropDict[name] = dropRate
        hpPotionNameDict[name] = self
        itemNameDict[name] = self

none = hpPotion('none', 0, 5000, 1)
minorPotion = hpPotion('minor potion', 15, 5000, 1)
lesserPotion = hpPotion('lesser potion', 25, 3500, 2)
smallPotion = hpPotion('small potion', 35, 2750, 4)
potion = hpPotion('potion', 50, 2250, 5)
strongPotion = hpPotion('strong potion', 75, 1625, 7)
largePotion = hpPotion('large potion', 100, 1250, 8)
elixir = hpPotion('elixir', 1000000, 100, 1)

class weapons():
    def __init__(self, name, attack, defence, specialEffect, dropRate, level):
        self.name = name
        self.attack = attack
        self.defence = defence
        self.specialEffect = specialEffect
        self.dropRate = dropRate
        self.level = level
        weaponDropDict[name] = dropRate
        weaponNameDict[name] = self
        itemNameDict[name] = self

none = weapons('none', 0, 0, 'none', 10000, 0)

stick = weapons('stick', 1, 0, 'none', 4000, 1)
wand = weapons('wand', 1, 0, 'magic1', 1800, 3)
oakWand = weapons('oak wand', 1, 0, 'magic2', 400, 6)

rustySword = weapons('rusty sword', 2, 1, 'block', 3000, 2)
ironSword = weapons('iron sword', 5, 1, 'block', 1000, 4)
steelSword = weapons('steel sword', 6, 2, 'block', 400, 6)

rustyDagger = weapons('rusty dagger', 2, 0, 'assassination', 2000, 3)
ironDagger = weapons('iron dagger', 3, 0, 'assassination', 1000, 4)
steelDagger = weapons('steel dagger', 4, 0, 'assassination', 450, 6)

hatchet = weapons('hatchet', 4, 0, 'none', 1800, 3)
ironAxe = weapons('iron axe', 6, 0, 'none', 700, 5)
steelAxe = weapons('steel axe', 8, 0, 'none', 300, 7)

ironGreatsword = weapons('iron greatsword', 6, 2, 'block', 800, 5)
steelGreatsword = weapons('steel greatsword', 8, 3, 'block', 200, 8)

shortBow = weapons('short bow', 3, 0, 'ranged attack', 3000, 2)
huntingBow = weapons('hunting bow', 5, 0, 'ranged attack', 800, 5)
compositeBow = weapons('composite bow', 7, 0, 'ranged attack', 250, 8)
longBow = weapons('long bow', 10, 0, 'ranged attack', 150, 9)
recurveBow = weapons('recurve bow', 13, 0, 'ranged attack', 100, 10)

hammer = weapons('hammer', 6, 0, 'stagger', 1000, 4)
sledgeHammer = weapons('sledge hammer', 10, 0, 'stagger', 350, 7)
giantHammer = weapons('giant hammer', 15, 0, 'stunning attack', 100, 10)

pitchfork = weapons('pitchfork', 1, 1, 'none', 3333, 1)
ironSpear = weapons ('iron spear', 4, 1, 'none', 2000, 3)
staff = weapons('staff', 3, 2, 'magic1', 1600, 4)

class armor ():
    pass

class stats():
    def __init__(self, name, currentHP, maxHP, attack, defence, speed, exp, maxExp, level, weapon, appearRate):
        self.name = name
        self.currentHP = currentHP
        self.maxHP = maxHP
        self.attack = attack
        self.defence = defence
        self.speed = speed
        self.exp = exp
        self.maxExp = maxExp
        self.level = level
        self.weapon = weapon
        if name != 'PLACEHOLDER' and name != 'COMBAT PLACEHOLDER':
            enemyAppearRateDict[name] = appearRate
            enemyNameDict[name] = self

hero = stats('PLACEHOLDER', 100, 100, 10, 0, 1, 0, 100, 1, none, 0)
dummy = stats('COMBAT PLACEHOLDER', 'CURRENT HP', 'MAX HP', 'ATTACK', 'DEFENCE', 'SPEED', 'EXP', 'MAXEXP', 'LEVEL', 'PLACEHOLDERWEAPON', 0)

greenSlime = stats('green slime', 20, 20, 5, 0, 0.66, 33, 2**31-1, 1, 'none', 2000)
bat = stats('bat', 25, 25, 7, 1, 1.19, 40, 2**31-1, 1, 'none', 1000)
yellowSlime = stats('yellow slime', 35, 35, 10, 1, 0.69, 60, 2**31-1, 2, 'none', 1000)
giantCrab = stats('giant crab', 60, 60, 15, 4, 0.49, 120, 2**31-1, 4, 'none', 1000)
wolf = stats('wolf', 50, 50, 12, 1, 1.6, 150, 2**31-1, 5, 'none', 1000)
redSlime = stats('red slime', 80, 80, 22, 2, 0.76, 210, 2**31-1, 6, 'none', 1000)
direWolf = stats('dire wolf', 75, 75, 14, 1, 1.7, 280, 2**31-1, 7, 'none', 1000)
vampire = stats('vampire', 130, 130, 21, 3, 1.3, 350, 2**31-1, 8, 'none', 1000)
greenDragon = stats('green dragon', 110, 100, 30, 6, 0.901, 490, 2**31-1, 9, 'none', 1000)
kingSlime = stats('king slime', 300, 300, 40, 2, 0.81, 800, 2**31-1, 9, 'none', 1000)
redDragon = stats('red dragon', 200, 200, 60, 12, 0.921, 1500, 2**31-1, 10, 'none', 1000)

