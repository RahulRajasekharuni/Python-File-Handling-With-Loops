def main():
	member_reader()
	rule_reader()
	readable_rules()
#Gives user some feedback.
	print('Processing Complete')
	
def member_reader():
	try:
#These variables are accessed by other functions and therefore cannot be local.
		global header
		global member_counter
		global age
		global winloss
		global login
		global gender
		global income
		header = ''
#check if Members.txt exists
		memberfile = open('Members.txt', 'r')
	
	#Counts the number of members in members file minus the header lines.
		member_counter = sum(1 for line in open('Members.txt')) - 2
		age = [0]*member_counter
		winloss = [0]*member_counter
		login = [0]*member_counter
		gender = [0]*member_counter
		income = [0]*member_counter
	#List declaration for each paramater used to compare members to the rules.
		counter = 0

#stores header in string variable
		for line in range(2):
			header += memberfile.readline()
	
#retrieves age, winloss, login, gender and income from members file	
		for line in memberfile:
			age[counter]=line[0:2]
			winloss[counter]=line[4]
			login[counter]=line[7:10]
			if line[12] =='M':
				gender[counter]=line[12:16]
			else:
				gender[counter]=line[12:18]
			if gender[counter] == 'Male':
				income[counter] = line[18:23]
			else:
				income[counter] = line[20:25]
			counter += 1
							
		memberfile.close()
	except IOError:
		print('Members.txt does not exist')
	except:
		print('error')
	
def rule_reader():
	counter = 0
	print_counter=0
	try:
		print_string = ['']*member_counter
	except IOError:
		print('Members.txt does not exist')
	except:
		print('error')
	member_report = open('MemberReport.txt','w')
#while the loop counter is less than the number of members
	try:
		while counter < member_counter:
			rulefile = open('Rules.txt', 'r')
#for each line in the rules file check which rule the member belongs to and save that data to a string list
			for line in rulefile:
				if line[0:5] == 'GE,25' and line[7:11] == 'GE,8' and line[13] == '-' and line[16] == 'M':
					if int(age[counter])>25 and int(winloss[counter]) > 8 and gender[counter] == 'Male':
						print_string[counter] = age[counter]+'\t\t'+winloss[counter]+'\t\t'+login[counter]+'\t\t'+gender[counter]+'\t\t'+ income[counter] + '\t\t' + 'Continue'
				if line[0:5] == 'GE,25' and line[7:11] == 'LT,8' and line[13] == '-' and line[16] == 'M':
					if int(age[counter])>25 and int(winloss[counter]) < 8 and gender[counter] == 'Male':
						print_string[counter] = age[counter]+'\t\t'+winloss[counter]+'\t\t'+login[counter]+'\t\t'+gender[counter]+'\t\t'+ income[counter] + '\t\t' + 'Discontinue'
				if line[0:5] == 'GE,25' and line[7] == '-' and line[10] == '-' and line[13] == 'F':
					if int(age[counter])>25 and gender[counter] == 'Female':
						print_string[counter] = age[counter]+'\t\t'+winloss[counter]+'\t\t'+login[counter]+'\t\t'+gender[counter]+'\t\t'+ income[counter] + '\t\t' + 'Discontinue'
				if line[0:5] == 'LT,25' and line[7] == '-' and line[10:16] == 'GE,150' and line[18] == '-':
					if int(age[counter])<25 and int(login[counter]) > 150:
						print_string[counter] = age[counter]+'\t\t'+winloss[counter]+'\t\t'+login[counter]+'\t\t'+gender[counter]+'\t\t'+ income[counter] + '\t\t' + 'Continue'
				if line[0:5] == 'LT,25' and line[7:11] == 'GE,5' and line[13:19] == 'LT,150' and line[21] == '-':
					if int(age[counter])<25 and int(winloss[counter]) > 5 and int(login[counter]) <150:
						print_string[counter] = age[counter]+'\t\t'+winloss[counter]+'\t\t'+login[counter]+'\t\t'+gender[counter]+'\t\t'+ income[counter] + '\t\t' + 'Continue'
				if line[0:5] == 'LT,25' and line[7:11] == 'LT,5' and line[13:19] == 'LT,150' and line[21] == '-':
					if int(age[counter])<25 and int(winloss[counter]) < 5 and int(login[counter]) < 150:
						print_string[counter] = age[counter]+'\t\t'+winloss[counter]+'\t\t'+login[counter]+'\t\t'+gender[counter]+'\t\t'+ income[counter] + '\t\t' + 'Discontinue'		
			counter += 1
#file opened and closed in while loop to ensure each member is checked against each rule
			rulefile.close()
#write header to MemberReport.txt		
		member_report.write(header)
#print contents of print_string list to MemberReport.txt file	
		while print_counter < member_counter:
			if print_counter > 0:
				member_report.write('\n')
			member_report.write(print_string[print_counter])
			print_counter+=1
			
		member_report.close()			
	except IOError:
		print('file does not exist')
	except:
		print('error')
					
def readable_rules():
	try:
		rulefile = open('Rules.txt', 'r')
		readrulesfile = open('ReadableRules.txt','w')
	#Each line in rulefile is checked and more readable rule text is written to ReadableRules.txt	
		for line in rulefile:
			if line[0:5] == 'GE,25' and line[7:11] == 'GE,8' and line[13] == '-' and line[16] == 'M':
				readrulesfile.write('Rule 1: If Age >= '+line[3:5]+' & Win-Loss >= '+line[10]+' & Gender = '+line[16:20]+' --> Continue.')
			if line[0:5] == 'GE,25' and line[7:11] == 'LT,8' and line[13] == '-' and line[16] == 'M':
				readrulesfile.write('\nRule 2: If Age >= '+line[3:5]+' & Win-Loss < '+line[10]+' & Gender = '+line[16:20]+' --> Discontinue.')
			if line[0:5] == 'GE,25' and line[7] == '-' and line[10] == '-' and line[13] == 'F':
				readrulesfile.write('\nRule 3: If Age >= '+line[3:5]+' & Gender = '+line[13:19]+' --> Discontinue.')
			if line[0:5] == 'LT,25' and line[7] == '-' and line[10:16] == 'GE,150' and line[18] == '-':
				readrulesfile.write('\nRule 4: If Age < '+line[3:5]+' & Log-in >= '+line[13:16]+' --> Continue.')		
			if line[0:5] == 'LT,25' and line[7:11] == 'GE,5' and line[13:19] == 'LT,150' and line[21] == '-':
				readrulesfile.write('\nRule 5: If Age < '+line[3:5]+' & Win-Loss >= '+line[10]+' & Log-in < '+line[16:19]+' --> Continue.')
			if line[0:5] == 'LT,25' and line[7:11] == 'LT,5' and line[13:19] == 'LT,150' and line[21] == '-':
				readrulesfile.write('\nRule 6: If Age < '+line[3:5]+' & Win-Loss < '+line[10]+' & Log-in < '+line[16:19]+' --> Discontinue.')			
		rulefile.close()
		readrulesfile.close()		
	except IOError:
		print('Rules.txt does not exist')
	except:
		print('error')
				
main()
input()	
