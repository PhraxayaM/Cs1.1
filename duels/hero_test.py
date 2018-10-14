import pytest
import io
import sys
import superheroes




def capture_console_output(function_body):
    
    string_io = io.StringIO()
    sys.stdout = string_io
    function_body()
    sys.stdout = sys.__stdout__
    return string_io.getvalue()




def test_ability_instance():

    test_strength = superheroes.Ability("Overwhelming Odds", 300)
    assert test_strength


def test_ability_name():

    test_strength = superheroes.Ability("Overwhelming Odds", 300)
    assert test_strength.name == "Overwhelming Odds"


def test_ability_update_attack():
    test_strength = superheroes.Ability("Overwhelming Odds", 300)
    test_strength.update_attack(400)
    test_runs = 100
    attack = 0
    for _ in range(0, test_runs):
        attack += test_strength.attack()
    assert attack <= (400 * test_runs) and attack >= (200 * test_runs)


def test_ability_attack():

    test_runs = 100
    test_strength = superheroes.Ability("Overwhelming Odds", 400)
    for _ in range(0, test_runs):
        attack = test_strength.attack()
        assert attack <= 400 and attack >= 200




def test_weapon_instance():
    the_commander = superheroes.Weapon("Final Duel", 200)
    assert "Weapon" in str(the_commander)


def test_weapon_attack():
    the_commander = superheroes.Weapon("Final Duel", 200)
    test_runs = 100
    for _ in range(0, test_runs):
        attack = the_commander.attack()
        assert attack <= 200 and attack >= 0




def test_hero_instance():
    Kratos = superheroes.Hero("Kratos")
    assert Kratos


def test_hero_add_ability():
    test_strength = superheroes.Ability("Overwhelming Odds", 300)
    Kratos = superheroes.Hero("Kratos")
    assert len(Kratos.abilities) == 0
    Kratos.add_ability(test_strength)
    assert len(Kratos.abilities) == 1
    # Check for correct type
    assert "Ability" in str(Kratos.abilities[0])
    assert Kratos.abilities[0].name == "Overwhelming Odds"


def test_hero_add_multi_ability():
    test_strength = superheroes.Ability("Overwhelming Odds", 300)
    speed = superheroes.Ability("Lightning Speed", 500)
    Kratos = superheroes.Hero("Kratos")
    assert len(Kratos.abilities) == 0
    Kratos.add_ability(test_strength)
    assert len(Kratos.abilities) == 1
    Kratos.add_ability(speed)
    assert len(Kratos.abilities) == 2
    # Check for correct type
    assert "Ability" in str(Kratos.abilities[0])
    assert Kratos.abilities[0].name == "Overwhelming Odds"


def test_hero_attack_ability():
    test_strength = superheroes.Ability("Overwhelming Odds", 30000)
    Kratos = superheroes.Hero("Kratos")
    assert Kratos.attack() == 0
    Kratos.add_ability(test_strength)
    attack = Kratos.attack()
    assert attack <= 30000 and attack >= 15000


def test_hero_attack_weapon():
    test_strength = superheroes.Ability("Overwhelming Odds", 200)
    Kratos = superheroes.Hero("Kratos")
    Kratos.add_ability(test_strength)
    test_runs = 100
    for _ in range(0, test_runs):
        attack = test_strength.attack()
        assert attack <= 200 and attack >= 0


def test_hero_multi_weapon_attack():
    strength = superheroes.Weapon("Overwhelming Odds", 200)
    sword_of_olympus = superheroes.Weapon("Sword of Truth", 700)
    Kratos = superheroes.Hero("Kratos")
    Kratos.add_ability(strength)
    Kratos.add_ability(sword_of_olympus)
    assert len(Kratos.abilities) == 2

    test_runs = 100
    for _ in range(0, test_runs):
        attack = Kratos.attack()
        assert attack <= 900 and attack >= 0


def test_hero_weapon_ability_attack():
    quickness = superheroes.Ability("Quickness", 1300)
    sword_of_olympus = superheroes.Weapon("Sword of Truth", 700)
    Kratos = superheroes.Hero("Kratos")
    Kratos.add_ability(quickness)
    Kratos.add_ability(sword_of_olympus)
    assert len(Kratos.abilities) == 2
    attack_avg(Kratos, 0, 2000)


def attack_avg(object, low, high):
    test_runs = 100
    for _ in range(0, test_runs):
        attack = object.attack()
        assert attack <= high and attack >= low




def test_team_instance():
    team = superheroes.Team("One")
    assert team


def test_team_name():
    team = superheroes.Team("One")
    assert team.name == "One"


def test_team_hero():
    team = superheroes.Team("One")
    ben = superheroes.Hero("ben affleck")
    team.add_hero(ben)
    assert len(team.heroes) == 1
    assert team.heroes[0].name == "ben affleck"


def test_team_remove_hero():
    team = superheroes.Team("One")
    ben = superheroes.Hero("ben affleck")
    team.add_hero(ben)
    assert team.heroes[0].name == "ben affleck"
    team.remove_hero("ben affleck")
    assert len(team.heroes) == 0


def test_team_remove_unlisted():

    team = superheroes.Team("One")
    ben = superheroes.Hero("ben affleck")
    team.add_hero(ben)
    code = team.remove_hero("Kratos")
    assert code == 0


def test_team_remove_empty_list():
    team = superheroes.Team("One")
    assert team.remove_hero("Kratos") == 0


def test_find_hero():
    team = superheroes.Team("One")
    ben = superheroes.Hero("ben affleck")
    team.add_hero(ben)
    hero = team.find_hero("ben affleck")
    assert hero.name == "ben affleck"


def test_find_unlisted_hero():
    team = superheroes.Team("One")
    ben = superheroes.Hero("ben affleck")
    team.add_hero(ben)
    assert team.find_hero("Altrues") == 0


def test_find_empty_hero():
    team = superheroes.Team("One")
    assert team.find_hero("Altrues") == 0


def test_print_heroes():
    team = superheroes.Team("One")
    ben = superheroes.Hero("ben affleck")
    team.add_hero(ben)
    Kratos = superheroes.Hero("Kratos")
    team.add_hero(Kratos)
    output_string = capture_console_output(team.view_all_heroes)

    assert "ben affleck" in output_string
    assert "Kratos" in output_string
