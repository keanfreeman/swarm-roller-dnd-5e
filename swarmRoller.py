# Kean Freeman 2017

import pdb
import dice

# function definitions
def optionsPrompt():
    print 'Input desired action:'
    print '"1": the swarm attacks'
    print '"2": the swarm takes damage'
    print '"q": quit'

# main
print 'Swarm attack bonus? (examples: "+5", "-1", "+0")'
attackBonus = 0
attackBonus += input()

print 'Swarm dice? (examples: "1d6+2", "20d7-1", "5d6+3")'
swarmDice = ""
swarmDice = raw_input()

print 'AC of target? (examples: "5", "20")'
targetAC = 0
targetAC += input()

print 'Hit Points per swarm individual? (examples: "7", "500")'
hitPoints = 0
hitPoints += input()

print 'Number of members of swarm? (examples: "2", "100")'
swarmSize = 0
swarmSize += input()

totalHP = hitPoints * swarmSize

pdb.set_trace()

while True:
    optionsPrompt()    
