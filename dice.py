import random


def dice_roll(x):
    roll = []
    x += 1
    for y in range(1, x):
        roll.append(random.randint(1, 6))
    return roll


def count_straight(length):
    if length == 5:
        return 750
    elif length == 6:
        return 1500


def count_doubles():
    return 750


def count_triples(die):
    if die == 1:
        return 1000
    elif die > 1:
        num = str(die) + "00"
        return int(num)


def count_singles(die):
    if die == 1:
        return 100
    elif die == 5:
        return 50


def count_die(roll, num_die):
    ones = roll.count(1)
    twos = roll.count(2)
    threes = roll.count(3)
    fours = roll.count(4)
    fives = roll.count(5)
    sixes = roll.count(6)
    tots = [ones, twos, threes, fours, fives, sixes]
    die = num_die
    score = 0
    num2 = tots.count(2)
    num1 = tots.count(1)
    if num2 == 3:
        score += count_doubles()
        die -= 6
    for key, value in enumerate(tots):
        pos = key + 1
        if num1 > 3:
            if key == 0 and value == 2:
                if fives == 1:
                    score += count_straight(5) + count_singles(5) * value
                    die -= 6
            if key == 4 and value == 2:
                score += count_straight(5) + count_singles(5)
                die -= 6
        if value == 3:
            score += count_triples(pos)
            die -= 3
        if value == 6:
            score += (count_triples(pos)) * 2
            die -= 6
        if value == 4 and 2 in tots and key == 0:
            score += (count_triples(pos) + count_singles(1))
            die -= 4
        if value == 4 and 2 in tots and key != 0:
            score += count_doubles()
            die -= 6
        if value == 5:
            if key == 4:
                score += (count_triples(pos) + count_singles(5) * 2)
                die -= 5
            else:
                score += count_triples(pos)
                die -= 3
    if ones == twos == threes == fours == fives == sixes:
        score += count_straight(6)
        die -= 6
    if die == 0:
        return score, 6
    if ones < 3 and die > 0:
        score += count_singles(1) * ones
        die -= ones
    if fives < 3 and die > 0:
        score += count_singles(5) * fives
        die -= fives
    if score > 0:
        return score, die
    if score == 0:
        return 0, 0


def take_turn(last_round=False, on_the_board=False, gambler=False):
    score = 0
    if on_the_board is False or last_round:
        stats = count_die(dice_roll(6), 6)
        if stats[0] == 0:
            return 0
        score += stats[0]
        die = stats[1]
        while score < 1000:
            new_roll = count_die(dice_roll(die), die)
            if new_roll != (0, 0):
                score += new_roll[0]
                die = new_roll[1]
                if die == 0:
                    die = 6
            elif new_roll == (0, 0):
                return 0
        if score > 999:
            return score

    if gambler is False and on_the_board:
        stats = count_die(dice_roll(6), 6)
        if stats[0] == 0:
            return 0
        score += stats[0]
        die = stats[1]
        while score < 350:
            new_roll = count_die(dice_roll(die), die)
            if new_roll != (0, 0):
                score += new_roll[0]
                die = new_roll[1]
                if die == 0:
                    die = 6
            elif new_roll == (0, 0):
                return 0
        if score >= 350:
            return score
    elif gambler and on_the_board:
        stats = count_die(dice_roll(6), 6)
        if stats[0] == 0:
            return 0
        score += stats[0]
        die = stats[1]
        while score < 750:
            new_roll = count_die(dice_roll(die), die)
            if new_roll != (0, 0):
                score += new_roll[0]
                die = new_roll[1]
                if die == 0:
                    die = 6
            elif new_roll == (0, 0):
                return 0
        if score >= 750:
            return score


def play_the_game():
    p1_score = 0
    p1_otb = False
    p2_score = 0
    p2_otb = False
    gambler_score = 0
    gamb_otb = False
    last_round = False
    last_turns = 0
    while p1_score < 10000 or p2_score < 10000 or gambler_score < 10000:
        if p1_otb is False:
            stats = take_turn()
            if stats != 0:
                p1_score += stats
                p1_otb = True
        if p2_otb is False:
            stats = take_turn()
            if stats != 0:
                p2_score += stats
                p2_otb = True
        if gamb_otb is False:
            stats = take_turn()
            if stats != 0:
                gambler_score += stats
                gamb_otb = True
        if last_round is False:
            if p1_otb:
                stats = take_turn(on_the_board=True)
                if stats != 0:
                    p1_score += stats
                    if p1_score > 10000:
                        last_round = True
            if p2_otb:
                stats = take_turn(on_the_board=True)
                if stats != 0:
                    p2_score += stats
                    if p2_score > 10000:
                        last_round = True
            if gamb_otb:
                stats = take_turn(on_the_board=True, gambler=True)
                if stats != 0:
                    gambler_score += stats
                    if gambler_score > 10000:
                        last_round = True
        if last_round:
            if p1_score < 10000:
                stats = take_turn(last_round=True, on_the_board=True)
                if stats != 0:
                    p1_score += stats
            if p2_score < 10000:
                stats = take_turn(last_round=True, on_the_board=True)
                if stats != 0:
                    p2_score += stats
            if gambler_score < 10000:
                stats = take_turn(last_round=True, on_the_board=True)
                if stats != 0:
                    gambler_score += stats

    if p1_score >= 10000 or p2_score >= 10000 or gambler_score >= 10000:
        print("Winner!")
        print("Player One {}, Player Two {}, Gambler {}".format(p1_score, p2_score, gambler_score))




play_the_game()
