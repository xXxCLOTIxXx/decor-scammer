from os import system as s
from random import choice
try:import AminoXZ
except:s("pip install AminoXZ");import AminoXZ
try:from colored import fore
except:s("pip install colored");from colored import fore
client = AminoXZ.Client()
s("cls")
print(fore.MEDIUM_PURPLE_4, """

██████╗░███████╗░█████╗░░█████╗░██████╗░
██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗
██║░░██║█████╗░░██║░░╚═╝██║░░██║██████╔╝
██║░░██║██╔══╝░░██║░░██╗██║░░██║██╔══██╗
██████╔╝███████╗╚█████╔╝╚█████╔╝██║░░██║
╚═════╝░╚══════╝░╚════╝░░╚════╝░╚═╝░░╚═╝

░██████╗░█████╗░░█████╗░███╗░░░███╗███╗░░░███╗███████╗██████╗░
██╔════╝██╔══██╗██╔══██╗████╗░████║████╗░████║██╔════╝██╔══██╗
╚█████╗░██║░░╚═╝███████║██╔████╔██║██╔████╔██║█████╗░░██████╔╝
░╚═══██╗██║░░██╗██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░██╔══██╗
██████╔╝╚█████╔╝██║░░██║██║░╚═╝░██║██║░╚═╝░██║███████╗██║░░██║
╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝
	
	Made by Xsarz (@DXsarz)
	GitHub: https://github.com/xXxCLOTIxXx
	Telegram channel: https://t.me/DxsarzUnion
	YouTube: https://www.youtube.com/channel/UCNKEgQmAvt6dD7jeMLpte9Q

	""", fore.GREY_63)

def name_generator(num: int = 8):
	g = ""
	for x in range(num):
		g = g + choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
	return g

def profile_design():
	while True:
		try:
			link_info = client.get_from_link(input("User Link>> "))['extensions']['linkInfo']
			info = client.get_user_info(userId=link_info['objectId'], comId=link_info['ndcId'])
			name = info["nickname"]
			icon = info["icon"]
			try:background = info["extensions"]["style"]["backgroundMediaList"][1]
			except: background = "None"
			try:content = info["content"]
			except:content = "None"
			try:mediaList = info["mediaList"]
			except: mediaList = "None"
			break
		except Exception as error:print(fore.RED, f"Error. Maybe you didn't link to the community:\n{error}\n", fore.GREY_63)
	total = f'Name: {name}\nIcon: {icon}\nBackground image: {background}\nContent:\n\n{content}\nMedia List: {mediaList}'
	file_name = f"profile_{name_generator()}.txt"
	file = open(file_name, "w+", encoding="utf-8")
	file.write(total)
	print(fore.GREEN, f'Design saved to file "{file_name}"', fore.GREY_63)


def community_design():
	while True:
		try:
			info = client.get_from_link(input("Community Link>> "))["extensions"]["community"]
			name = info['name']
			icon = info['icon']
			content = info['content']
			mediaList = ['mediaList']
			break
		except Exception as error:print(fore.RED, f"Error. Maybe you didn't link to the profile:\n{error}\n", fore.GREY_63)
	total = f'Community Name: {name}\nCommunity icon: {icon}\nCommunity Description:\n\n{content}\n\nMedia list:\n {str(mediaList)}\n\n\n{info}'
	file_name = f"community_{name_generator()}.txt"
	file = open(file_name, "w+", encoding="utf-8")
	file.write(total)
	print(fore.GREEN, f'Design saved to file "{file_name}"', fore.GREY_63)


def chat_design():
	while True:
		try:
			link_info = client.get_from_link(input("Chat Link>> "))['extensions']['linkInfo']
			chat_info = client.get_chat_thread(comId=link_info['ndcId'], chatId=link_info['objectId'])
			name = chat_info['title']
			icon = chat_info['icon']
			try:chatContent = chat_info['content']
			except:chatContent = None
			try:chatBackground = chat_info['extensions']['bm'][1]
			except:chatBackground = None
			break
		except Exception as error:print(fore.RED, f"Error. Maybe you didn't link to the chat:\n{error}\n", fore.GREY_63)
	total = f'Name: {name}\nIcon: {icon}\nContent:\n\n{chatContent}\n\nChat background: {chatBackground}'
	file_name = f"chat_{name_generator()}.txt"
	file = open(file_name, "w+", encoding="utf-8")
	file.write(total)
	print(fore.GREEN, f'Design saved to file "{file_name}"', fore.GREY_63)




while True:
	print("\n1)Profile design\n2)Community Design\n3)Chat design\n")
	select = input("Design type>> ")
	if select == '1':profile_design()
	elif select == '2':community_design()
	elif select == '3':chat_design()
	else:print(fore.RED, "\nError, select 1 or 2 or 3\n", fore.GREY_63)