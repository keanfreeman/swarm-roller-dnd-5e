# Kean Freeman 2017

import pdb
import dice
import sys
from math import floor

# class definitions
"""
print 'Swarm name? (examples: "Goblin", "Druid")'
print 'Swarm attack bonus? (examples: "+5", "-1", "+0")'
print 'Swarm dice? (examples: "1d6+2", "20d7-1", "5d6+3")'
print 'Hit Points per swarm individual? (examples: "7", "500")'
print 'Number of members of swarm? (examples: "2", "100")'
"""
class Swarm(object):
	def __init__(self, name, attackBonus, damageDice, averageDamage, hitPoints, size):
		self.name = name
		self.attackBonus = attackBonus
		self.damageDice = damageDice
		self.averageDamage = averageDamage
		self.individualHP = hitPoints
		self.size = size

		self.totalHP = self.individualHP * size
		self.currentHP = self.totalHP
		self.currentNumMembers = size

	def inflictDamage(self, damage):
		self.currentHP -= damage
		numDead = floor((self.totalHP - self.currentHP) / self.individualHP)
		self.currentNumMembers =self.size - int(numDead)

# function definitions
def optionsPrompt():
	print 'Input command, type \'help\', or enter \'q\' to exit'
def helpPage():
	print 'Available commands: \n'
	print '<roll/average/damage>  <adv/dis>'

def collectSwarmFromFile(fileName):
	print 'Collecting swarm info from ' + fileName + ':'
	with open(fileName) as f:
		fileList = f.read().splitlines()
		if len(fileList) < 5:
			print 'Error: not enough information in creature swarm input file'
			exit(1)

		name = fileList[0]
		print 'Swarm name is "' + name + '"'
		
		attackBonus = 0
		attackBonus += int(fileList[1])
		print 'Swarm attack bonus is: ' + str(attackBonus)

		damageDice = ""
		damageDice = fileList[2]
		print 'Swarm dice are: ' + damageDice

		averageDamage = 0
		averageDamage = calcAverageDamage(damageDice)
		print 'Swarm average damage is: ' + str(averageDamage)

		hitPoints = 0
		hitPoints += int(fileList[3])
		print 'Hit Points per swarm individual: ' + str(hitPoints)
		
		size = 0
		size += int(fileList[4])
		print 'Number of members of swarm: ' + str(size) + '\n'

		return Swarm(name, attackBonus, damageDice, averageDamage, hitPoints, size)



def swarmAttack(swarmIn, isAverageAttack, vantage):
	print 'AC of target? (examples: "5", "20")'
	targetAC = int(raw_input())

	isAdvantaged = False
	isDisadvantaged = False
	if vantage == 1:
		isAdvantaged = True
	elif vantage == 2:
		isDisadvantaged = True

	damage = 0
	# dice info below for calculations
	endOfDiceType = (swarmIn.damageDice).find('+')
	diceType = swarmIn.damageDice[:endOfDiceType]
	diceDamageModifier = int(swarmIn.damageDice[endOfDiceType + 1:])
	
	for i in range(swarmIn.currentNumMembers):
		attackRoll = 0
		if isAdvantaged:
			attackRoll1 = dice.roll('1d20t') + swarmIn.attackBonus
			attackRoll2 = dice.roll('1d20t') + swarmIn.attackBonus
			attackRoll = max(attackRoll1, attackRoll2)
		elif isDisadvantaged:
			attackRoll1 = dice.roll('1d20t') + swarmIn.attackBonus
			attackRoll2 = dice.roll('1d20t') + swarmIn.attackBonus
			attackRoll = min(attackRoll1, attackRoll2)
		else:
			attackRoll = dice.roll('1d20t') + swarmIn.attackBonus
		
		# critical hits always hit, and deal twice the damage dice
		if (attackRoll - swarmIn.attackBonus) == 20:
			if isAverageAttack:
				damage += ((swarmIn.averageDamage * 2) - diceDamageModifier)
			else:
				dCharPosition = diceType.find('d')
				numDice = int(diceType[:dCharPosition])
				numDice *= 2
				tempDiceType = str(numDice) + diceType[dCharPosition:]
				rollTotal = dice.roll(tempDiceType + 't') + diceDamageModifier
				damage += rollTotal

		elif attackRoll >= targetAC:
			if isAverageAttack:
				damage += swarmIn.averageDamage
			else:
				rollTotal = dice.roll(diceType + 't') + diceDamageModifier
				damage += rollTotal
		

	# TODO: calculating average damage as well for convenience
	"""
	numDice = diceType[:diceType.find('d')]
	diceShape = diceType[diceType.find('d') + 1:]
	averageDamageRoll = float(int(diceShape)/ float(2)) * int(numDice) + \
diceDamageModifier
	numberNeededToHit = targetAC - swarmIn.attackBonus
	chanceOfHitting = float((20 - numberNeededToHit) / float(20))
	
	print 'Approximate average damage: ' + \
str(int((chanceOfHitting * averageDamageRoll) * swarmIn.currentNumMembers))
	"""	
	if damage == 0:
		print 'The attack missed!\n'
	else:
		print 'The swarm deals ' + str(damage) + 'HP damage to the target!\n'

def calcAverageDamage(damageDice):
	dCharPosition = damageDice.find('d')
	endPos = damageDice.find('+')
	diceTypeAndNum = damageDice[:endPos]
	attackBonus = int(damageDice[endPos:])
	maxVal = float(diceTypeAndNum[dCharPosition + 1:])
	numDice = int(damageDice[:dCharPosition])
	average = floor((maxVal + 1) / 2) * numDice
	avgDmg = int(average) + attackBonus
	return avgDmg

def swarmTakesDamage(swarmIn):
	print 'How much HP damage does the swarm take?'
	damageTaken = int(raw_input())
	swarmIn.inflictDamage(damageTaken)
	if swarmIn.currentHP < 0:
		print 'The swarm has no more HP!'
	else:
		print 'After damage, the swarm has ' + str(swarmIn.currentHP) + \
' HP out of ' + str(swarmIn.totalHP) + 'HP!\nAlso, the swarm has ' + \
str(swarmIn.currentNumMembers) + ' member(s) remaining!\n'

# main
if len(sys.argv) != 2:
	print 'Error, need to input monster file name as argument'
	exit(1)
swarm1 = collectSwarmFromFile(sys.argv[1])

while True:
	optionsPrompt() 
	input = raw_input()

	if input.find('average') != -1:
		if input.find('adv') != -1:
			swarmAttack(swarm1, True, 1)
		elif input.find('dis') != -1:
			swarmAttack(swarm1, True, 2)
		else:
			swarmAttack(swarm1, True, 0)

	elif input.find('roll') != -1:
		if input.find('adv') != -1:
			swarmAttack(swarm1, False, 1)
		elif input.find('dis') != -1:
			swarmAttack(swarm1, False, 2)
		else:
			swarmAttack(swarm1, False, 0)

	elif input.find('damage') != -1:
		swarmTakesDamage(swarm1)
	
	elif (input == 'help'):
		helpPage()
			
	elif (input == 'q'):
		print 'Program terminating'
		exit()
	else:
		print 'Invalid option selected\n'
