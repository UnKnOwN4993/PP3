from time import *
from random import *
global move1, move2, move3, move4
stat_move = 'stat move'
normal_move = 'normal move'
move_type = move_type_p1 = move_type_p2 = normal_move
hp, p1_hp, p2_hp = 100, 100, 100
oppo_hp = 100
strength, strength_p1, strength_p2 = 1, 1, 1
crit_chance, crit_chance_p1, crit_chance_p2 = 10, 10, 10
crit_damage_p1, crit_damage_p2 = 3, 3
double_hit, double_hit_p1, double_hit_p2 = 20, 20, 20
burning_time, burning_time_p1, burning_time_p2 = 0, 0, 0
burning_damage = 2
damage, damage_p1, damage_p2 = 0, 0, 0
defense, defense_p1, defense_p2 = 1, 1, 1
characters, character_p1, character_p2 = '', '', ''
p1_move1, p1_move2, p1_move3, p1_move4 = '', '', '', ''
p2_move1, p2_move2, p2_move3, p2_move4 = '', '', '', ''
soul, soul_p1, soul_p2 = 0, 0, 0
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
    global soul, soul_p1, soul_p2

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
        soul = soul_p1

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
        soul = soul_p2


def recieve_turns():
    global characters, character_p1, character_p2
    global damage, damage_p1, damage_p2
    global hp, p1_hp, p2_hp
    global move1, move2, move3, move4
    global p1_move1, p1_move2, p1_move3, p1_move4
    global p2_move1, p2_move2, p2_move3, p2_move4
    global burning_time, burning_time_p1, burning_time_p2
    global double_hit, double_hit_p1, double_hit_p2
    global crit_chance, crit_chance_p1, crit_chance_p2
    global strength, strength_p1, strength_p2
    global defense, defense_p1, defense_p2
    global move_type, move_type_p1, move_type_p2
    global oppo_hp
    global soul, soul_p1, soul_p2

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
        p1_move1 = move1
        p1_move2 = move2
        p1_move3 = move3
        p1_move4 = move4
        soul_p1 = soul

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
        p2_move1 = move1
        p2_move2 = move2
        p2_move3 = move3
        p2_move4 = move4
        soul_p2 = soul


def character_choice():
    if turn == 1:
        print('Player 1:')
    if turn == 2:
        print('Player 2:')
    print('What character would you like to select')
    print('[1] Korma        [5] Splitzo')
    print('[2] Zenith       [6] Claec')
    print('[3] Galen        [r] Random')
    print('[4] Sharpshot')
    print()


def moves_choice():
    global crit_chance
    global move1, move2, move3, move4
    global hp
    if turn == 1:
        crit_chance = crit_chance_p1
        hp = p1_hp
        move1 = p1_move1
        move2 = p1_move2
        move3 = p1_move3
        move4 = p1_move4
    if turn == 2:
        crit_chance = crit_chance_p2
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

    print('What move would you like to do:            HP:', hp, '  CC:', crit_chance)
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
    crit_chance_p1, crit_chance_p2 = 100, 100
    crit_damage_p1, crit_damage_p2 = 3, 3
    double_hit_p1, double_hit_p2 = 200, 200
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
    choose_characters = 0
    while True:
        if choose_characters > 6 or choose_characters < 1:
            if choose_characters != 'r':
                choose_characters = input()

        if choose_characters == 'r':
            print('You have selected random')
            choose_characters = randint(1, 6)
            sleep(2)
            continue

        elif int(choose_characters) == 1:
            characters = 'Korma'
            print('You have selected', characters)
            print('')
            move1 = 'Hellish slash'
            move2 = 'Hellish fire'
            move3 = 'Sins redemption'
            move4 = "Devil's Wrath"
            sleep(2)

        elif int(choose_characters) == 2:
            characters = 'Zenith'
            print('You have selected', characters)
            print('')
            move1 = 'Zap'
            move2 = 'Strategize'
            move3 = 'Knowledge'
            move4 = 'Checkmate'
            sleep(2)

        elif int(choose_characters) == 3:
            characters = 'Galen'
            print('You have selected', characters)
            print('')
            move1 = 'Teachings'
            move2 = "God's blessing"
            move3 = 'Blessed'
            move4 = 'Ressurect'
            sleep(2)

        elif int(choose_characters) == 3:
            characters = 'Sharpshot'
            print('You have selected', characters)
            print('')
            move1 = 'Bang'
            move2 = 'Headshot'
            move3 = 'Bandage'
            move4 = 'Take cover'
            sleep(2)

        elif int(choose_characters) == 5:
            characters = 'Splitzo'
            print('You have selected', characters)
            print('')
            characters = 'Sovary'
            move1 = 'Slice'
            move2 = 'Spice'
            move3 = 'Flying croissant'
            move4 = 'Switch'
            sleep(2)

        elif int(choose_characters) == 6:
            characters = 'Claec'
            print('You have selected', characters)
            print('')
            move1 = 'Gather'
            move2 = 'Enhanced soul'
            move3 = 'Sacrificing soul'
            move4 = 'Soul unleash'
            sleep(2)

        else:
            print('That is not a valid choice, please choose the character again')
            print('')

        if 1 <= int(choose_characters) <= 6:
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
    global move1, move2, move3, move4
    global damage, damage_p1, damage_p2
    global hp, p1_hp, p2_hp
    global burning_time, burning_time_p1, burning_time_p2
    global double_hit, double_hit_p1, double_hit_p2
    global crit_chance, crit_chance_p1, crit_chance_p2
    global strength, strength_p1, strength_p2
    global defense, defense_p1, defense_p2
    global move_type, move_type_p1, move_type_p2
    global soul
    set_turns()


# Korma movesets
    if characters == 'Korma':
        if choose_moves == 1:
            damage = 10
            burning_time = burning_time + 1
            move_type = normal_move
        if choose_moves == 2:
            damage = 5
            burning_time = burning_time + 5
            move_type = normal_move
        if choose_moves == 3:
            damage = 0
            hp = hp + 5
            if hp > 100:
                hp = 100
            move_type = stat_move
            print('Player', turn, 'HP has risen by 5')
        if choose_moves == 4:
            damage = 0
            strength = strength + 0.2
            print('Player', turn, 'has risen strength by 2%')
            move_type = stat_move

# Zenith movesets
    if characters == 'Zenith':
        if choose_moves == 1:
            damage = 7
            double_hit = 70
            move_type = normal_move
        if choose_moves == 2:
            crit_chance = crit_chance + 10
            damage = 0
            move_type = stat_move
            print('Player', turn, 'has risen critical hit chance by 10%')
        if choose_moves == 3:
            damage = 10
            move_type = normal_move
        if choose_moves == 4:
            move_type = stat_move
            if oppo_hp == 30:
                print('Player', oppo_turn, 'has the perfect amount of HP to get checkmated')
                sleep(0.5)
                print('Player', oppo_turn, 'got checkmated!!')
                sleep(2)
                damage = 30
            else:
                print('Move failed')
                sleep(1)
                print("Player", oppo_turn, "doesn't have the right circumstance to get checkmated")
                sleep(1)
                damage = 0

# Galen movesets
    if characters == 'Galen':
        ressurect_time = 1
        if choose_moves == 1:
            damage = 10
            move_type = normal_move
        if choose_moves == 2:
            damage = 0
            crit_chance = crit_chance + 5
            print('Player', turn, 'has risen critical hit chance by 5%')
            move_type = stat_move
        if choose_moves == 3:
            damage = 0
            hp = hp + 20
            if hp > 100:
                hp = 100
            print('Player', turn, 'has heal 20 HP')
            move_type = stat_move
        if choose_moves == 4:
            damage = 0
            if hp <= 20:
                if ressurect_time > 0:
                    hp = hp + 75
                    print('Player', turn, 'has heal 75 HP')
                    ressurect_time = ressurect_time - 1
                    print('Player', turn, 'now has', ressurect_time, 'chances of ressurecting again')
                else:
                    print('Player', turn, 'has already ressurected and cannot be used again')
            else:
                print('Player', turn, "doesn't have the right circumstance to use ressurect")
            move_type = stat_move

# Sharpshot movesets
    if characters == 'Sharpshot':
        if choose_moves == 1:
            damage = 10
            crit_chance = crit_chance + 5
            move_type = normal_move
        if choose_moves == 2:
            damage = 5
            crit_chance = crit_chance + 10
            print('Player', turn, 'has risen critical hit chance by 10%')
            move_type = normal_move
        if choose_moves == 3:
            damage = 0
            hp = hp + 10
            if hp > 100:
                hp = 100
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

# Splitzo movesets
# Sovary movesets
    if characters == 'Sovary':
        if choose_moves == 1:
            damage = 10
            move_type = normal_move
        if choose_moves == 2:
            damage = 10
            burning_time = 1
            move_type = normal_move
        if choose_moves == 3:
            damage = 7
            double_hit = 60
            move_type = normal_move
        if choose_moves == 4:
            damage = 0
            characters = 'Swete'
            move1 = 'Coffee cake'
            move2 = 'Nutritious carrot'
            move3 = 'Delightful smoothie'
            print('Swete has taken over the body!!')
            move_type = stat_move

# Swete movesets
    elif characters == 'Swete':
        damage = 0
        move_type = stat_move
        if choose_moves == 1:
            strength = strength + 0.5
            print('Player', turn, 'has risen strength by 5%')
        if choose_moves == 2:
            crit_chance = crit_chance + 5
            print('Player', turn, 'has risen critical hit chance by 5%')
        if choose_moves == 3:
            hp = hp + 10
            if hp > 100:
                hp = 100
            print('Player', turn, 'has heal 10 HP')
        if choose_moves == 4:
            characters = 'Sovary'
            move1 = 'Slice'
            move2 = 'Spice'
            move3 = 'Flying croissant'
            print('Sovary has taken over the body!!')

# Claec movesets
    elif characters == 'Claec':
        if choose_moves == 1:
            damage = 0
            soul = soul + 1
            print('Player', turn, 'has gathered 1 soul')
            sleep(1)
            if soul == 1:
                print('Player', turn, 'now has', soul, 'soul')
            if soul > 1:
                print('Player', turn, 'now has', soul, 'souls')
            move_type = stat_move
        if choose_moves == 2:
            damage = 0
            strength = strength + 0.1
            print('Player', turn, 'has risen the strength of the souls by 1%')
            move_type = stat_move
        if choose_moves == 3:
            damage = 0
            hp = hp + 5
            if hp > 100:
                hp = 100
            print('Player', turn, 'has sacrificed 1 soul and heal 5 HP')
            move_type = stat_move
        if choose_moves == 4:
            if soul <= 4:
                damage = soul * 10
            if 5 <= soul <= 7:
                damage = soul * 11
            if soul >= 8:
                damage = soul * 12
            move_type = normal_move
            print('Player', turn, 'has unleased', soul, 'soul')
            soul = 0
            if strength > 1:
                strength = 1
                sleep(1)
                print("Player", turn, "soul's will now have the normal amount of strength")
                sleep(1)

    damage = damage * strength


print('What mode would you like to select?')
print('[1] 1 player mode')
print('[2] 2 player mode')
print('[3] Sandbag mode')
print('')
gamemode = int(input())
while True:
    if gamemode == 1:
        print('You have selected 1 player mode')
        break
    elif gamemode == 2:
        print('You have selected 2 player mode')
        break
    elif gamemode == 3:
        print('You have selected sandbag mode')
        break
    else:
        print('That is not a valid gamemode, please choose the gamemode again')
print('')
sleep(2)
turn = 1
set_character()
if gamemode == 1:
    turn = turn + 1
    set_character()
elif gamemode == 2:
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
while True:
    if gamemode == 3:
        turn = 1
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
            double_hit = 20
            print('Player', turn, 'landed a double hit!!!')
            oppo_hp = oppo_hp - damage
            sleep(1)
            health_int()
            print('Player', oppo_turn, 'now has', oppo_hp, 'HP left')
            sleep(1)

# burning damage
    if burning_time > 0:
        luck = randint(1, 100)
        if luck <= 60:
            oppo_hp = oppo_hp - burning_damage
            print('Player', oppo_turn, 'has taken 2 damage from burning')
            sleep(0.5)
            burning_time = burning_time - 1
            health_int()
            print('Player', oppo_turn, 'now has', oppo_hp, 'HP left')
            sleep(1)

    recieve_turns()

    if p1_hp <= 0:
        print('Player 1 has been knockout!')
        exit()
    if p2_hp <= 0:
        print('Player 2 has been knockout!')
        exit()

    if turn == 1:
        turn = 2
    elif turn == 2:
        turn = 1
