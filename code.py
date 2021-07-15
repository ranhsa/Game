#HEADER
#Created by: Scott Russell
#Practicing my python (Small game example)

#Time, os, and sys used for typewriter printing
import time,os,sys
#random Seed imports
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
def clear_screen():
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
		confirm = printi("Are you sure you want to be named: ["+name+"] (y/n): ")
		
		if str(confirm) == "y" or str(confirm) == "Y":
			clear_screen()
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
	
	#Class Definitions
	#		   Name, Role,	 Base-HP,	Max-HP, Weapon Name,	Weapon-L,   Weapon-H,   Weapon Crit%,	Strength,   Dexterity,  Constitution,	Level	First Strike	Restoration	Protection
	array[0] = [name,"Soldier", 20,		 20,	 "Broken Sword", 1,		  	4,		  	10,			 	5,		 	5,		  	5,				1,		0,				2,					0]
	array[0].append("A strong and well balanced warrior, the soldier is able to restore health between fights.")
	
	array[1] = [name,"Rogue",   20,		 20,	 "Rusty Dagger", 1,		  	4,		  	30,			 	5,		 	5,		 	5,				1,		1,				0,					0]
	array[1].append("The stealthy Rogue has an innate ability to always attack first.")
	
	array[2] = [name,"Bulwark", 20,		 20,	 "Dull Axe",	 1,		  	4,		  	0,			  	5,		 	5,		  	5,				1,		0,				0,					1]	
	array[2].append("With heavy armor the bulwark is protected against a portion of all attacks.")

	#For each Class assign statistics and display basic information
	for i in range(class_count):
		array[i] = set_stats(array[i])
   
	#Loop until a class is chosen
	while 1: 
		clear_screen()
		printo("\n---CLASS SELECTION SCREEN---")
		#Display the names of each class for input
		for i in range(class_count):
			printo("["+str(i+1)+"]=["+array[i].role +"]\n"+array[i].description+"\n")
		#Using a try except to catch invalid input from user
		try:
			choice =int(printi("Select a class for in depth statistics: "))
			if choice <= class_count and choice >0:
				display_stats(array[choice-1])
				choice2 = printi("[1] - Confirm selection of class: ["+str(array[choice-1].role)+"]\n[2] - Return to List of Classes\n-->:")
				if str(choice2) != "1":
					continue
				clear_screen()
				return array[choice-1]
			else:
				printo("Invalid Input!\n")
				os.system("pause")
				continue
		except ValueError as e:
			printo( "Invalid Input!\n")
			os.system("pause")
			continue
	
	#This line should not be reachable
	return 0
	
#Displays in depth information for any character sent to this function.
def display_stats(character):
	clear_screen()
	printo("---DETAILED-STATISTICS---")
	printo ("\nName: [" + character.name+"]")
	printo ("Level: ["+str(character.level)+"] Experience: ["+str(character.experience)+"/"+str(character.experience_to_level[character.level])+"]")
	printo ("Role: [" + (character.role)+"]")
	printo("Health: ["+str(character.health[0]) +"/"+str(character.health[1])+"]")
	printo("Weapon: ["+str(character.weapon) +"] ( Base Crit: ["+str(character.weaponC)+"%] )")
	printo("Base Damage: ["+str(character.weaponD[0])+"-"+str(character.weaponD[1])+"]")
	printo("Bonus Damage: ["+str(character.strength_bonus)+"]")
	printo("Critical Strike Chance: ["+str(character.critical)+"%]")
	printo("Strength: ["+str(character.strength) +"] provides a bonus of: ["+str(character.strength_bonus)+"] to damage.")
	printo("Dexterity: ["+str(character.dexterity) + "] provides a bonus of: ["+str(character.dexterity_bonus)+ "%] to Critical Strike Chance.")
	printo("Constitution: ["+str(character.constitution) + "] provides a bonus of: ["+str(character.constitution_bonus) +"] to health.")
	if character.first_strike == 1:
		printo("Special: [First Strike] in every combat")
	if character.restoration > 0:
		printo("Special: This character restores ["+str(character.restoration)+"] health after each battle")
	if character.protection > 0:
		printo("Special: Heavy Armor protects against ["+str(character.protection)+"] damage each combat")
	
	if character.tower_level > 0:
		printo("Tower Level: ["+str(character.tower_level)+"]")
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
		base_health  = data[2],data[3]
		#Weapon Name
		weapon = data[4]
		#Damage has a low and high end
		weaponD = [data[5],data[6]]
		#Weapon Critical Strike Chance
		weaponC = data[7]
		
		#Strength of character --> Damage Bonus
		strength = data[8]
		strength_bonus = int(strength-5)
		
		#Dexterity of character --> Critical Strike Bonus
		dexterity = data[9]
		dexterity_bonus = int(dexterity-5)*10
   
		#Constitution of Character --> Increased Health
		constitution = data[10]
		constitution_bonus = int(constitution-5)
		level = data[11]
		
		#First strike players always attack first
		first_strike = data[12]
		restoration = data[13]
		protection = data[14]
		description = data[15]
		is_player = True
		tower_level = 0
		
		#player starts with 0 experiencre
		experience = 0
		
		#break points for experience to level up
		experience_to_level = [0,5,10,15,20,25,30]
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
		printo("---CHOOSE A GAMEPLAY MODE---")
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
	clear_screen()
	printo("---WELCOME TO TOWER MODE---")
	printo("In this mode, you will climb the tower.")
	printo("As you ascend, you will face stronger enemies")
	printo("How far can you go? good luck!\n")
	os.system('pause')
	
	Player.tower_level = 1
	
	while 1:
		#Select an enemy based on tower level
		Enemy = enemy_selection(Player.tower_level)  


		#Displays information about the character
		#display_stats(Player)
		clear_screen()
		printo("---Tower Level: ["+str(Player.tower_level)+"]---")
		combat_stats(Enemy)

		combat_stats(Player)
		
		os.system('pause')
		
		#perform combat
		attack_order(Player,Enemy)
		
		#After combat is over, End of combat actions take place
		combat_end(Player,Enemy)
		
		#If Tower Level = 10 the player wins
		if Player.tower_level == 10:
			victory_screen(Player)
			
		#increase tower level following each victory
		Player.tower_level += 1
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
	enemy_list[0] = ["Deer",			"Beast",   		3,		  3,	"Hoof",			2,		  3,		20,			 	4,	  	4,			6,				1]
	enemy_list[1] = ["Eagle",		  	"Beast",	  	3,		  3,	"Talon",		2,		  3,		20,			 	6,		6,			3,				1]
	enemy_list[2] = ["Red  Wolf",		"Beast",  		3,		  3,	"Fangs",		2,		  3,		20,			 	5,	  	5,			5,				1]
	enemy_list[3] = ["Boar",   			"Beast",	   	3,		  3,	"Tusks",		2,		  3,		20,			 	4,	  	5,			7,				1]
	enemy_list[4] = ["Rabbit",			"Beast",		3,		  3,	"Teeth",		2,		  3,		20,			 	5,	  	7,			3,				1]
	enemy_stats = [0]*rows  
	#apply stats for all enemies created dynamically
	for i in range(enemy_count):
		enemy_stats[i] = set_enemy(enemy_list[i])
	return enemy_stats

def tier_two():
	enemy_count = 5
	rows, cols = (enemy_count, 11)
	enemy_list = [[0]*cols]*rows  
	
		#			Name,			  	Role,		   	Base-HP,	Max-HP,	 	Weapon,		 Weapon-L,   Weapon-H, Weapon Crit%   Strength Dexterity Constitution Level
	enemy_list[0] = ["Gate Guard",		"Human",		5,		  	5,		  	"Rusty Sword",	3,		  5,		20,			 	8,	 	5,		 	7,		2]
	enemy_list[1] = ["Archer",		  	"Human",	  	5,		  	5,		 	"Longbow", 		3,		  5,		20,			 	4,	 	12,		 	4,		2]
	enemy_list[2] = ["Pikeman",			"Human",  		5,		  	5,		  	"Pike",		 	3,		  5,		20,			 	5,	 	5,		 	5,		2]
	enemy_list[3] = ["Templar",   		"Human",	   	5,		  	5,		  	"Mace",			3,		  5,		20,			 	6,	 	6,			8,		2]
	enemy_list[4] = ["King's Guard",	"Human",		5,		  	5,		  	"Claymore",		3,		  5,		20,			 	10,	 	5,		 	5,		2]
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
	enemy_list[0] = ["The Black Knight",		"Demon",		10,		  	10,		  	"Halburk",		3,		  6,			  20,			 10,	 10,		 	10,			3]

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
		strength_bonus = int(strength-5)
		
		#Dexterity of character --> Critical Strike Bonus
		dexterity = data[9]
		dexterity_bonus = int(dexterity-5)*10
   
		#Constitution of Character --> Increased Health
		constitution = data[10]
		constitution_bonus = int(constitution-5)
		level = data[11]
		
		#Enemies are not the player
		is_player = False
		
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
def combat_stats(character):
	printo ("\n["+character.name+"] ["+str(character.role)+"] Level: ["+str(character.level)+"]")
	printo("Health: ["+str(character.health[0]) +"/"+str(character.health[1])+"]")
	printo("Weapon: ["+str(character.weapon)+"] ["+str(character.weaponD[0])+"-"+str(character.weaponD[1])+"] Bonus: ["+str(character.strength_bonus)+"]")
	return 0

#Based on first strike, loops each player back and 
#forth until someone is dead
def attack_order(Player,Enemy):

	#When result is 0, the enemy has been defeated
	end_of_combat = False
	while end_of_combat == False:
	
		#If the player has first strike, they attack first
		if Player.first_strike:
			# (attacker,defender)			
			end_of_combat = attack(Player,Enemy)
			end_of_combat = attack(Enemy,Player)
			   
			#Else, enemy attacks first
		else:
			end_of_combat = attack(Enemy,Player)
			end_of_combat = attack(Player,Enemy)
	
	return 0

#Defines actions that take place after combat finishes
def combat_end(Player,Enemy):
	clear_screen()
	printo("---Combat is Over---")
	printo(Enemy.name+" has been defeated!")
	experience(Player, Enemy)
	
	#If applicable, restore health to player
	restoration(Player)
	os.system("pause")
	display_stats(Player)
	os.system("pause")
	
	return 0
	
#Heal character after combat if they have restoration
def restoration(Player):
	if Player.restoration > 0:
		Player.health[0] = Player.health [0] + Player.restoration
		if Player.health[0] > Player.health[1]:
			Player.health[0] = Player.health[1]
		printo("\n"+str(Player.name)+"'s natural healing takes effect")
		printo(str(Player.name)+" has restored: ["+str(Player.restoration)+"] Health.")
		printo(str(Player.name)+": ["+str(Player.health[0])+"/"+str(Player.health[1])+"] Health")
	return Player

#Player chooses their action during combat
def combat_selection(Attacker,Defender):
	while 1:
		try:
			printo("[1] - Attack with ["+str(Attacker.weapon)+"] ("+str(Attacker.damage[0])+"-"+str(Attacker.damage[1])+")")
			printo("[2] - Wait")
			selection = int(printi("Choose:"))
			if selection == 1:
				return 1
			if selection == 2:
				return 2
			printo("Invalid Input!")
		except ValueError as e:
			printo("Invalid Input!\n")
			continue
	
	return 0
 
#If the player has 0 health, the game is over
def game_over_check(Attacker,Defender):
	if (Defender.health[0] <= 0 and Defender.is_player == True):
		clear_screen()
		printo("You have died.")
		printo("Your adventure ends here...")
		os.system("pause")
		display_stats(Defender)
		sys.exit()
		
	if (Attacker.health[0] <= 0 and Attacker.is_player == True):
		clear_screen()
		printo("You have died.")
		printo("Your adventure ends here...")
		display_stats(Attacker)
		sys.exit()
	return 0
 
#Calculates damaged based on attacker stats
def attack(Attacker,Defender):
	
	#Attacker cannot respond if they are dead
	if Attacker.health[0] <= 0:
		return
	
	#Header for Attacking function
	printo("\n")
	printo("---"+Attacker.name+"'s Turn---")
	
	#Player selects their attack type
	if Attacker.is_player == True:
		selection = combat_selection(Attacker,Defender)
	
	#Enemy Selection is chosen randomly
	else:
		selection = 1	
	
	#Basic Attack Calculation
	if selection == 1:
		#Calculate damage based on random range between low and high end 
		end_of_combat = basic_attack(Attacker,Defender)
		return end_of_combat
	
	elif selection == 2:
		printo("You choose to skip your turn")
		return False

	#should not reach this line
	return False

#Display's the damage from combat to the screen
def damage_display(Attacker,Defender,damage):
	printo(str(Attacker.name)+" hits "+str(Defender.name)+" for: ["+str(damage)+"] Damage with: ["+str(Attacker.weapon)+"]")
	printo(str(Defender.name)+" now has: ["+str(Defender.health[0])+"] / ["+str(Defender.health[1])+"]")
	os.system("pause")
	return 0

#Apply damage to the defending player's health
def damage_apply(Attacker,Defender, damage):
	Defender.health[0] = Defender.health[0] - damage
	#return 0 if Defender has died
	if Defender.health[0] <= 0:
		return True
	return False

def level_up(Player):
	printo("---LEVEL UP!---")
	Player.level += 1
	return 0

#Gain experience after combat based on enemy defeated
def experience(Player, Enemy):
	Player.experience += Enemy.level
	printo("Experience gain: +["+str(Enemy.level)+"]")
	printo("Experience: ["+str(Player.experience)+"/"+str(Player.experience_to_level[Player.level])+"]")
	if (Player.experience >= Player.experience_to_level[Player.level]):
		Player.experience = Player.experience - Player.experience_to_level[Player.level]
		level_up(Player)

	return 0

#Applies protection to combat 
def protection(Attacker, Defender, damage):
	if Defender.protection > 0:
		#Reduce Damage based on protection
		damage = damage - Defender.protection
		if damage < 0:
			damage = 0
	return damage

#Calculates if a critical hit occurs
def critical_hit(Attacker, Defender, damage):
	critical = randint (1,100)
	if critical > 100 - Attacker.critical:
		printo("Critical hit!")
		return damage * 2
	return damage

#Performs a basic weapon attack based on damage range
def basic_attack(Attacker, Defender):
	
	#Base Damage based on damage range
	damage = randint(Attacker.damage[0],Attacker.damage[1])

	#Apply Attacker Critical Strike
	damage = critical_hit(Attacker, Defender, damage)
	
	#Apply Defender protection
	damage = protection(Attacker, Defender,damage)
	
	#Removes health from Defender based on attack damage
	#If combat is over it will return True
	end_of_combat = damage_apply(Attacker, Defender, damage)
	
	#Display's damage output to the screen
	damage_display(Attacker, Defender, damage)
	
	game_over_check(Attacker,Defender)
	return end_of_combat

#If the player has defeated all levels of the tower
def victory_screen(Player):
	clear_screen()
	printo("You've ascended to the top of the tower.")
	printo("Victory is yours!")
	display_stats (Player)
	sys.exit()
	return 0
  
#Main is the hub that calls other functions to start the game   
def main(): 

	#Clear the screen before the game starts
	clear_screen()
	
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
main( )