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


def count_die(roll):
    print(roll)
    ones = roll.count(1)
    twos = roll.count(2)
    threes = roll.count(3)
    fours = roll.count(4)
    fives = roll.count(5)
    sixes = roll.count(6)
    tots = [ones, twos, threes, fours, fives, sixes]
    die = 6
    score = 0
    if ones == twos == threes == fours == fives == sixes:
        return count_straight(6), die
    if ones > 0:
        if twos == threes == fours == fives:
            score = count_straight(5) + count_singles(1)
            return score, die
        if ones < 3:
            score += count_singles(1) * ones
            die -= ones
        if ones > 3:
            if ones == 6:
                score += count_triples(1) * 2
                return score, die
            else:
                score += count_singles(1) * (ones - 3)
                die -= (ones - 3)
    if 3 in tots:
        for key, value in enumerate(tots):
            if value == 3:
                score += count_triples(key+1)
                die -= 3
    if 4 in tots:
        for key, value in enumerate(tots):
            if value == 4:
                score += count_triples(key+1)
                die -= 3
    if fives > 0:
        if ones == twos == threes == fours:
            score = count_straight(5) + count_singles(5)
            return score, die
        if twos == threes == fours == sixes:
            score = count_straight(5) + count_singles(5)
            return score, die
        if fives < 3:
            score += count_singles(5) * fives
            die -= fives
        if fives > 3:
            if fives == 6:
                score += count_triples(5) * 2
                return score, die
            else:
                score += count_singles(5) * (fives - 3)
                die -= (fives - 3)
    if 2 in tots:
        num = tots.count(2)
        if num == 3:
            score = count_doubles()
            return score, die
    if score > 0:
        return score, die
    else:
        return roll



print(count_die(dice_roll(6)))