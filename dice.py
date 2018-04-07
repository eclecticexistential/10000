import random


def dice_roll(x):
    roll = []
    for x in range(1,x):
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


def count_die(roll):
    ones = roll.count(1)
    twos = roll.count(2)
    threes = roll.count(3)
    fours = roll.count(4)
    fives = roll.count(5)
    sixes = roll.count(6)
    return ones, twos, threes, fours, fives, sixes


def roll_again(x):
    die = dice_roll(x)
    stats = count_die(die)
    return die, stats


def count5s_n_1s(x, y):
    if x != 3 and y == 0:
        return count_singles(1) * x
    if y != 3 and x == 0:
        return count_singles(5) * y
    if x != 3 and y != 3:
        return (count_singles(1) * x) + (count_singles(5) * y)


def get_score_full(roll):
    stats = count_die(roll)
    doubles = stats.count(2)
    triples = stats.count(3)
    score = 0
    if stats == (1, 1, 1, 1, 1, 1):
        return count_straight(6)
    if stats in [(1, 2, 1, 1, 1, 0), (1, 1, 2, 1, 1, 0), (1, 1, 1, 2, 1, 0), (0, 2, 1, 1, 1, 1), (0, 1, 2, 1, 1, 1), (0, 1, 1, 2, 1, 1), (0, 1, 1, 1, 1, 2)]:
        score += count_straight(5)
    if stats in [(2, 1, 1, 1, 1, 0), (2, 0, 1, 1, 1, 1)]:
        num = count_straight(5) + count_singles(1)
        score += num
    if stats in [(0, 1, 1, 1, 2, 1), (1, 1, 1, 1, 2, 0)]:
        num = count_straight(5) + count_singles(5)
        score += num
    if doubles == 3:
        score += count_doubles()
        return score
    if triples > 0:
        for key, value in enumerate(stats):
            if value == 3:
                num = key + 1
                score += count_triples(num)
    if stats[0] != 3 and stats[0] > 0 and stats[4] == 0 or stats[4] == 3:
        score += count5s_n_1s(stats[0], 0)
    if stats[4] != 3 and stats[4] > 0 and stats[0] == 0 or stats[0] == 3:
        score += count5s_n_1s(0, stats[4])
    if stats[0] != 3 and stats[0] != 0 and stats[4] != 0 and stats[4] != 3 and score == 0:
        score += count5s_n_1s(stats[0], stats[4])
    return score, roll, stats


def play_the_game(stats, on_the_board=False, gamble=False):
    score = 0
    if len(stats) > 1:
        score += stats[0]
        if score >= 1000:
            if on_the_board is False or gamble is False:
                return score
        num1 = stats[1].count(1)
        num5 = stats[1].count(5)
        dice = 6
        if 3 in stats[2]:
            dice -= 3
        if num1 < 3:
            dice -= num1
        if num5 < 3:
            dice -= num5
        while dice > 0:
            print(score)
            if on_the_board == False:
                if score >= 1000:
                    return 1000
                new_roll = roll_again(dice)
                print(new_roll)
                if new_roll[1][0] == 0 and new_roll[1][4] == 0:
                    print("busted")
                    return 0
                if 3 in new_roll:
                    for key, value in enumerate(new_roll):
                        if value == 3:
                            num = key + 1
                            score += count_triples(num)
                            print("Never tell me the odds!")
                            new_hand = roll_again(7)
                            add_score = get_score_full(new_hand[0])
                            print(dice)
                            dice = 0
                if new_roll[1][0] in range(1, 3):
                    score += count_singles(1)
                    dice -= new_roll[1][0]
                if new_roll[1][4] in range(1, 3):
                    score += count_singles(5)
                    dice -= new_roll[1][4]
                else:
                    print(score)
                    print("garbage.")
                    dice = 0


def keep_track():
    stats = get_score_full(dice_roll(7))
    score = 0
    print(stats)
    if type(stats) == int():
        if stats == 1500:
            print("full-straight")
            new_hand = roll_again(7)
            add_score = get_score_full(new_hand[0])
            return play_the_game(add_score)
        if stats == 750:
            print("doubles")
            new_hand = roll_again(7)
            add_score = get_score_full(new_hand[0])
            return play_the_game(add_score)
    # work on what happens once you get on the board.
    return play_the_game(stats)

keep_track()
