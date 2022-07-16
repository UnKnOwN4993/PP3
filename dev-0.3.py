from time import *
from random import *

global move1, move2, move3, move4
stat_move = 'stat move'
normal_move = 'normal move'
gamemode = 0
in_gamemode_4 = False
gamemode_4_player = 0
move_type = move_type_p1 = move_type_p2 = normal_move
hp, p1_hp, p2_hp = 100, 100, 100
oppo_hp = 100
strength, strength_p1, strength_p2 = 1, 1, 1
crit_chance, crit_chance_p1, crit_chance_p2 = 10, 10, 10
crit_damage, crit_damage_p1, crit_damage_p2 = 3, 3, 3
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
choose_characters = 0
ressurect_time, ressurect_time_p1, ressurect_time_p2 = 1, 1, 1


def set_turns():
    global characters, character_p1, character_p2
    global damage, damage_p1, damage_p2
    global hp, p1_hp, p2_hp
    global burning_time, burning_time_p1, burning_time_p2
    global double_hit, double_hit_p1, double_hit_p2
    global crit_chance, crit_chance_p1, crit_chance_p2
    global crit_damage, crit_damage_p1, crit_damage_p2
    global strength, strength_p1, strength_p2
    global defense, defense_p1, defense_p2
    global move_type, move_type_p1, move_type_p2
    global oppo_hp
    global soul, soul_p1, soul_p2
    global ressurect_time, ressurect_time_p1, ressurect_time_p2
    global p1_move1, p1_move2, p1_move3, p1_move4
    global p2_move1, p2_move2, p2_move3, p1_move4
    global move1, move2, move3, move4

    if turn == 1:
        characters = character_p1
        damage = damage_p1
        hp = p1_hp
        oppo_hp = p2_hp
        burning_time = burning_time_p1
        double_hit = double_hit_p1
        crit_chance = crit_chance_p1
        crit_damage = crit_damage_p1
        strength = strength_p1
        defense = defense_p1
        move_type = move_type_p1
        soul = soul_p1
        ressurect_time = ressurect_time_p1
        move1 = p1_move1
        move2 = p1_move2
        move3 = p1_move3
        move4 = p1_move4

    if turn == 2:
        characters = character_p2
        damage = damage_p2
        hp = p2_hp
        oppo_hp = p1_hp
        burning_time = burning_time_p2
        double_hit = double_hit_p2
        crit_chance = crit_chance_p2
        crit_damage = crit_damage_p2
        strength = strength_p2
        defense = defense_p2
        move_type = move_type_p2
        soul = soul_p2
        ressurect_time = ressurect_time_p2
        move1 = p2_move1
        move2 = p2_move2
        move3 = p2_move3
        move4 = p2_move4


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
    global crit_damage, crit_damage_p1, crit_damage_p2
    global strength, strength_p1, strength_p2
    global defense, defense_p1, defense_p2
    global move_type, move_type_p1, move_type_p2
    global oppo_hp
    global soul, soul_p1, soul_p2
    global ressurect_time, ressurect_time_p1, ressurect_time_p2

    if turn == 1:
        character_p1 = characters
        damage_p1 = damage
        p1_hp = hp
        p2_hp = oppo_hp
        burning_time_p1 = burning_time
        double_hit_p1 = double_hit
        crit_chance_p1 = crit_chance
        crit_damage_p1 = crit_damage
        strength_p1 = strength
        defense_p1 = defense
        move_type_p1 = move_type
        p1_move1 = move1
        p1_move2 = move2
        p1_move3 = move3
        p1_move4 = move4
        soul_p1 = soul
        ressurect_time_p1 = ressurect_time

    if turn == 2:
        character_p2 = characters
        damage_p2 = damage
        p2_hp = hp
        p1_hp = oppo_hp
        burning_time_p2 = burning_time
        double_hit_p2 = double_hit
        crit_chance_p2 = crit_chance
        crit_damage_p2 = crit_damage
        strength_p2 = strength
        defense_p2 = defense
        move_type_p2 = move_type
        p2_move1 = move1
        p2_move2 = move2
        p2_move3 = move3
        p2_move4 = move4
        soul_p2 = soul
        ressurect_time_p2 = ressurect_time


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
    global crit_chance, crit_chance_p1, crit_chance_p2
    global crit_damage, crit_damage_p1, crit_damage_p2
    global hp, p1_hp, p2_hp
    global double_hit
    global characters, move1, move2, move3, move4
    global choose_characters
    global gamemode
    global luck
    if not in_gamemode_4:
        if choose_characters != 'r':
            character_choice()
    else:
        choose_characters = 'r'
    if choose_characters != 'r':
        choose_characters = 0
    while True:
        if choose_characters != 'r':
            if choose_characters > 6 or choose_characters < 1:
                choose_characters = input()

        if choose_characters == 'r':
            if not in_gamemode_4:
                print('You have selected random')
                sleep(2)
            choose_characters = randint(1, 6)
            continue

        elif choose_characters == 'summon TSJ':
            characters = 'Teacher Saijai'
            print('You have summmoned TSJ!!!')
            sleep(2)
            print('The world SHALL PERRISH IN HER HANDS')
            sleep(2)
            move1 = 'Emotional damage'
            move2 = 'Spare life'
            move3 = 'Spare life'
            move4 = 'Give homework'
            choose_characters = 1

        elif int(choose_characters) == 1:
            characters = 'Korma'
            if not in_gamemode_4:
                print('You have selected', characters)
                print('')
                sleep(2)
            move1 = 'Hellish slash'
            move2 = 'Hellish fire'
            move3 = 'Sins redemption'
            move4 = "Devil's Wrath"

        elif int(choose_characters) == 2:
            characters = 'Zenith'
            if not in_gamemode_4:
                print('You have selected', characters)
                print('')
                sleep(2)
            move1 = 'Zap'
            move2 = 'Strategize'
            move3 = 'Knowledge'
            move4 = 'Checkmate'

        elif int(choose_characters) == 3:
            characters = 'Galen'
            if not in_gamemode_4:
                print('You have selected', characters)
                print('')
                sleep(2)
            move1 = 'Teachings'
            move2 = "God's blessing"
            move3 = 'Blessed'
            move4 = 'Ressurect'
        elif int(choose_characters) == 4:
            characters = 'Sharpshot'
            if not in_gamemode_4:
                print('You have selected', characters)
                print('')
                sleep(2)
            move1 = 'Bang'
            move2 = 'Headshot'
            move3 = 'Bandage'
            move4 = 'Take cover'

        elif int(choose_characters) == 5:
            characters = 'Splitzo'
            if not in_gamemode_4:
                print('You have selected', characters)
                print('')
                sleep(2)
                characters = 'Sovary'
                move1 = 'Slice'
                move2 = 'Spice'
                move3 = 'Flying croissant'
                move4 = 'Switch'
            else:
                luck = randint(1, 2)
                if luck == 1:
                    characters = 'Sovary'
                    move1 = 'Slice'
                    move2 = 'Spice'
                    move3 = 'Flying croissant'
                    move4 = 'Switch'
                if luck == 2:
                    characters = 'Swete'
                    move1 = 'Coffee cake'
                    move2 = 'Nutritious carrot'
                    move3 = 'Delightful smoothie'
                    move4 = 'Switch'

        elif int(choose_characters) == 6:
            characters = 'Claec'
            if not in_gamemode_4:
                print('You have selected', characters)
                print('')
                sleep(2)
            move1 = 'Gather'
            move2 = 'Enhanced soul'
            move3 = 'Sacrificing soul'
            move4 = 'Soul unleash'

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
    global crit_damage, crit_damage_p1, crit_damage_p2
    global strength, strength_p1, strength_p2
    global defense, defense_p1, defense_p2
    global move_type, move_type_p1, move_type_p2
    global luck
    global soul
    global ressurect_time
    set_turns()

    # Korma movesets
    if characters == 'Korma':
        if choose_moves == 1:
            damage = 10
            burning_time += 1
            move_type = normal_move
        if choose_moves == 2:
            damage = 5
            burning_time += 5
            move_type = normal_move
        if choose_moves == 3:
            damage = 0
            hp += 5
            if hp > 100:
                hp = 100
            move_type = stat_move
            print('Player', turn, 'HP has risen by 5')
        if choose_moves == 4:
            damage = 0
            strength += 0.2
            print('Player', turn, 'has risen strength by 20%')
            move_type = stat_move

    # Zenith movesets
    if characters == 'Zenith':
        if choose_moves == 1:
            damage = 7
            double_hit = 70
            move_type = normal_move
        if choose_moves == 2:
            crit_chance += 10
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
        if choose_moves == 1:
            damage = 10
            move_type = normal_move
        if choose_moves == 2:
            damage = 0
            crit_chance += 5
            print('Player', turn, 'has risen critical hit chance by 5%')
            move_type = stat_move
        if choose_moves == 3:
            damage = 0
            hp += 15
            if hp > 100:
                hp = 100
            print('Player', turn, 'has heal 15 HP')
            move_type = stat_move
        if choose_moves == 4:
            damage = 0
            if hp <= 20:
                if ressurect_time > 0:
                    hp = hp + 75
                    print('Player', turn, 'has heal 75 HP')
                    ressurect_time -= 1
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
            crit_chance += 5
            move_type = normal_move
        if choose_moves == 2:
            damage = 5
            crit_chance += 10
            print('Player', turn, 'has risen critical hit chance by 10%')
            move_type = normal_move
        if choose_moves == 3:
            damage = 0
            hp += 7
            if hp > 100:
                hp = 100
            print('Player', turn, 'has heal 7 HP')
            move_type = stat_move
        if choose_moves == 4:
            if hp <= 15:
                damage = 40
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
            damage = 2
            burning_time = 5
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
            strength += 0.5
            print('Player', turn, 'has risen strength by 50%')
        if choose_moves == 2:
            crit_chance += 7
            print('Player', turn, 'has risen critical hit chance by 7%')
        if choose_moves == 3:
            hp += 10
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
            soul += 1
            luck = randint(1, 10)
            if luck <= 3:
                soul += 2
                print('Player', turn, 'got lucky and has gathered 2 souls')
            else:
                print('Player', turn, 'has gathered 1 soul')
            sleep(1)
            if soul == 1:
                print('Player', turn, 'now has', soul, 'soul')
            if soul > 1:
                print('Player', turn, 'now has', soul, 'souls')
            move_type = stat_move
        if choose_moves == 2:
            damage = 0
            strength += 0.1
            print('Player', turn, 'has risen the strength of the souls by 10%')
            move_type = stat_move
        if choose_moves == 3:
            damage = 0
            if soul > 0:
                hp += 5
                if hp > 100:
                    hp = 100
                print('Player', turn, 'has sacrificed 1 soul and heal 5 HP')
                soul -= 1
            else:
                print('Player', turn, "doesn't have enough souls to heal")
            move_type = stat_move
        if choose_moves == 4:
            if soul <= 3:
                damage = soul * 11
            if 4 <= soul <= 6:
                damage = soul * 12
            if soul >= 7:
                damage = soul * 13
            move_type = normal_move
            print('Player', turn, 'has unleashed', soul, 'soul')
            soul = 0
            if strength > 1:
                strength = 1
                sleep(1)
                print("Player", turn, "soul's will now have the normal amount of strength")
                sleep(1)

    elif characters == 'Teacher Saijai':
        hp = 100000
        crit_damage = 1000
        crit_chance = 300
        double_hit = 200
        move_type = stat_move
        if choose_moves == 1:
            damage = 99
        if choose_moves == 2:
            damage = 0
            print('TSJ has spared your life')
        if choose_moves == 3:
            damage = 0
            print('TSJ has spared your life')
        if choose_moves == 4:
            strength = 1000
            damage = 1000
            move_type = normal_move

    damage *= strength


def bot_turn():
    global characters, character_p1, character_p2
    global move1, move2, move3, move4
    global damage, damage_p1, damage_p2
    global hp, p1_hp, p2_hp, oppo_hp
    global burning_time, burning_time_p1, burning_time_p2
    global double_hit, double_hit_p1, double_hit_p2
    global crit_chance, crit_chance_p1, crit_chance_p2
    global strength, strength_p1, strength_p2
    global defense, defense_p1, defense_p2
    global move_type, move_type_p1, move_type_p2
    global luck
    global soul
    global choose_moves
    global ressurect_time, ressurect_time_p1, ressurect_time_p2

    while True:

        # Korma bot
        if characters == 'Korma':
            choose_moves = randint(1, 4)
            if choose_moves == 2:
                if burning_time == 0:
                    break
            elif choose_moves == 3:
                if hp <= 95:
                    break
            elif oppo_hp < 20:
                choose_moves = 1
                break
            else:
                break

        # Zenith bot
        if characters == 'Zenith':
            choose_moves = randint(1, 3)
            if oppo_hp == 30:
                choose_moves = 4
                break
            elif oppo_hp < 20:
                choose_moves = 1
            else:
                break

        # Galen bot
        if characters == 'Galen':
            choose_moves = randint(1, 3)  
            if hp <= 20:
                choose_moves = 4
            if choose_moves == 3:
                if hp <= 80:
                    break
            elif oppo_hp < 20:
                choose_moves = 1
                break
            else:
                break

        # Sharpshot bot
        if characters == 'Sharpshot':
            choose_moves = randint(1, 3)
            if choose_moves == 3:
                if hp <= 93:
                    break
            elif hp <= 15:
                choose_moves = 4
            else:
                break

        # Sovary bot
        if characters == 'Sovary':
            choose_moves = randint(1, 4)
            if choose_moves == 2:
                if burning_time <= 0:
                    break
            else:
                break

        # Swete bot
        if characters == 'Swete':
            choose_moves = randint(1, 4)
            if choose_moves == 3:
                if hp <= 90:
                    break
            else:
                break

        # Claec bot
        if characters == 'Claec':
            choose_moves = randint(1, 2)
            luck = randint(1, 10)
            if luck == 1:
                if soul > 0:
                    choose_moves = 3
                    break
            elif choose_moves == 2:
                if luck >= 3:
                    choose_moves = 2
                else:
                    choose_moves = 1
            elif soul >= 5:
                choose_moves = 4
                break
            else:
                break

        # TSJ bot
        if characters == 'Teacher Saijai':
            if oppo_hp == 100:
                choose_moves = 1
                break
            else:
                choose_moves = 4
                break


# In the game
print('What mode would you like to select?')
print('[1] Single player')
print('[2] Multiplayer')
print('[3] Sandbag mode')
print('[4] Randomizer mode')
print('')
while True:
    gamemode = int(input())
    if gamemode == 1:
        print('You have selected single player')
        break
    elif gamemode == 2:
        print('You have selected multiplayer')
        break
    elif gamemode == 3:
        print('You have selected sandbag mode')
        break
    elif gamemode == 4:
        print('You have selected randomizer mode')
        in_gamemode_4 = True
        sleep(1)
        print('\nHow many people are playing this mode?')
        print('[1] 1 player')
        print('[2] 2 players')
        gamemode_4_player = int(input('\n'))
        if gamemode_4_player == 1:
            print('You have selected 1 player randomizer')
        if gamemode_4_player == 2:
            print('You have selected 2 player randomizer')
        break
    else:
        print('That is not a valid gamemode, please choose the gamemode again')

print('')
sleep(2)
turn = 1
set_character()
set_turns()

if gamemode != 3:
    turn = 2
    set_character()
    set_turns()

print('The round will start in...')
print(3), sleep(1)
print(2), sleep(1)
print(1), sleep(1)
print('GO!!')
print()

turn = turn - 1
while True:
    if gamemode == 3:
        turn = 1
    set_turns()
    choose_moves = 0
    if gamemode == 4:
        choose_characters = 'r'
        set_character()
        crit_chance_p1 = randint(1, 100)
        crit_chance_p2 = randint(1, 100)
    if gamemode == 1 or gamemode_4_player == 1:
        if turn == 2:
            sleep(1)
            print('')
            bot_turn()
        if turn == 1:
            moves_choice()
            choose_moves = int(input())
    else:
        moves_choice()
        choose_moves = int(input())

    oppositing_turn()
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
        if luck <= crit_chance:
            damage = crit_damage_p1 * damage
            print('Player', turn, 'has landed a devastating critical hit!!!')

    # normal damage
    if choose_moves > 4:
        damage = 0
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
            print('Player', turn, 'landed a double hit!!!')
            oppo_hp = oppo_hp - damage
            sleep(1)
            health_int()
            print('Player', oppo_turn, 'now has', oppo_hp, 'HP left')
            sleep(1)
        double_hit = 20

    # burning damage
    if burning_time > 0:
        luck = randint(1, 100)
        burning_time = burning_time - 1
        if luck <= 90:
            oppo_hp = oppo_hp - burning_damage
            print('Player', oppo_turn, 'has taken 2 damage from burning')
            sleep(0.5)
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
