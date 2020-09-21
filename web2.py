#IMPORT
import getpass
import os
import sys


#CVALUE
blue= '\33[94m'
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[32m'
cyan  = "\033[96m"
end = '\033[0m'
line=yellow+"======================================================================================================================"
space=" "
logo=red+str("""
     8888888b.   .d88888b.   .d8888b.       Y88b   d88P 
     888   Y88b d88P" "Y88b d88P  Y88b       Y88b d88P  
     888    888 888     888 888    888        Y88o88P   
     888   d88P 888     888 888        888888  Y888P    
     8888888P"  888     888 888        888888  d888b    
     888 T88b   888     888 888    888        d88888b   
     888  T88b  Y88b. .d88P Y88b  d88P       d88P Y88b  
     888   T88b  "Y88888P"   "Y8888P"       d88P   Y88b""")



os.system("clear || cls")


#HEADER
print(logo)
print(green+"\n<<<<★★★★>>>> Hello, Guys! I am Sanaur Rahman Asif. Welcome To \'\'Root Of Cyber\'\' All in One Tool. If you want to use our Tools, You have to SignUp or Login in our tool<<<★★★★>>>               ")
print(line)
print("\n")


#WHILE_INT
optcount=1
passcountn=1
uvalid=1
uvalid2=1
test=1
passchck=1
main=1
setting=1


#USER
while optcount<2:
	print(cyan+"""==» Select (1) if you want to SignUp and select (2) to Login from below.\n"""+yellow+"""\n\n  [1] SignUp \n  [2] Login\n  [3] Exit"""+end)
	try:
		opt=int(input(blue+"\n[>] Select Your Option: "+yellow))
		
#REGISTRATION
		if opt==1:
			while uvalid<2:
				unamen=str(input(blue+"\n[>] Enter a Username: "+yellow))
				uvalidchck=str(space in unamen)
				if uvalidchck=="True":
					print(red+"\n[!] Don\'t use space in the username. Try Again!")
					continue
				else:
					try:
						unamef=open(unamen,"x")
						break
					except:
						print(red+"\n[!] The usernmae has already taken. Please use another! ")
						continue
				
			while passcountn<2:
				passn=str(input(blue+"\n[>] Enter a Password: "+yellow))
				passnc=str(input(blue+"\n[?] Enter the Password Again: "+yellow))
				if passn==passnc:
					passf=open(unamen,"w")
					passf.write(passn)
					passf.close()
					break
				else:
					print(red+"\n[!] Password does not Matched. Try Again!"+end)
					passcountn-=1
			os.system('clear')
			print(logo)
			print(green+"\n\n\n\n\t     ★★★REGISTRATION COMPLETED!★★★   "+yellow+"\n\n\n[>]Now select (2) from below to Login to your account: \n")
			
#LOGIN
		elif opt==2:
			test=1
			while test<2:
				passchck=1
				os.system('clear')
				print(logo)
				print("\n\n"+line+"\n")
				print(cyan+"\n\n Enter your account\'s "+blue+"Username"+cyan+" to Login.\n If you want to go back, just press the "+yellow+"Enter"+cyan+" key.\n\n")
				unamel=str(input(blue+"\n[>] Enter Your Username:"+yellow))
				try:
					unamelf=open(unamel,"r")
					unamelfc=unamelf.readline()
					test=2
					optcount=2
					passchck=1
				except:
					os.system('clear')
					print(logo)
					print(red+"\n\n\n"+line+red+"\n\n\n\n[!] ERROR: There are no account by this username. Please enter the proper username. Or signup if you have no account.\n\n\n")
					passchck=3
					main=3
					optcount=1
					test=3
				while passchck<2:
					passl=getpass.getpass(blue+"\n[>] Enter Your Password"+yellow+" {typing hidden} "+blue+": "+yellow)
					if unamelfc==passl:
						passchck=3
						main=1
					elif passl=="":
						os.system('clear')
						print(logo)
						passchck=3
						test=1
						main=3
					else:
						os.system('clear')
						print(logo)
						print("\n"+line)
						print(red+"\n\n\t\t  [!] Wrong Password!"+cyan+"\n\n [!] If you want to go back, just press the "+green+"Enter"+cyan+" Key.\n [>] Please enter the password of "+yellow+"\'\'"+yellow+unamel+"\'\'"+cyan+" to Login.\n\n")
						passchck=1
						
#MAIN_TOOLS

					
				#starting_point
				while main<2:
						os.system('clear')
						print(logo)
						print(green+"\n\n\n   ★★★ Login Succesful! Welcome,  "+cyan+unamel+green+"! Enjoy Our Tools.★★★    ")
						print("\n"+line)
						print(cyan+"\n\n==> Select the number of the option that you want to start from below. ")
						print(yellow+"\n\n  [1] E-Mail Bombing\n  [2] G-Mail BruteForce\n  [3] Exit")
						tool=str(input(blue+"\n[>] Select Your Option :"+yellow))
						
						
#GMAIL-ATTACK
						if tool=="1":
							main=1
							import emailtool
						elif tool=="2":
							setting=1
							while setting<2:
								stin=(str(input(red+"\n[!] Server upgrading. Press "+yellow+"Enter"+red+" to go back.")))
								if stin=="":
									setting=3
								else:
									setting=1
						elif tool=="3":
							print(end)
							optcount=3
							passcountn=3
							uvalid=3
							uvalid2=3
							test=3
							passchck=3
							main=3
							setting=3
							os.system('clear')
						
						
						
						
						
						
						
						
						
		elif opt==2:
			import bforce
			

#EXIT
		elif opt==3:
			print(end)
			optcount=3
			passcountn=3
			uvalid=3
			uvalid2=3
			test=3
			passchck=3
			main=3
			setting=3
			os.system('clear')
		
#INVALID_CHECK
	except:
			os.system('clear')
			print(logo+"\n")
			print(line+"\n")
			print(red+"\n[!] You Have Entered a Wrong value. Please Enter 1 or 2 only. Try Again!\n"+end)
			optcount=1
