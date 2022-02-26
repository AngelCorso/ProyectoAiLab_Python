class Character:
    def __init__(self,name,HP,type,isPowerUpActive,imagePath,attacks,powerUpName,advantage,disadvantage,normal):
        self.name = name
        self.HP = HP
        self.type = type
        self.attacks = attacks
        self.powerUpName = powerUpName
        self.isPowerUpActive = isPowerUpActive
        self.imagePath=imagePath
        self.advantage = advantage
        self.disadvantage = disadvantage
        self.normal = normal
        self.isPowerUpAvailable = True
        self.powerUpTurnsCounter = 5
        self.isPlayer = False

    def attack(self,enemyType,attackName):
        # Si el ataque es el primero
        attackNames = list(self.attacks)

        if attackName == attackNames[0]:
            return self.checkDamageByEnemyType(enemyType) + (2 if self.isPowerUpActive else 0)
        else:
        # Si no, solo se hace el daño
            return self.attacks[attackName]

    def receiveDamage(self,damage):
        self.HP -= damage

    def checkDamageByEnemyType(self,enemyType):
        #ventaja
        attackName = list(self.attacks)[0]
        attackDamage = self.attacks[attackName]
        if self.hasAdvantage(enemyType):
            return attackDamage[1]
        #desventaja
        elif self.hasDisadvantage(enemyType):
            return attackDamage[2]
        #normal
        else:
            return attackDamage[0]

    def hasAdvantage(self,enemyType):
        if enemyType in self.advantage:
            return True
        return False

    def hasDisadvantage(self,enemyType):
        if enemyType in self.disadvantage:
            return True
        return False


    def activatePowerUp(self):
        self.powerUpTurnsCounter = 4
        self.isPowerUpActive = True
        self.isPowerUpAvailable = False
    
    def updatePowerUp(self):
        if self.powerUpTurnsCounter > -1 and self.powerUpTurnsCounter < 5:
            self.powerUpTurnsCounter -= 1

        if self.powerUpTurnsCounter == 1:
            self.isPowerUpActive = False

        elif self.powerUpTurnsCounter == 0:
            self.isPowerUpAvailable = True
                
def initCharacters():
    characters = [
    Character("Aquarder",25,"Agua",False,"images/aquarder.png",{"Aqua-jet":[3,5,2,5,7,4],"Cola férrea":2,"Cabezazo":2},"Lluvia",["Roca","Fuego"],["Eléctrico","Planta"],["Agua","Escarabajo"]),
    Character("Electder",25,"Eléctrico",False,"images/electder.png",{"Trueno":[3,5,2,5,7,4],"Arañazo":3,"Mordisco":3},"Campo magnético",["Agua","Escarabajo"],["Roca","Planta"],["Eléctrico","Fuego"]),
    Character("Firesor",25,"Fuego",False,"images/firesor.png",{"Llamarada":[3,5,2,5,7,4],"Embestida":2,"Mordisco":2},"Día soleado",["Planta","Escarabajo"],["Agua","Roca"],["Eléctrico","Fuego"]),
    Character("Mousebug",25,"Escarabajo",False,"images/mousebug.png",{"Picotazo":[3,5,2,5,7,4],"Embestida":2,"Cabezazo":2},"Esporas",["Planta","Roca"],["Fuego","Eléctrico"],["Escarabajo","Agua"]),
    Character("Splant",25,"Planta",False,"images/splant.png",{"Hoja navaja":[3,5,2,5,7,4],"Mordisco":2,"Cabezazo":2},"Rayo solar",["Roca","Agua","Eléctrico"],["Fuego","Escarabajo"],["Planta"]),
    Character("Rockdog",25,"Roca",False,"images/rockdog.png",{"Roca afilado":[3,5,2,5,7,4],"Velocidad":2,"Cola ferrea":2},"Campo rocoso",["Fuego","Eléctrico"],["Agua","Planta"],["Roca","Escarabajo"])
    ]
    return characters