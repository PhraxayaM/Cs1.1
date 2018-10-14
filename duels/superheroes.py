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
