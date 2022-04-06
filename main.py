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


def character_choice():
    print('What character would you like to select')
    print('[1] Korma')
    print('[2] Zenith')
    print('[3] Galen')
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
    crit_chance_p1, crit_chance_p2 = 1, 1
    crit_damage_p1, crit_damage_p2 = 3, 3
    double_hit_p1, double_hit_p2 = 2, 2
    burning_time_p1, burning_time_p2 = 0, 0
    burning_damage = 2


def health_int():
    global p1_hp, p2_hp
    if p1_hp == int(p1_hp):
        p1_hp = int(p1_hp)
    if p2_hp == int(p2_hp):
        p2_hp = int(p2_hp)


def action():
    global damage_p1, damage_p2
    global p1_hp, p2_hp
    global burning_time_p1
    global double_hit_p1
    global crit_chance_p1
    global strength_p1
    global move_type
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
        if choose_moves == 4:
            damage_p1 = 0
            strength_p1 = strength_p1 + 0.2
            print('Player 1 has risen strength by 0.2')
            move_type = stat_move

    if characters == 'Zenith':
        if choose_moves == 1:
            damage_p1 = 7
            double_hit_p1 = 70
            move_type = normal_move
        if choose_moves == 2:
            crit_chance_p1 = crit_chance_p1 + 5
            damage_p1 = 0
            move_type = stat_move
        if choose_moves == 3:
            damage_p1 = 10
        if choose_moves == 4:
            damage_p1 = 10

    if characters == 'Galen':
        if choose_moves == 1:
            damage_p1 = 10
        if choose_moves == 2:
            damage_p1 = 10
        if choose_moves == 3:
            damage_p1 = 10
        if choose_moves == 4:
            damage_p1 = 10

    damage_p1 = damage_p1 * strength_p1


character_choice()
choose_characters = int(input())
while True:
    if choose_characters == 1:
        characters = 'Korma'
        print('You have selected Korma')
        move1 = 'Hellish slash'
        move2 = 'Hellish fire'
        move3 = 'Sins redemption'
        move4 = "Devil's Wrath"
        sleep(2)
        break
    if choose_characters == 2:
        characters = 'Zenith'
        print('You have selected Zenith')
        move1 = 'Zap'
        move2 = 'Strategize'
        move3 = 'Knowledge'
        move4 = 'Checkmate'
        sleep(2)
        break
    if choose_characters == 3:
        characters = 'Galen'
        print('You have selected Galen')
        move1 = 'Bullseye'
        move2 = 'Returning arrow'
        move3 = 'Disappearing arrow'
        move4 = 'Heal'
        sleep(2)
        break

print('The round will start in...')
print(3), sleep(1)
print(2), sleep(1)
print(1), sleep(1)
print('GO!!')
print()

# In the game
reset()
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
        p2_hp = p2_hp - burning_damage
        print('Player 2 has taken 2 damage from burning')
        sleep(0.5)
        burning_time_p1 = burning_time_p1 - 1
        health_int()
        print('Player 2 now has', p2_hp, 'HP left')
        sleep(1)

    if p2_hp <= 0:
        print('Player 2 got knockout!')
