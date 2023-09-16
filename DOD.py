import os,platform
os.system('git pull')
os.system('touch proxies.txt')
DOD=platform.architecture()[0]

if DOD=="32bit":

	

	print('\n \033[1;32m [×] \033[1;33mSorry Bro Your Device 32bit \n \033[1;32m [√] \033[1;31mThis Tool 32Bits Device Not Supported')

elif DOD=="64bit":

	

    __import__("dod")