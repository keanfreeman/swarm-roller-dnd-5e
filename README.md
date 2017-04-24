# swarm-roller-dnd-5e
# by Kean Freeman
A python script that helps a Dungeon Master keep track of many weaker enemies at once!

*Introduction*

Hello! I'm a DM for D&D 5th edition. I like to throw a variety of monsters 
at my players, including weaker ones that they could easily defeat. 
However, these monsters tend to become irrelevant pretty quickly if there 
aren't many of them. The nice thing about 5th edition, however, is a big 
crowd of weaker monsters can overcome a much stronger one after enough 
of them become part of the battle. This allows you to do some cool stuff; 
for example, if your players can't defeat a dragon themselves, they could 
pay a village of 50 commoners to help them shoot at the dragon with 
longbows. In previous editions, this sort of thing was impossible, but 
in this edition, a group like this could be a credible threat to a dragon!

Similarly, a DM can use this fact to make mobs of weak enemies tougher. 
If a small number of orcs can't challenge your party, throw a couple of 
swarms at them and see how they do!

So, why use this script? Keeping track of many, many monsters becomes 
too much after there are about 10 of them or so, in my experience. 
Also, the existing mass combat rules I feel oversimplify things, 
overcomplicate things, or aren't balanced very well.

*Usage as of 4/24/17*

"python swarmRoller.py <creatureFile.txt>"

creatureFile.txt must be formatted as follows (look at goblin.txt for an example):

|swarm name|

|swarm attack bonus|

|swarm dice type| (must be of the format in the following examples: 
1d6+3, or 2d12+0, or 1d4-1)

|HP of individual in swarm|

|number of individuals in swarm|

*Future Features*

In the future, I'd like to add:
1. The user can make some/all of the swarm make a saving throw
2. The user can impose disadvantage on the swarm's attack 
rolls/saving throws
3. A graphical user interface
