import random
#
# kill = Ability("kill_somdbody", 50)
# kill.update_attack(25)

class Hero:
    def __init__(self, name):
        self.abilities = list()
        self.name = name


    def add_ability(self, ability):
        abilities_list = self.abilities
        abilities_list.append(ability)

    def attack(self):
        total_attack = 0
        if not self.abilities:
            print("No abilities")
        else:
            for ability in self.abilities:
                attack_damage = ability.attack()
                total_attack += attack_damage
        return total_attack

class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        min_attack_strength = self.attack_strength // 2
        attack_value = random.randint(min_attack_strength, self.attack_strength)
        return attack_value

    def update_attack(self, attack_strength):
        self.attack_strength = attack_strength

class Weapon(Ability):
    def attack(self):
        weapon_attack = random.randint(0, self.attack_strength)
        return weapon_attack

class Armor:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense

    def defend(self):
        return random.randint(0, self.defense)

class Team:
    def __init__(self, team_name):
        self.name = team_name
        self.heroes = list()

    def add_hero(self, hero):
        if hero not in self.heroes:
            self.heroes.append(hero)
            #print("{} added to {}".format(hero.name, self.name))
        #else:
            #print("{} is already in {}".format(hero.name, self.name))

    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                return 1
                #print("{} removed from {}".format(hero.name, self.name))
            #else:
                #print("{} is not in {}".format(hero.name, self.name))
        return 0

    def find_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                #print("{} found in {}".format(hero.name, self.name))
                return hero
            #else:
                #print("{} is not in {}".format(hero.name, self.name))
        return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def attack(self, other_team):
        totalAttack = 0
        for hero in self.heroes:
            totalAttack += hero.attack()
        enemiesDead = other_team.defend(totalAttack)

        for hero in self.heroes:
            hero.add_kill(enemiesDead)

        return totalAttack


    def defend(self, damage_amt):
        deadHeroes = 0
        totalDefense = 0
        for hero in self.heroes:
            totalDefense += hero.defend()
        if damage_amt > totalDefense:
            self.deal_damage(totalDefense - damage_amt)
        for hero in self.heroes:
            if hero.deaths > 0:
                deadHeroes += 1
        return deadHeroes

    def deal_damage(self, damage):
        deadHeroes = 0
        damage = damage // len(self.heroes)
        for hero in self.heroes:
            hero.take_damage(damage)
            deadHeroes += hero.deaths
        return deadHeroes

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.health = hero.start_health

    def stats(self):
        stats_array = []
        for hero in self.heroes:
            if hero.deaths != 0:
                ratio = hero.kills // hero.deaths
                stats_array.append((str(hero.name) + " has " + str(hero.health) + " health, killed " + str(hero.kills) + " hero(es) and died " + str(hero.deaths) + " time(s). THEIR KILLS TO DEATHS RATIO WAS " + str(ratio) + "."))
            else:
                stats_array.append((str(hero.name) + " has " + str(hero.health) + " health, killed " + str(hero.kills) + " hero(es) and never died."))
        return stats_array

    def update_kills(self):
        totalTeamKills = 0
        for hero in self.heroes:
            totalTeamKills += hero.kills
        return totalTeamKills

    def deadHeroes(self):
        deadHeroes = 0
        for hero in self.heroes:
            deadHeroes += hero.deaths
        if deadHeroes >= len(self.heroes):
            return True
        else:
            return False

class Arena:
    """Four methods:
    build_team_one: build team one
    build_team_two: build team two
    team_battle: play match if either team has at least one member still alive
    show_stats: make an array of two items: team_one, team_two, then call the Team() class method stats()
    end_Docstringtest!"""
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def build_team_one(self):
        hero1 = ""
        ability1 = ""
        heroDict = {}
        heroCounter = 0
        powerCounter = 0
        yes = ["yeah", "y", "yes", "ye"]
        print("\nIt's judgement day. Meet your DOOM\n")
        teamName1 = input("Who is your first team?\n\n")
        self.team_one = Team(teamName1)
        print("\nThank you. \n")
        while len(self.team_one.heroes) < 2:
                heroDict[heroCounter] = Hero(input("Please enter the name of a superhero on " + str(self.team_one.name) + ". \n \n"))
                self.team_one.add_hero(heroDict[heroCounter])
                print("\n\nYour team: ")
                print(self.team_one.view_all_heroes())
                print("\nEach hero can have 3 powers. \nThe strength of each power is randomly created \nbetween weak (strength: <10) and strong (stength: 100+).\n")
                powerCounter = 0
                while powerCounter < 2:
                    if ability1 == "x":
                        ability1 = ""
                        heroCounter += 1
                    else:
                        ability1 = input("\nWhat's " + heroDict[heroCounter].name + "'s superpower # " + str(powerCounter + 1) + " called? \n\n")
                        abilityability = Ability(ability1, (powerCounter + 1) * random.randint(1,60))
                        heroDict[heroCounter].add_ability(abilityability)
                        print("")
                        powerCounter += 1
                print("Is your hero equipped with a weapon?")
                answer = str.lower(input("Enter yes or no.\n\n"))
                if answer in yes:
                    weapon = input("\n\nWhat's your weapon?\n\n")
                    weapon1 = Weapon(str(weapon), random.randint(1,100))
                    heroDict[heroCounter].add_ability(weapon1)
                else:
                    print("\n\nYour hero has no weapon.\n\n")
                print("\n\nDoes your hero have armor equipped?")
                answer = str.lower(input("Enter yes or no.\n\n"))
                if answer in yes:
                    armor = input("\n\nWhat's the armor that your hero has equipped?\n\n")
                    armor1 = Weapon(str(armor), random.randint(1,50))
                    heroDict[heroCounter].add_armor(armor1)
                else:
                    print("Your hero has no armor.")
                print("Your abilities are: \n\n")
                print(heroDict[heroCounter].listAbilities())
                if len(heroDict[heroCounter].armors) > 0:
                    print("Your armor is: \n\n")
                    print(armor)

    def build_team_two(self):
        hero1 = ""
        ability1 = ""
        heroDict = {}
        heroCounter = 0
        powerCounter = 0
        yes = ["yeah", "y", "yes", "ye"]
        print("\nHello, welcome to hell.\n")
        teamName2 = input("What is your SECOND TEAM of super hero's NAME?\n\n")
        self.team_two = Team(teamName2)
        print("\nVery cool. \n")
        while len(self.team_two.heroes) < 2:
                heroDict[heroCounter] = Hero(input("Please enter the name of a superhero on " + str(self.team_two.name) + ". \n \n"))
                self.team_two.add_hero(heroDict[heroCounter])
                print("\n\nYour team: ")
                print(self.team_two.view_all_heroes())
                print("\nEach hero can have three powers. \nThe strength of each power is randomly generated \nbetween weak (strength: <10) and strong (stength: 100+).\n")
                powerCounter = 0
                while powerCounter < 2:
                    if ability1 == "x":
                        ability1 = ""
                        heroCounter += 1
                    else:
                        ability1 = input("\nWhat's " + heroDict[heroCounter].name + "'s superpower # " + str(powerCounter + 1) + " called? \n\n")
                        abilityability = Ability(ability1, (powerCounter + 1) * random.randint(1,60))
                        heroDict[heroCounter].add_ability(abilityability)
                        print("")
                        powerCounter += 1
                print("Does your hero have a weapon?")
                answer = str.lower(input("Enter yes or no.\n\n"))
                if answer in yes:
                    weapon = input("\n\nWhat's your weapon?\n\n")
                    weapon1 = Weapon(str(weapon), random.randint(1,100))
                    heroDict[heroCounter].add_ability(weapon1)
                else:
                    print("\n\nYour hero has no weapon.\n\n")
                print("\n\nDoes your hero wear armor.")
                answer = str.lower(input("Enter yes or no.\n\n"))
                if answer in yes:
                    armor = input("\n\nWhat's the armor your hero is wearing?\n\n")
                    armor1 = Weapon(str(armor), random.randint(1,50))
                    heroDict[heroCounter].add_armor(armor1)
                else:
                    print("Your hero has no armor.")
                print("Your abilities are: \n\n")
                print(heroDict[heroCounter].listAbilities())
                if len(heroDict[heroCounter].armors) > 0:
                    print("Your armor is: \n")
                    print(armor)
                    print(" ")

    def team_battle(self):
        gameover1 = False
        gameover2 = False
        self.build_team_one()
        self.build_team_two()
        print("Your teams are: ")
        print(self.team_one.view_all_heroes_stats())
        print(self.team_two.view_all_heroes_stats())
        x = random.randint(0,1)
        print("\nWho strikes first??")
        if x == True:
            print("\nTeam one got the drop on team two!!! Careful team two!")
            while gameover1 != True and gameover2 != True:
                self.team_one.attack(self.team_two)
                gameover1 = self.team_two.deadHeroes()
                gameover2 = self.team_one.deadHeroes()
                self.team_two.attack(self.team_one)
                gameover1 = self.team_two.deadHeroes()
                gameover2 = self.team_one.deadHeroes()
        else:
            print("Team two got the drop on team one!!! Careful team one!")
            while gameover1 != True and gameover2 != True:
                self.team_two.attack(self.team_one)
                gameover1 = self.team_one.deadHeroes()
                gameover2 = self.team_two.deadHeroes()
                self.team_one.attack(self.team_two)
                gameover1 = self.team_one.deadHeroes()
                gameover2 = self.team_two.deadHeroes()

    def show_stats(self):
        print("\n\nTEAM ONE STATS:")
        print(self.team_one.stats())
        print("\nTEAM TWO STATS:")
        print(self.team_two.stats())

myArena = Arena()
myArena.team_battle()
myArena.show_stats()




# my_hero = Hero("Matt")
# my_ability = Ability("Kamehameha", 10)
# my_hero.add_ability(my_ability)
# print(my_hero.attack())
if __name__ == "__main__":
    hero = Hero("The Flash")
#     hero2 = Hero("Batman")
#     hero3 = Hero("Thor")
    team = Team("HeroVerse")
    team.add_hero(hero)
    print(len(team.heroes))
#     team.add_hero(hero2)
#     team.add_hero(hero3)
#     # team.find_hero(hero)
    team.remove_hero("The Flash")
    print(len(team.heroes))
#     team.find_hero(hero)
#     team.view_all_heroes()
#     print(hero.attack())
#     ability = Ability("Flash punch", 150)
#     #ability2 = Weapon("Sucker Punch", 100)
#     #print("weapon damage: {}".format(ability2.attack()) )
#     hero.add_ability(ability)
#     print(hero.attack())
#     new_ability = Ability("Crazy attack", 600)
#     hero.add_ability(new_ability)
#     print(hero.attack())
