#HEADER
#Created by: Scott Russell
#Practicing my python (Small game example)
#Time, os, and sys used for typewriter printing
import time,os,sys


#random stuff
from random import seed
from random import randint
import random

#Typewriter printing
def printo(text):
	for character in text:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.00)
	print("")
	return

#Typewriter printing for input line
def printi(text):
	for character in text:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.00)   
	value = input() 
	return value  

#Clear screen 
def clearScreen():
  os.system("cls")

#Initial screen display
def intro():
	printo ("---INTRO---")
	printo ("Welcome to Scott's Game\n")
	return 0
 
#Selecting a class name
def character_name():
	while 1:
		printo("---NAME SELECTION SCREEN---")
		#pick a name
		
		name = str(printi("Please Enter a Character Name: "))
		confirm = printi("Are you sure you want to be named: "+name+"? (y/n): ")
		
		if str(confirm) == "y" or str(confirm) == "Y":
			clearScreen()
			return name
		elif str(confirm) == "n" or str(confirm) == "N":
			printo("You may choose another name!")
		else:
			printo("Invalid input. Let's try again.")
			
#Contains list of player classes, and provides input for selection
def class_selection(name):
	
	#IMPORTANT: To change the # of character classes simply chang the class_count variable
	# You must also add/remove a line from the class Defintions array below. That's it!
	class_count = 3
	
	#Define a 2D Array to contain all the information needed for classes
	rows, cols = (class_count, 11)
	array = [[0]*cols]*rows	
	
	printo("Below is a list of the available classes")
	
	#Class Definitions
	#		   Name, Role,	 Base-HP,	Max-HP, Weapon Name,	Weapon-L,   Weapon-H,   Weapon Crit%,	Strength,   Dexterity,  Constitution,	Level	First Strike	Restoration	Protection
	array[0] = [name,"Soldier", 10,		 10,	 "Broken Sword", 1,		  	4,		  	10,			 	14,		 	8,		  	12,				1,		0,				4,					0]
	array[0].append("A strong and well balanced warrior, the soldier is able to restore health between fights.")
	
	array[1] = [name,"Rogue",   10,		 10,	 "Rusty Dagger", 1,		  	3,		  	30,			 	10,		 	16,		 	8,				1,		1,				0,					0]
	array[1].append("The stealthy Rogue has an innate ability to always attack first.")
	
	array[2] = [name,"Bulwark", 10,		 10,	 "Dull Axe",	 1,		  	6,		  	0,			  	12,		 	8,		  	14,				1,		0,				0,					1]	
	array[2].append("With heavy armor the bulwark is protected against a portion of all attacks.")

	#For each Class assign statistics and display basic information
	for i in range(class_count):
		array[i] = set_stats(array[i])
   
	#Loop until a class is chosen
	while 1:  
		printo("\n---CLASS SELECTION SCREEN---")
		#Display the names of each class for input
		for i in range(class_count):
			printo("["+str(i+1)+"]= "+array[i].role +"\n"+array[i].description+"\n")
		#Using a try except to catch invalid input from user
		try:
			choice =int(printi("Select a class for in depth statistics: "))
			if choice <= class_count and choice >0:
				display_stats(array[choice-1])
				choice2 = printi("[1] - Confirm selection of class: ["+str(array[choice-1].role)+"]\n[2] - View List of Classes\n-->:")
				if str(choice2) != "1":
					continue
				clearScreen()
				return array[choice-1]
			else:
				printo("Invalid Input!\n")
				continue
		except ValueError as e:
			printo( "Invalid Input!\n")
			continue
 
	
#Displays in depth information for any character sent to this function.
def display_stats(character):
	printo ("\nName: " + character.name)
	printo ("Level: "+str(character.level))
	printo ("Role: " + (character.role))
	printo("Health: ["+str(character.health[0]) +"/"+str(character.health[1])+"]")
	printo("Weapon: ["+str(character.weapon) +"] ( Base Crit: ["+str(character.weaponC)+"%] )")
	printo("Base Damage: ["+str(character.weaponD[0])+"-"+str(character.weaponD[1])+"]")
	printo("Bonus Damage: ["+str(character.strength_bonus)+"]")
	printo("Critical Strike Chance: "+str(character.critical)+"%")
	printo("Strength: ["+str(character.strength) +"] provides a bonus of: ["+str(character.strength_bonus)+"] to damage.")
	printo("Dexterity: ["+str(character.dexterity) + "] provides a bonus of: ["+str(character.dexterity_bonus)+ "%] to Critical Strike Chance.")
	printo("(Dexterity: Also determines [Combat Order])")
	printo("Constitution: ["+str(character.constitution) + "] provides a bonus of: ["+str(character.constitution_bonus) +"] to health.")
	if character.first_strike == 1:
		printo("Special: [First Strike] in every combat")
	if character.restoration > 0:
		printo("Special: This character restores ["+str(character.restoration)+"] health after each battle")
	if character.protection > 0:
		printo("Special: Heavy Armor protects against ["+str(character.protection)+"] damage each combat")
	
	printo("\n")
	return 0
 #Assigns Statistics to character or enemies based on 11 input fields data[0] - data[10]
def set_stats(data):
	class Character:
		#Character Name
		name = data[0]
		#Character role
		role = data[1]
		#Current/Max
		base_health  = [data[2],data[3]]
		#Weapon Name
		weapon = data[4]
		#Damage has a low and high end
		weaponD = [data[5],data[6]]
		#Weapon Critical Strike Chance
		weaponC = data[7]
		
		#Strength of character --> Damage Bonus
		strength = data[8]
		strength_bonus = int((strength-10)/2)
		
		#Dexterity of character --> Critical Strike Bonus
		dexterity = data[9]
		dexterity_bonus = int((dexterity-10) / 2)*10
   
		#Constitution of Character --> Increased Health
		constitution = data[10]
		constitution_bonus = int((constitution-10) / 2)
		level = data[11]
		
		first_strike = data[12]
		restoration = data[13]
		protection = data[14]
		description = data[15]

		
		
		#Apply Attributes bonuses to damage, health, and critical strike chance
		damage = [weaponD[0]+strength_bonus,weaponD[1]+strength_bonus]
		#Prevents damage from being lower than 0
		if weaponD[0] < 0:
			weaponD[0] = 0
		
		health = [base_health[0]+constitution_bonus,base_health[1]+constitution_bonus]
		critical = weaponC + dexterity_bonus
		#Prevent critical strike chance from being lower than 0%
		if (critical < 0):
			critical = 0
	#Assign a player object to the class, and return
	Player = Character() 
	return Player


#select between Story Mode or Tower Mode
def gameplay_selection():  
	while 1:
		printo("You're adventure begins! Choose a gameplay mode.")
		try:
			choice = int(printi("[1] - Tower Mode  \n[2] - Story Mode\n-->:"))
			if choice == 1 or choice == 2:
				return choice
			else:
				printo("Invalid Input\n")
		except ValueError as e:
			printo( "Invalid Input!\n")
			continue
	return 0

#Tower mode, fight waves of enemies until you die
def tower_mode(Player):
	clearScreen()
	printo("---WELCOME TO TOWER MODE---")
	printo("In this mode, you will climb the tower.")
	printo("As you ascend, you will face stronger enemies")
	printo("How far can you go? good luck!\n")
	os.system('pause')
	
	Tower_Level = 1
	
	while 1:
		#Select an enemy based on tower level
		Enemy = enemy_selection(Tower_Level)  


		#Displays information about the character
		#display_stats(Player)
		clearScreen()
		printo("---ENEMY #"+str(Tower_Level)+"---")
		basic_stats(Enemy)
		
		printo("\n---YOUR STATS---")
		basic_stats(Player)
		
		os.system('pause')
		
		#perform combat
		combat(Player,Enemy)
		
		#If Tower Level = 10 win
		if Tower_Level == 10:
			victory_screen()
			
		#increase tower level following each victory
		Tower_Level += 1
	return 0
 
#Starting point for the game (Not implemented yet)
def story_mode(Player):
	printo("Story Mode not implemented yet, goodbye")
	return 0

#Enemy Selection for Tower Mode combat (Currently completely random no monster tiers)
def enemy_selection(Tower_Level):
  
	#Obtain a list of potential enemies
	if (Tower_Level < 5):
		enemy_stats = tier_one()	
	elif (Tower_Level < 10):
		enemy_stats = tier_two()
	else:
		enemy_stats = tier_three()
	#Code for randomly selecting an enemy based on time seed
	enemy_count = len(enemy_stats)
   
	#Select a random enemy based on how many are available
	random_value = randint(0,enemy_count-1)
	
	return enemy_stats[random_value]

#Tier 1 Biome: Forest
def tier_one():
	enemy_count = 5
	rows, cols = (enemy_count, 11)
	enemy_list = [[0]*cols]*rows  
	
		#			Name,			  	Role,		   Base-HP,	Max-HP,	Weapon,		 Weapon-L,   Weapon-H, 	Weapon Crit%   Strength Dexterity   Constitution	Level
	enemy_list[0] = ["Deer",			"Beast",   		5,		  5,	"Hoof",			2,		  3,		10,			 	8,	  	10,			8,				1]
	enemy_list[1] = ["Eagle",		  	"Beast",	  	5,		  5,	"Talon",		2,		  3,		10,			 	12,		8,			6,				1]
	enemy_list[2] = ["Red  Wolf",		"Beast",  		5,		  5,	"Fangs",		2,		  3,		10,			 	8,	  	12,			6,				1]
	enemy_list[3] = ["Boar",   			"Beast",	   	5,		  5,	"Tusks",		2,		  3,		10,			 	8,	  	8,			10,				1]
	enemy_list[4] = ["Angry Farmer",	"Human",		5,		  5,	"Pitchfork",	2,		  3,		10,			 	6,	  	6,			16,				1]
	enemy_stats = [0]*rows  
	#apply stats for all enemies created dynamically
	for i in range(enemy_count):
		enemy_stats[i] = set_enemy(enemy_list[i])
	return enemy_stats

def tier_two():
	enemy_count = 5
	rows, cols = (enemy_count, 11)
	enemy_list = [[0]*cols]*rows  
	
		#			Name,			  	Role,		   	Base-HP,	Max-HP,	 	Weapon,		 Weapon-L,   Weapon-H,	   Weapon Crit%   Strength Dexterity   Constitution Level
	enemy_list[0] = ["Red Wolf",		"Elemental",	5,		  	5,		  	"Fangs",		1,		  2,			  20,			 10,	 10,		 10,		1]
	enemy_list[1] = ["Goblin",		  	"Warrior",	  	2,		  	2,		 	"Rusty Dagger", 1,		  1,			  10,			 10,	 10,		 10,		1]
	enemy_list[2] = ["Injured Wolf",	"Pack Leader",  3,		  	6,		  	"Bite",		 	2,		  4,			  50,			 10,	 10,		 10,		1]
	enemy_list[3] = ["Angry Peasent",   "Farmer",	   	5,		  	5,		  	"Pitchfork",	1,		  1,			  10,			 10,	 10,		 10,		1]
	enemy_list[4] = ["Big Pig",		 	"Swine",		2,		  	2,		  	"Tusks",		1,		  2,			  10,			 10,	 10,		 10,		1]
	enemy_stats = [0]*rows  
	#apply stats for all enemies created dynamically
	for i in range(enemy_count):
		enemy_stats[i] = set_enemy(enemy_list[i])
	return enemy_stats

def tier_three():
	enemy_count = 1
	rows, cols = (enemy_count, 11)
	enemy_list = [[0]*cols]*rows  
	
		#			Name,			  			Role,		   	Base-HP,	Max-HP,	 	Weapon,		 Weapon-L,   Weapon-H,	   Weapon Crit%   Strength Dexterity   Constitution Level
	enemy_list[0] = ["The Black Knight",		"Demon",		20,		  	20,		  	"Halburk",		5,		  10,			  20,			 16,	 16,		 16,		5]

	enemy_stats = [0]*rows  
	#apply stats for all enemies created dynamically
	for i in range(enemy_count):
		enemy_stats[i] = set_enemy(enemy_list[i])
	return enemy_stats

#Sets the enemies Stats based on the tier
def set_enemy(data):
	class Character:
		#Character Name
		name = data[0]
		#Character role
		role = data[1]
		#Current/Max
		base_health  = [data[2],data[3]]
		#Weapon Name
		weapon = data[4]
		#Damage has a low and high end
		weaponD = [data[5],data[6]]
		#Weapon Critical Strike Chance
		weaponC = data[7]
		
		#Strength of character --> Damage Bonus
		strength = data[8]
		strength_bonus = int((strength-10)/2)
		
		#Dexterity of character --> Critical Strike Bonus
		dexterity = data[9]
		dexterity_bonus = int((dexterity-10) / 2)*10
   
		#Constitution of Character --> Increased Health
		constitution = data[10]
		constitution_bonus = int((constitution-10) / 2)
		level = data[11]
		
		#Enemies have no innate protection
		protection  = 0
		#Apply Attributes bonuses to damage, health, and critical strike chance
		damage = [weaponD[0]+strength_bonus,weaponD[1]+strength_bonus]
		#Prevents damage from being lower than 0
		if weaponD[0] < 0:
			weaponD[0] = 0
		
		health = [base_health[0]+constitution_bonus,base_health[1]+constitution_bonus]
		critical = weaponC + dexterity_bonus
		#Prevent critical strike chance from being lower than 0%
		if (critical < 0):
			critical = 0
	#Assign a player object to the class, and return
	Player = Character() 
	return Player

#Displays basic infomration about a character (Used in Tower mode for enemies)
def basic_stats(character):
	printo ("\nName: " + character.name+" ["+str(character.role)+"]")
	printo("Health: ["+str(character.health[0]) +"/"+str(character.health[1])+"]")
	printo("Weapon: ["+str(character.weapon)+"] ("+str(character.damage[0])+"-"+str(character.damage[1])+")")
	return 0

def combat_order(Player, Enemy):
	if Player.first_strike == 1:
		return 1
	return 0

#Based on first strike, loops each player back and 
#forth until someone is dead
def combat(Player,Enemy):
	while 1:
		order = combat_order(Player, Enemy)
		
		
		#enemy Attacks First
		else:
			
		#First strike we attack first
		if Player.first_strike:
			# (attacker,defender)
			result = damage_calculation(Player,Enemy,1)
			if result:
				break
			damage_calculation(Enemy,Player,0)
			   
			#Else, enemy attacks first
		else:
			damage_calculation(Enemy,Player,0)
			result = damage_calculation(Player,Enemy,1)
			if result:
				break
	
	restoration(Player)	
		
	return 0


#Heal character after combat if they have restoration
def restoration(Player):
	Player.health[0] = Player.health[0] + Player.restoration
	if Player.health[0] > Player.health[1]:
		Player.health[0] = Player.health[1]
	printo(str(Player.name)+" has restored: ["+str(Player.restoration)+"] health.")
	os.system('pause')
	return Player



 
#Calculates damaged based on attacker stats
def damage_calculation(Attacker,Defender,player_attacker):
	printo("\n")
	printo(Attacker.name+"'s turn...")
	
	if (player_attacker):
		while 1:
			try:
				selection = int(printi("[1] - Attack with ["+str(Attacker.weapon)+"] ("+str(Attacker.damage[0])+"-"+str(Attacker.damage[1])+")\nChoose:"))
				if selection == 1:
					break
				printo("Invalid Input!")
			except ValueError as e:
				printo("Invalid Input!\n")
				continue
		
	#Calculate damage based on random range between low and high end 
	damage = randint(Attacker.damage[0],Attacker.damage[1])
	
	#Roll a D100 to determine if a crit is rolled (if so, double the damage)
	critical = randint(1,100)
	if critical > 100 - Attacker.critical:
		damage = damage * 2
		printo("Critical hit!")

	
	
	#If the Defender has protection, reduce the damage (damage cannot be reduced below 0)
	if Defender.protection > 0:
		#Reduce Damage based on protection
		damage = damage - Defender.protection
		if damage < 0:
			damage = 0
		printo(str(Attacker.name)+" hits "+str(Defender.name)+" for: ["+str(damage)+"] Damage with: ["+str(Attacker.weapon)+"] (Protection ["+str(Defender.protection)+"] )")
	
	else: #Display damage output from attacker
		printo(str(Attacker.name)+" hits "+str(Defender.name)+" for: ["+str(damage)+"] Damage with: ["+str(Attacker.weapon)+"]")
	
	Defender.health[0] = Defender.health[0] - damage
	
	#Display how much health the defender has left
	printo(str(Defender.name)+" now has: ["+str(Defender.health[0])+"] / ["+str(Defender.health[1])+"]")
	os.system("pause")
   
	if Defender.health[0] <= 0:
		printo(Defender.name+" Has been defeated!")
		
		#If the player is not the attacker, they just died.
		if player_attacker == 0:
			gameover()
		return 1
	#Return 0 indicates the enemy has been defeated
	return 0





#Runs on death of the main character
def gameover():
	printo("You have died.")
	printo("Your adventure ends here...")
	sys.exit()
	
	return 0

def victory_screen():
	clearScreen()
	printo("You've ascended to the top of the tower.")
	printo("Victory is yours!")
	sys.exit()
	return 0
  
#Main is the hub that calls other functions to start the game   
def main(): 
	#Display intro screen
	intro()
	
	#Select a nam
	name = character_name()
	
	#pick a class
	Player = class_selection(name)

	#The Class Player now contains all info about the player.
	
	#Select a gameplay mode
	mode = gameplay_selection()
	
	if mode == 1:
		tower_mode(Player)
	if mode == 2:
		story_mode(Player)		  	
	return 0
	
#Call main to begin the game (Set random seed for randomness!)
seed(time.time())
main()