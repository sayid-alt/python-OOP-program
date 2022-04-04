from numpy import random

class Player:
	def __init__(self, name, health, armor, attackPower):
		self.name = name
		self.health = health
		self.armor = armor
		self.attackPower = attackPower
	
	def status(self):
		print("----- status of " + self.name + " -----")
		print("name\t\t: ", self.name)
		print("health\t\t: ", self.health)
		print("armor\t\t: ", self.armor)
		print("attack power\t: ", self.attackPower)

	
	def attack(self, enemy):
		print(self.name + " attack " + enemy.name)
		enemy.attacked_by(self)
	
	def attacked_by(self, enemyAttack):
		print(self.name + " attacked by " + enemyAttack.name)	
		power_attack = enemyAttack.attackPower/self.armor
		self.health = self.health - power_attack
		print("power attack of " + enemyAttack.name + " = " + str(power_attack))
		print("health remaining of " + self.name + " = " + str(self.health))
	
	

p1 = Player("Joma", 100, 20, 10)
p2 = Player("Kolo", 100, 20, 10)

p1.status()
p2.status()

print("\n----- Fight field ------")
p1Attack = 0
p2Attack = 0
while(True):
	attack_p1 = 0
	attack_p2 = 1
	random_number = random.choice([0,1])
	if random_number == 0:
		print("----------------------")
		print("random : " + str(random_number))
		p1.attack(p2)
		p1Attack += 1
	else:
		print("----------------------")
		print("random : " + str(random_number))
		p2.attack(p1)
		p2Attack += 1
	
	if p1.health == 0 or p2.health == 0:
		break

print("\n==== Final Result ====")
if p1.health == 0:
	print(p2.name + " is winner")
else:
	print(p1.name + " is winner")

print(p1.name, "'s total attack: ", p1Attack)
print(p2.name, "'s total attack: ", p2Attack)