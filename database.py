import sys

def exist(ID):
	searchFor = '^' + ID + '^'
	if searchFor in open('.database').read():
		return True
	return False

def getName():
	inputName = input('Enter name: ')
	name = ''
	for i in inputName:
		if i == ' ':
			name += '@'
		else:
			name += i
			
	return name

def getUserID():
	userID = ''
	inputID = input('Enter userID: ')
	for i in inputID:
		if i == ' ':
			pass
		else:
			userID += i

	userExists = exist(userID)

	if userExists:
		return ''
	else:
		return userID

def getPassword():
	password = input('Enter password: ')
	for i in password:
		if i == ' ':
			sys.exit('Password should not contain spaces.')
	return password

print('Welcome to secure city.\n')
print('Press 1 to sign up.\nPress 2 to log in.')

choice = input(': ')

if choice == '1':

	name = getName()
	userID = getUserID()
	if userID == '':
		sys.exit('This ID already exists, try to log in.')
		
	password = getPassword()


	saveData = open('.database', 'a')
	data = name + '^' + userID + '^' + password + '\n'

	saveData.write(data)

	print('Your account is successfully created.')
	print(name, userID)

elif choice == '2':
	userID = input('Enter userID: ')
	password = input('Enter password: ')
	search = '^' + userID + '^' + password
	# search in database file and print user's name	
	with open('.database', 'r') as fileRead:
		for j in fileRead:
			FileContent = fileRead.readline()
			if search in FileContent:
				break
	toPrint = ''
	for i in FileContent:
		if i == '^':	# '^' is used to separate name, id and password
			toPrint += ' '
		elif i == '@':	# '@' is used instead of spaces in name
			toPrint += ' '
		else:
			toPrint += i
	
	print(toPrint)

