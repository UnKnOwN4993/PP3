from time import *
from random import *
global move1, move2, move3, move4
stat_move = 'stat move'
normal_move = 'normal move'
move_type = move_type_p1 = move_type_p2 = normal_move
hp = p1_hp, p2_hp = 100, 100
oppo_hp = 100
strength = strength_p1, strength_p2 = 1, 1
crit_chance, crit_chance_p1, crit_chance_p2 = 10, 10, 10
crit_damage_p1, crit_damage_p2 = 3, 3
double_hit, double_hit_p1, double_hit_p2 = 20, 20, 20
burning_time, burning_time_p1, burning_time_p2 = 0, 0, 0
burning_damage = 2
damage = damage_p1, damage_p2 = 0, 0
defense = defense_p1, defense_p2 = 1, 1
characters = character_p1, character_p2 = '', ''
p1_move1, p1_move2, p1_move3, p1_move4 = '', '', '', ''
p2_move1, p2_move2, p2_move3, p2_move4 = '', '', '', ''
oppo_turn = 1


def set_turns():
    global characters, character_p1, character_p2
    global damage, damage_p1, damage_p2
    global hp, p1_hp, p2_hp
    global burning_time, burning_time_p1, burning_time_p2
    global double_hit, double_hit_p1, double_hit_p2
    global crit_chance, crit_chance_p1, crit_chance_p2
    global strength, strength_p1, strength_p2
    global defense, defense_p1, defense_p2
    global move_type, move_type_p1, move_type_p2
    global oppo_hp

    if turn == 1:
        characters = character_p1
        damage = damage_p1
        hp = p1_hp
        oppo_hp = p2_hp
        burning_time = burning_time_p1
        double_hit = double_hit_p1
        crit_chance = crit_chance_p1
        strength = strength_p1
        defense = defense_p1
        move_type = move_type_p1

    if turn == 2:
        characters = character_p2
        damage = damage_p2
        hp = p2_hp
        oppo_hp = p1_hp
        burning_time = burning_time_p2
        double_hit = double_hit_p2
        crit_chance = crit_chance_p2
        strength = strength_p2
        defense = defense_p2
        move_type = move_type_p2


def recieve_turns():
    global characters, character_p1, character_p2
    global damage, damage_p1, damage_p2
    global hp, p1_hp, p2_hp
    global burning_time, burning_time_p1, burning_time_p2
    global double_hit, double_hit_p1, double_hit_p2
    global crit_chance, crit_chance_p1, crit_chance_p2
    global strength, strength_p1, strength_p2
    global defense, defense_p1, defense_p2
    global move_type, move_type_p1, move_type_p2
    global oppo_hp

    if turn == 1:
        character_p1 = characters
        damage_p1 = damage
        p1_hp = hp
        p2_hp = oppo_hp
        burning_time_p1 = burning_time
        double_hit_p1 = double_hit
        crit_chance_p1 = crit_chance
        strength_p1 = strength
        defense_p1 = defense
        move_type_p1 = move_type

    if turn == 2:
        character_p2 = characters
        damage_p2 = damage
        p2_hp = hp
        p1_hp = oppo_hp
        burning_time_p2 = burning_time
        double_hit_p2 = double_hit
        crit_chance_p2 = crit_chance
        strength_p2 = strength
        defense_p2 = defense
        move_type_p2 = move_type


def character_choice():
    if turn == 1:
        print('Player 1:')
    if turn == 2:
        print('Player 2:')
    print('What character would you like to select')
    print('[1] Korma')
    print('[2] Zenith')
    print('[3] Galen')
    print('[4] Sharpshot')
    print()


def moves_choice():
    global move1, move2, move3, move4
    global hp
    if turn == 1:
        hp = p1_hp
        move1 = p1_move1
        move2 = p1_move2
        move3 = p1_move3
        move4 = p1_move4
    if turn == 2:
        hp = p2_hp
        move1 = p2_move1
        move2 = p2_move2
        move3 = p2_move3
        move4 = p2_move4
    print('')
    if turn == 1:
        print('Player 1:')
    if turn == 2:
        print('Player 2:')
    print('What move would you like to do:            HP:', hp)
    print("[1]", move1)
    print("[2]", move2)
    print("[3]", move3)
    print("[4]", move4)
    print('')


def reset():
    global p1_hp, p2_hp, strength_p1, strength_p2, crit_chance_p1, crit_chance_p2
    global double_hit_p1, double_hit_p2, burning_time_p1, burning_time_p2, burning_damage
    global crit_damage_p1, crit_damage_p2
    p1_hp, p2_hp = 100, 100
    strength_p1, strength_p2 = 1, 1
    crit_chance_p1, crit_chance_p2 = 10, 10
    crit_damage_p1, crit_damage_p2 = 3, 3
    double_hit_p1, double_hit_p2 = 20, 20
    burning_time_p1, burning_time_p2 = 0, 0
    burning_damage = 2


def health_int():
    global oppo_hp
    oppo_hp = int(oppo_hp)


def oppositing_turn():
    global oppo_turn
    if turn == 1:
        oppo_turn = 2
    if turn == 2:
        oppo_turn = 1


def set_character():
    global character_p1, p1_move1, p1_move2, p1_move3, p1_move4
    global character_p2, p2_move1, p2_move2, p2_move3, p2_move4
    global characters, move1, move2, move3, move4
    character_choice()
    while True:
        choose_characters = int(input())
        if choose_characters == 1:
            characters = 'Korma'
            print('You have selected', characters)
            print('')
            move1 = 'Hellish slash'
            move2 = 'Hellish fire'
            move3 = 'Sins redemption'
            move4 = "Devil's Wrath"
            sleep(2)

        elif choose_characters == 2:
            characters = 'Zenith'
            print('You have selected', characters)
            print('')
            move1 = 'Zap'
            move2 = 'Strategize'
            move3 = 'Knowledge'
            move4 = 'Checkmate'
            sleep(2)

        elif choose_characters == 3:
            characters = 'Galen'
            print('You have selected', characters)
            print('')
            move1 = 'Teachings'
            move2 = "God's blessing"
            move3 = 'Blessed'
            move4 = 'Ressurect'
            sleep(2)

        elif choose_characters == 4:
            characters = 'Sharpshot'
            print('You have selected', characters)
            print('')
            move1 = 'Bang'
            move2 = 'Headshot'
            move3 = 'Alchoholism'
            move4 = 'Take cover'
            sleep(2)

        else:
            print('That is not a valid answer, please type in again')

        if turn == 1:
            character_p1 = characters
            p1_move1 = move1
            p1_move2 = move2
            p1_move3 = move3
            p1_move4 = move4
            break

        if turn == 2:
            character_p2 = characters
            p2_move1 = move1
            p2_move2 = move2
            p2_move3 = move3
            p2_move4 = move4
            break


def action():
    global characters, character_p1, character_p2
    global damage, damage_p1, damage_p2
    global hp, p1_hp, p2_hp
    global burning_time, burning_time_p1, burning_time_p2
    global double_hit, double_hit_p1, double_hit_p2
    global crit_chance, crit_chance_p1, crit_chance_p2
    global strength, strength_p1, strength_p2
    global defense, defense_p1, defense_p2
    global move_type, move_type_p1, move_type_p2
    set_turns()


# Korma movesets
    if characters == 'Korma':
        if choose_moves == 1:
            damage = 10
            burning_time = burning_time + 2
            move_type = normal_move
        if choose_moves == 2:
            damage_p1 = 5
            burning_time = burning_time + 5
            move_type = normal_move
        if choose_moves == 3:
            damage = 0
            hp = hp + 15
            if hp > 100:
                hp = 100
            move_type = stat_move
            print('Player', turn, 'HP has risen by 15')
        if choose_moves == 4:
            damage = 0
            strength = strength + 0.5
            print('Player', turn, 'has risen strength by 5%')
            move_type = stat_move

# Zenith movesets
    if characters == 'Zenith':
        if choose_moves == 1:
            damage = 7
            double_hit = 70
            move_type = normal_move
        if choose_moves == 2:
            crit_chance = crit_chance + 5
            damage = 0
            move_type = stat_move
            print('Player', turn, 'has risen critical hit chance by 5%')
        if choose_moves == 3:
            damage = 10
        if choose_moves == 4:
            move_type = stat_move
            if p2_hp == 30:
                print('Player', oppo_turn, 'has the perfect amount of HP to get checkmated')
                sleep(0.5)
                damage = 30
            else:
                print('Move failed')
                sleep(1)
                print("Player", oppo_turn, "doesn't have the right circumstance to get checkmated")
                sleep(1)
                damage = 0

# Galen movesets
    if characters == 'Galen':
        if choose_moves == 1:
            damage = 10
            defense = defense + 0.2
            move_type = normal_move
        if choose_moves == 2:
            damage = 0
            crit_chance = crit_chance + 10
            print('Player', turn, 'has risen critical hit chance by 10%')
            move_type = stat_move
        if choose_moves == 3:
            damage = 0
            hp = hp + 20
            print('Player', turn, 'has heal 20 HP')
            move_type = stat_move
        if choose_moves == 4:
            damage = 0
            if hp <= 20:
                hp = hp + 75
                print('Player', turn, 'has heal 75 HP')
                move_type = stat_move

# Sharpshot movesets
    if characters == 'Sharpshot':
        if choose_moves == 1:
            damage = 10
            crit_chance = crit_chance + 2
            move_type = normal_move
        if choose_moves == 2:
            damage = 5
            crit_chance = crit_chance + 5
            move_type = normal_move
        if choose_moves == 3:
            damage = 0
            hp = hp + 10
            print('Player', turn, 'has heal 10 HP')
            move_type = stat_move
        if choose_moves == 4:
            if hp < 10:
                damage = 20
                move_type = normal_move
            else:
                damage = 0
                print('Move failed')
                sleep(1)
                print('Player', turn, 'HP is not low enough to use this move')
                sleep(1)
                move_type = stat_move

    damage = damage * strength


turn = 1
set_character()
turn = turn + 1
set_character()
print('The round will start in...')
print(3), sleep(1)
print(2), sleep(1)
print(1), sleep(1)
print('GO!!')
print()

# In the game
turn = turn - 1
while p1_hp and p2_hp > 0:
    set_turns()
    moves_choice()
    choose_moves = int(input())
    if choose_moves == 1:
        print(characters, 'used', move1)
        sleep(2)
        action()
    if choose_moves == 2:
        print(characters, 'used', move2)
        sleep(2)
        action()
    if choose_moves == 3:
        print(characters, 'used', move3)
        sleep(2)
        action()
    if choose_moves == 4:
        print(characters, 'used', move4)
        sleep(2)
        action()

    oppositing_turn()

# critical damage
    if move_type == normal_move:
        luck = randint(1, 100)
        if luck <= crit_chance:
            damage = crit_damage_p1 * damage
            print('Player', turn,  'has landed a devastating critical hit!!!')

# normal damage
    damage = damage / defense
    oppo_hp = oppo_hp - damage
    health_int()
    if oppo_hp == oppo_hp + damage:
        print('Player', oppo_turn, 'still has', oppo_hp, 'HP')
    else:
        print('Player', oppo_turn, 'now has', oppo_hp, 'HP left')
    sleep(2)

# double hit
    if move_type == normal_move:
        double_hit_luck = randint(1, 100)
        if double_hit_luck <= double_hit:
            double_hit_p1 = 20
            print('Player', turn, 'landed a double hit!!!')
            oppo_hp = oppo_hp - damage
            sleep(1)
            health_int()
            print('Player', oppo_turn, 'now has', oppo_hp, 'HP left')
            sleep(1)

# burning damage
    if burning_time > 0:
        luck = randint(1, 100)
        if luck <= 80:
            oppo_hp = oppo_hp - burning_damage
            print('Player', oppo_turn, 'has taken 2 damage from burning')
            sleep(0.5)
            burning_time = burning_time - 1
            health_int()
            print('Player', oppo_turn, 'now has', oppo_hp, 'HP left')
            sleep(1)

    recieve_turns()

    if oppo_hp <= 0:
        print('Player', oppo_turn, 'has been knockout!')

    if turn == 1:
        turn = 2
    elif turn == 2:
        turn = 1
