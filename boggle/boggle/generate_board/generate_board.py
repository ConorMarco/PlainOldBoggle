import random
import more_itertools

def generate_board(dice, size):
	faceup = [random.choice(die) for die in dice]
	random.shuffle(faceup)
	return list(more_itertools.chunked(faceup, size))

def make_dicelist_from_file(filename):
	return [s.strip().split(',') for s in open(filename, 'r').readlines()]


classic_four_dice = make_dicelist_from_file('classic_four_dice.csv')
new_four_dice = make_dicelist_from_file('new_four_dice.csv')

