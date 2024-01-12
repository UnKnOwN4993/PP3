from time import *
from random import *

stat_move = 'stat move'
normal_move = 'normal move'
gamemode = 0
in_gamemode_4 = False
gamemode_4_player = 0
move_type = normal_move
hp = [0, 100, 100]
oppo_hp = 100
strength = [0, 1, 1]
crit_chance = [0, 10, 10]
crit_damage = [0, 3, 3]
double_hit = 20
burning_time = [0, 0, 0]
damage = [0, 0, 0]
defense = [0, 1, 1]
characters = ['', '', '']
p1_moves = ['', '', '', '', '']
p2_moves = ['', '', '', '', '']
moves = ['', p1_moves, p2_moves]
soul = [0, 0, 0]
oppo_turn = 1
ressurect_time = [0, 1, 1]
choose_characters = 'a'


def character_choice():
    print(f'Player {turn}:')
    print('What character would you like to select')
    print('[1] Korma        [5] Splitzo')
    print('[2] Zenith       [6] Claec')
    print('[3] Galen        [7] New character')
    print('[4] Sharpshot    [r] random\n')


def moves_choice():
    print(f'\nPlayer {turn}:')

    int(hp[turn])
    print('What move would you like to do:            HP:', hp[turn], '  CC:', crit_chance[turn])
    print("[1]", moves[turn][1])
    print("[2]", moves[turn][2])
    print("[3]", moves[turn][3])
    print("[4]", moves[turn][4])
    print('')


def oppositing_turn():
    global oppo_turn, oppo_hp
    if turn == 1:
        oppo_turn = 2
        oppo_hp = hp[2]
    if turn == 2:
        oppo_turn = 1
        oppo_hp = hp[1]


def set_character():
    global characters
    global moves
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
            if int(choose_characters) > 6 or int(choose_characters) < 1:
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
            moves[turn][1] = 'Emotional damage'
            moves[turn][2] = 'Spare life'
            moves[turn][3] = 'Spare life'
            moves[turn][4] = 'Give homework'
            choose_characters = 1

        elif int(choose_characters) == 1:
            characters = 'Korma'
            if not in_gamemode_4:
                print('You have selected', characters)
                print('')
                sleep(2)
            moves[turn][1] = 'Hellish slash'
            moves[turn][2] = 'Hellish fire'
            moves[turn][3] = 'Sins redemption'
            moves[turn][4] = "Devil's Wrath"

        elif int(choose_characters) == 2:
            characters = 'Zenith'
            if not in_gamemode_4:
                print('You have selected', characters)
                print('')
                sleep(2)
            moves[turn][1] = 'Zap'
            moves[turn][2] = 'Strategize'
            moves[turn][3] = 'Knowledge'
            moves[turn][4] = 'Checkmate'

        elif int(choose_characters) == 3:
            characters = 'Galen'
            if not in_gamemode_4:
                print('You have selected', characters)
                print('')
                sleep(2)
            moves[turn][1] = 'Teachings'
            moves[turn][2] = "God's blessing"
            moves[turn][3] = 'Blessed'
            moves[turn][4] = 'Ressurect'

        elif int(choose_characters) == 4:
            characters = 'Sharpshot'
            if not in_gamemode_4:
                print('You have selected', characters)
                print('')
                sleep(2)
            moves[turn][1] = 'Bang'
            moves[turn][2] = 'Headshot'
            moves[turn][3] = 'Bandage'
            moves[turn][4] = 'Take cover'

        elif int(choose_characters) == 5:
            characters = 'Splitzo'
            if not in_gamemode_4:
                print('You have selected', characters)
                print('')
                sleep(2)
                characters = 'Sovary'
                moves[turn][1] = 'Slice'
                moves[turn][2] = 'Spice'
                moves[turn][3] = 'Flying croissant'
                moves[turn][4] = 'Switch'
            else:
                luck = randint(1, 2)
                if luck == 1:
                    characters = 'Sovary'
                    moves[turn][1] = 'Slice'
                    moves[turn][2] = 'Spice'
                    moves[turn][3] = 'Flying croissant'
                    moves[turn][4] = 'Switch'
                if luck == 2:
                    characters = 'Swete'
                    moves[turn][1] = 'Coffee cake'
                    moves[turn][2] = 'Nutritious carrot'
                    moves[turn][3] = 'Delightful smoothie'
                    moves[turn][4] = 'Switch'

        elif int(choose_characters) == 6:
            characters = 'Claec'
            if not in_gamemode_4:
                print('You have selected', characters)
                print('')
                sleep(2)
            moves[turn][1] = 'Gather'
            moves[turn][2] = 'Enhanced soul'
            moves[turn][3] = 'Sacrificing soul'
            moves[turn][4] = 'Soul unleash'

        else:
            print('That is not a valid choice, please choose the character again\n')
            continue

        if choose_characters == 'summon TSJ' or 1 <= int(choose_characters) <= 6:
            break


def action():
    global characters
    global damage
    global moves
    global hp
    global burning_time
    global double_hit
    global crit_chance
    global crit_damage
    global strength
    global move_type
    global luck
    global soul
    global ressurect_time

    # Korma movesets
    if characters == 'Korma':
        if choose_moves == 1:
            print(turn)
            damage[turn] = 10
            burning_time[turn] += 1
            move_type = normal_move
        if choose_moves == 2:
            damage[turn] = 5
            burning_time[turn] += 5
            move_type = normal_move
        if choose_moves == 3:
            damage[turn] = 0
            hp[turn] += 5
            if hp[turn] > 100:
                hp[turn] = 100
            move_type = stat_move
            print('Player', turn, 'HP has risen by 5')
        if choose_moves == 4:
            damage[turn] = 0
            strength[turn] += 0.2
            print('Player', turn, 'has risen strength by 20%')
            move_type = stat_move

    # Zenith movesets
    if characters == 'Zenith':
        if choose_moves == 1:
            damage[turn] = 7
            double_hit = 70
            move_type = normal_move
        if choose_moves == 2:
            crit_chance[turn] += 10
            damage[turn] = 0
            move_type = stat_move
            print('Player', turn, 'has risen critical hit chance by 10%')
        if choose_moves == 3:
            damage[turn] = 10
            move_type = normal_move
        if choose_moves == 4:
            move_type = stat_move
            if oppo_hp == 40:
                print('Player', oppo_turn, 'has the perfect amount of HP to get checkmated')
                sleep(0.5)
                print('Player', oppo_turn, 'got checkmated!!')
                sleep(2)
                damage[turn] = 40
            else:
                print('Move failed')
                sleep(1)
                print("Player", oppo_turn, "doesn't have the right circumstance to get checkmated")
                sleep(1)
                damage[turn] = 0

    # Galen movesets
    if characters == 'Galen':
        if choose_moves == 1:
            damage[turn] = 10
            move_type = normal_move
        if choose_moves == 2:
            damage[turn] = 0
            crit_chance[turn] += 5
            print('Player', turn, 'has risen critical hit chance by 5%')
            move_type = stat_move
        if choose_moves == 3:
            damage[turn] = 0
            hp[turn] += 15
            if hp[turn] > 100:
                hp[turn] = 100
            print('Player', turn, 'has heal 15 HP')
            move_type = stat_move
        if choose_moves == 4:
            damage[turn] = 0
            if hp[turn] <= 20:
                if ressurect_time[turn] > 0:
                    hp[turn] = hp[turn] + 75
                    print('Player', turn, 'has heal 75 HP')
                    ressurect_time[turn] -= 1
                    print('Player', turn, 'now has', ressurect_time[turn], 'chances of ressurecting again')
                else:
                    print('Player', turn, 'has already ressurected and cannot be used again')
            else:
                print('Player', turn, "doesn't have the right circumstance to use ressurect")
            move_type = stat_move

    # Sharpshot movesets
    if characters == 'Sharpshot':
        if choose_moves == 1:
            damage[turn] = 10
            crit_chance[turn] += 5
            move_type = normal_move
        if choose_moves == 2:
            damage[turn] = 5
            crit_chance[turn] += 10
            print('Player', turn, 'has risen critical hit chance by 10%')
            move_type = normal_move
        if choose_moves == 3:
            damage[turn] = 0
            hp[turn] += 7
            if hp[turn] > 100:
                hp[turn] = 100
            print('Player', turn, 'has heal 7 HP')
            move_type = stat_move
        if choose_moves == 4:
            if hp[turn] <= 15:
                damage[turn] = 40
                move_type = normal_move
            else:
                damage[turn] = 0
                print('Move failed')
                sleep(1)
                print('Player', turn, 'HP is not low enough to use this move')
                sleep(1)
                move_type = stat_move

    # Splitzo movesets
    # Sovary movesets
    if characters == 'Sovary':
        if choose_moves == 1:
            damage[turn] = 10
            move_type = normal_move
        if choose_moves == 2:
            damage[turn] = 2
            burning_time[turn] = 5
            move_type = normal_move
        if choose_moves == 3:
            damage[turn] = 7
            double_hit = 60
            move_type = normal_move
        if choose_moves == 4:
            damage[turn] = 0
            characters = 'Swete'
            moves[turn][1] = 'Coffee cake'
            moves[turn][2] = 'Nutritious carrot'
            moves[turn][3] = 'Delightful smoothie'
            print('Swete has taken over the body!!')
            move_type = stat_move

    # Swete movesets
    elif characters == 'Swete':
        damage[turn] = 0
        move_type = stat_move
        if choose_moves == 1:
            strength[turn] += 0.5
            print('Player', turn, 'has risen strength by 50%')
        if choose_moves == 2:
            crit_chance[turn] += 7
            print('Player', turn, 'has risen critical hit chance by 7%')
        if choose_moves == 3:
            hp[turn] += 10
            if hp[turn] > 100:
                hp[turn] = 100
            print('Player', turn, 'has heal 10 HP')
        if choose_moves == 4:
            characters = 'Sovary'
            moves[turn][1] = 'Slice'
            moves[turn][2] = 'Spice'
            moves[turn][3] = 'Flying croissant'
            print('Sovary has taken over the body!!')

    # Claec movesets
    elif characters == 'Claec':
        if choose_moves == 1:
            damage[turn] = 0
            soul[turn] += 1
            luck = randint(1, 10)
            if luck <= 3:
                soul[turn] += 2
                print('Player', turn, 'got lucky and has gathered 2 souls')
            else:
                print('Player', turn, 'has gathered 1 soul')
            sleep(1)
            if soul[turn] == 1:
                print('Player', turn, 'now has', soul[turn], 'soul')
            if soul[turn] > 1:
                print('Player', turn, 'now has', soul[turn], 'souls')
            move_type = stat_move
        if choose_moves == 2:
            damage[turn] = 0
            strength[turn] += 0.1
            print('Player', turn, 'has risen the strength of the souls by 10%')
            move_type = stat_move
        if choose_moves == 3:
            damage[turn] = 0
            if soul[turn] > 0:
                hp[turn] += 5
                if hp[turn] > 100:
                    hp[turn] = 100
                print('Player', turn, 'has sacrificed 1 soul and heal 5 HP')
                soul[turn] -= 1
            else:
                print('Player', turn, "doesn't have enough souls to heal")
            move_type = stat_move
        if choose_moves == 4:
            if soul[turn] <= 3:
                damage[turn] = soul[turn] * 11
            if 4 <= soul[turn] <= 6:
                damage[turn] = soul[turn] * 12
            if soul[turn] >= 7:
                damage[turn] = soul[turn] * 13
            move_type = normal_move
            print('Player', turn, 'has unleashed', soul[turn], 'soul')
            soul[turn] = 0
            if strength > 1:
                strength = 1
                sleep(1)
                print("Player", turn, "soul's will now have the normal amount of strength")
                sleep(1)

    elif characters == 'Teacher Saijai':
        hp[turn] = 100000
        crit_damage[turn] = 1000
        crit_chance[turn] = 300
        double_hit = 200
        move_type = stat_move
        if choose_moves == 1:
            damage[turn] = 99
        if choose_moves == 2:
            damage[turn] = 0
            print('TSJ has spared your life')
        if choose_moves == 3:
            damage[turn] = 0
            print('TSJ has spared your life')
        if choose_moves == 4:
            strength[turn] = 1000
            damage[turn] = 1000
            move_type = normal_move

    damage[turn] *= strength[turn]


def bot_turn():
    global characters
    global damage
    global hp, oppo_hp
    global burning_time
    global double_hit
    global crit_chance
    global strength
    global defense
    global move_type
    global luck
    global soul
    global choose_moves
    global ressurect_time

    while True:

        # Korma bot
        if characters == 'Korma':
            choose_moves = randint(1, 4)
            if choose_moves == 2:
                if burning_time[turn] == 0:
                    break
            elif choose_moves == 3:
                if hp[turn] <= 95:
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
            if hp[turn] <= 20:
                choose_moves = 4
            if choose_moves == 3:
                if hp[turn] <= 80:
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
                if hp[turn] <= 93:
                    break
            elif hp[turn] <= 15:
                choose_moves = 4
            else:
                break

        # Sovary bot
        if characters == 'Sovary':
            choose_moves = randint(1, 4)
            if choose_moves == 2:
                if burning_time[turn] <= 0:
                    break
            else:
                break

        # Swete bot
        if characters == 'Swete':
            choose_moves = randint(1, 4)
            if choose_moves == 3:
                if hp[turn] <= 90:
                    break
            else:
                break

        # Claec bot
        if characters == 'Claec':
            choose_moves = randint(1, 2)
            luck = randint(1, 10)
            if luck == 1:
                if soul[turn] > 0:
                    choose_moves = 3
                    break
            elif choose_moves == 2:
                if luck >= 3:
                    choose_moves = 2
                else:
                    choose_moves = 1
            elif soul[turn] >= 5:
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

if gamemode != 3:
    turn = 2
    set_character()

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
    choose_moves = 0
    if gamemode == 4:
        choose_characters = 'r'
        set_character()
        crit_chance[turn] = randint(1, 100)
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
    print(characters, 'used', moves[turn][choose_moves])
    sleep(2)
    action()

    # critical damage
    if move_type == normal_move:
        luck = randint(1, 100)
        if luck <= crit_chance[turn]:
            damage[turn] *= 3
            print('Player', turn, 'has landed a devastating critical hit!!!')

    # normal damage
    if choose_moves > 4:
        damage[turn] = 0
    oppo_hp -= damage[turn]
    if oppo_hp == oppo_hp + damage[turn]:
        print('Player', oppo_turn, 'still has', int(oppo_hp), 'HP')
    else:
        print('Player', oppo_turn, 'now has', int(oppo_hp), 'HP left')
    sleep(2)

    # double hit
    if move_type == normal_move:
        double_hit_luck = randint(1, 100)
        if double_hit_luck <= double_hit:
            print('Player', turn, 'landed a double hit!!!')
            oppo_hp -= damage[turn]
            sleep(1)
            print('Player', oppo_turn, 'now has', int(oppo_hp), 'HP left')
            sleep(1)
        double_hit = 20

    # burning damage
    if burning_time[turn] > 0:
        luck = randint(1, 100)
        burning_time[turn] -= 1
        if luck <= 90:
            oppo_hp -= 2
            print('Player', oppo_turn, 'has taken 2 damage from burning')
            sleep(0.5)
            print('Player', oppo_turn, 'now has', int(oppo_hp), 'HP left')
            sleep(1)

    if hp[turn] <= 0:
        print(f'Player {turn} has been knockout!')
        exit()

    if turn == 1:
        turn = 2
        hp[2] = oppo_hp
    elif turn == 2:
        turn = 1
        hp[1] = oppo_hp
