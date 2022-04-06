from time import *
from random import *
global move1, move2, move3, move4
stat_move = 'stat move'
normal_move = 'normal move'
move_type = normal_move
p1_hp, p2_hp = 100, 100
strength_p1, strength_p2 = 1, 1
crit_chance_p1, crit_chance_p2 = 10, 10
crit_damage_p1, crit_damage_p2 = 3, 3
double_hit_p1, double_hit_p2 = 20, 20
burning_time_p1, burning_time_p2 = 0, 0
burning_damage = 2
damage_p1, damage_p2 = 0, 0
defense_p1, defense_p2 = 1, 1


def character_choice():
    print('What character would you like to select')
    print('[1] Korma')
    print('[2] Zenith')
    print('[3] Galen')
    print('[4] Sharpshot')
    print()


def moves_choice():
    print('')
    print('What move would you like to do:            HP:', p1_hp)
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
    global p1_hp, p2_hp
    p1_hp = int(p1_hp)
    p2_hp = int(p2_hp)


def action():
    global damage_p1, damage_p2
    global p1_hp, p2_hp
    global burning_time_p1
    global double_hit_p1
    global crit_chance_p1
    global strength_p1
    global defense_p1
    global move_type

# Korma movesets
    if characters == 'Korma':
        if choose_moves == 1:
            damage_p1 = 10
            burning_time_p1 = burning_time_p1 + 2
            move_type = normal_move
        if choose_moves == 2:
            damage_p1 = 5
            burning_time_p1 = burning_time_p1 + 5
            move_type = normal_move
        if choose_moves == 3:
            damage_p1 = 0
            p1_hp = p1_hp + 15
            if p1_hp > 100:
                p1_hp = 100
            move_type = stat_move
            print('Player 1 HP has risen by 15')
        if choose_moves == 4:
            damage_p1 = 0
            strength_p1 = strength_p1 + 0.5
            print('Player 1 has risen strength by 5%')
            move_type = stat_move

# Zenith movesets
    if characters == 'Zenith':
        if choose_moves == 1:
            damage_p1 = 7
            double_hit_p1 = 70
            move_type = normal_move
        if choose_moves == 2:
            crit_chance_p1 = crit_chance_p1 + 5
            damage_p1 = 0
            move_type = stat_move
            print('Player 1 has risen critical hit chance by 5%')
        if choose_moves == 3:
            damage_p1 = 10
        if choose_moves == 4:
            move_type = stat_move
            if p2_hp == 30:
                print('Player 2 has the perfect amount of HP to get checkmated')
                sleep(0.5)
                damage_p1 = 30
            else:
                print('Move failed')
                sleep(1)
                print("Player 2 doesn't have the right circumstance to get checkmated")
                sleep(1)
                damage_p1 = 0

# Galen movesets
    if characters == 'Galen':
        if choose_moves == 1:
            damage_p1 = 10
            defense_p1 = defense_p1 + 0.2
            move_type = normal_move
        if choose_moves == 2:
            damage_p1 = 0
            crit_chance_p1 = crit_chance_p1 + 10
            print('Player 1 has risen critical hit chance by 10%')
            move_type = stat_move
        if choose_moves == 3:
            damage_p1 = 0
            p1_hp = p1_hp + 20
            print('Player 1 has heal 20 HP')
            move_type = stat_move
        if choose_moves == 4:
            damage_p1 = 0
            if p1_hp <= 20:
                p1_hp = p1_hp + 75
                print('Player 1 has heal 75 HP')
                move_type = stat_move

# Sharpshot movesets
    if characters == 'Sharpshot':
        if choose_moves == 1:
            damage_p1 = 10
            crit_chance_p1 = crit_chance_p1 + 2
            move_type = normal_move
        if choose_moves == 2:
            damage_p1 = 5
            crit_chance_p1 = crit_chance_p1 + 5
            move_type = normal_move
        if choose_moves == 3:
            damage_p1 = 0
            p1_hp = p1_hp + 10
            print('Player 1 has heal 10 HP')
            move_type = stat_move
        if choose_moves == 4:
            if p1_hp < 10:
                damage_p1 = 20
                move_type = normal_move
            else:
                damage_p1 = 0
                print('Move failed')
                sleep(1)
                print('Player 1 HP is not low enough to use this move')
                sleep(1)
                move_type = stat_move

    damage_p1 = damage_p1 * strength_p1


character_choice()
choose_characters = int(input())
while True:
    if choose_characters == 1:
        characters = 'Korma'
        print('You have selected', characters)
        move1 = 'Hellish slash'
        move2 = 'Hellish fire'
        move3 = 'Sins redemption'
        move4 = "Devil's Wrath"
        sleep(2)
        break
    if choose_characters == 2:
        characters = 'Zenith'
        print('You have selected', characters)
        move1 = 'Zap'
        move2 = 'Strategize'
        move3 = 'Knowledge'
        move4 = 'Checkmate'
        sleep(2)
        break
    if choose_characters == 3:
        characters = 'Galen'
        print('You have selected', characters)
        move1 = 'Teachings'
        move2 = "God's blessing"
        move3 = 'Blessed'
        move4 = 'Ressurect'
        sleep(2)
        break
    if choose_characters == 4:
        characters = 'Sharpshot'
        print('You have selected', characters)
        move1 = 'Bang'
        move2 = 'Headshot'
        move3 = 'Alchoholism'
        move4 = 'Take cover'
        sleep(2)
        break

print('The round will start in...')
print(3), sleep(1)
print(2), sleep(1)
print(1), sleep(1)
print('GO!!')
print()

# In the game
while p2_hp > 0:
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

# critical damage
    if move_type == normal_move:
        luck = randint(1, 100)
        if luck <= crit_chance_p1:
            damage_p1 = crit_damage_p1 * damage_p1
            print('Player 1 has landed a devastating critical hit!!!')

# normal damage
    damage_p1 = damage_p1 / defense_p2
    p2_hp = p2_hp - damage_p1
    health_int()
    if p2_hp == p2_hp + damage_p1:
        print('Player 2 still has', p2_hp, 'HP')
    else:
        print('Player 2 now has', p2_hp, 'HP left')
    sleep(2)

# double hit
    if move_type == normal_move:
        double_hit_luck = randint(1, 100)
        if double_hit_luck <= double_hit_p1:
            double_hit_p1 = 20
            print('Player 1 landed a double hit!!!')
            p2_hp = p2_hp - damage_p1
            sleep(1)
            health_int()
            print('Player 2 now has', p2_hp, 'HP left')
            sleep(1)

# burning damage
    if burning_time_p1 > 0:
        luck = randint(1, 100)
        if luck <= 80:
            p2_hp = p2_hp - burning_damage
            print('Player 2 has taken 2 damage from burning')
            sleep(0.5)
            burning_time_p1 = burning_time_p1 - 1
            health_int()
            print('Player 2 now has', p2_hp, 'HP left')
            sleep(1)

    if p2_hp <= 0:
        print('Player 2 has been knockout!')
