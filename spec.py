import csv
import sys

# load data

# clothing 
clothing = []

with open('data/speccloth.csv') as f:
	reader = csv.reader(f)
	for row in reader:
		clothing.append(row)

# headgear 
headgear = []

with open('data/spechgear.csv') as f:
	reader = csv.reader(f)
	for row in reader:
		headgear.append(row)
		
# shoes
shoes = []

with open('data/specshoes.csv') as f:
	reader = csv.reader(f)
	for row in reader:
		shoes.append(row)
		
# brand
brand = {}

with open('data/specbrand.csv') as f:
	reader = csv.reader(f)
	for row in reader:
		#brand.append(Brand(row))
		brand[row[0]] = Brand(row)
		
class Brand:
	def __init__(self,args):
		self.name = args[0]
		self.boon = args[1]
		self.bane = args[2]
		
def handle_args(arg):
	
	argv = arg
	
	for i in range(len(argv)):
		if argv[i] == 'mpu':
			argv[i] = 'Main Power Up'
			
		elif argv[i] == 'spu':
			argv[i] = 'Sub Power Up'
		
		elif argv[i] == 'iss':
			argv[i] = 'Ink Saver (Sub)'
		
		elif argv[i] == 'spu':
			argv[i] = 'Special Power Up'
		
		elif argv[i] == 'bdu':
			argv[i] = 'Bomb Defense Up DX'
		
		elif argv[i] == 'ssu':
			argv[i] = 'Swim Speed Up'
		
		elif argv[i] == 'rsu':
			argv[i] = 'Run Speed Up'
		
		elif argv[i] == 'qr':
			argv[i] = 'Quick Respawn'
		
		elif argv[i] == 'ism':
			argv[i] = 'Ink Saver (Main)'
		
		elif argv[i] == 'irsu':
			argv[i] = 'Ink Resistance Up'
		
		elif argv[i] == 'scu':
			argv[i] = 'Special Charge Up'
		
		elif argv[i] == 'ircu':
			argv[i] = 'Ink Recharge Up'
		
		elif argv[i] == 'ss':
			argv[i] = 'Special Saver'
		
		elif argv[i] == 'qsj':
			argv[i] = 'Quick Super Jump'
			
	
	while len(argv) < 5:
		argv.append(argv[-1])
	
	return argv[1:];
	
def compare(a,b):
	if a.strip().lower() == b.strip().lower():
		return True
	else:
		return False
	
def optimise(argv):
	optimal = []
	
	options = []
	
	for i in clothing: 
		if compare(i[4],argv[0]): 
			options.append(i)
	
	for i in headgear: 
		if compare(i[4],argv[0]): 
			options.append(i)
	
	for i in shoes: 
		if compare(i[4],argv[0]): 
			options.append(i)
			
	duplicate = 0
			
	for i in range(1,len(argv)):
		for j in range(1,len(argv)):
			if i == j:
				continue
			if argv[i] == argv[j]:
				duplicate = argv[i]
				
	if duplicate:
		for i in options:
			if 

def main():
	
	if len(sys.argv) < 2:
		print('Invalid Arguments! Correct Usage: ')
		print('python spec.py main sub [sub] [sub]')
	
	argv = handle_args(sys.argv)
	
	opt = optimise(argv)
	
if __name__ == '__main__':
	main()