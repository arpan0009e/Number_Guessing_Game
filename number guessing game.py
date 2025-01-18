#number guessing game
print ('''
Welcome you in Number Gueesing Game
''')
print('''
Instruction:
     (1) user have to input upper limit and lower limit.
     (2) lower limit and upper limit must have to contain minimum 3 diffirnce .
     (3) Computer will randomly pick a number between lower limit to upper limit .
     (4) User have only 3 chance to find out that Randomly picked  Number.
''')
import random
num1= int(input("Enter Lower limit "))
num2= int(input("Enter Upper  limit "))
n=random.randint(num1, num2)
print('''
You Have Only 3 chance
''')
found=0
for j in range (0,3):
	ruslt=int(input("Enter your guessing number "))
	print(
	2-j,'''attempt remanin''')
	if ruslt==n:
		print("Congratulation your ans is correct" )
		print ("You own the game")
		found==1
		break
	elif ruslt<n:
		print(''' 
		Hint : Your guessing number is too less 
		''')
	else :
		print ('''
		Hint : Your Gueeing number is too high 
		''')
		j=j+1
if found==0:
    print('''
    Better luck in next time
    ''')
    print('''
Randomly picked number is,''' , n)