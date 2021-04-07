from art import *
from termcolor import colored
import subprocess
subprocess.call('', shell=True)
import os
import sys
import youtube_dl


def clss():
	os.system('cls' if os.name=='nt' else 'clear')




def main():
	clss()
	print(colored(text2art("YTB  Download"),'red'))
	print(colored('Created by Cucus\n\n\n'.center(143),'cyan'))


def downl():
	
	urll = input("Veuillez enter l'url complète de la vidéo en question\n\n--> ")


	ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})

	with ydl:
	    result = ydl.extract_info(
	        urll, #Ici c'est l'url en strings
	        download=True
	    )

	if 'entries' in result:
	    # Si c'est une playlist
	    video = result['entries'][0]
	else:
	    # Si c'est juste une vidéo
	    video = result

	video_url = video['url']
	print(video_url)
	print("\n\n\n")



if __name__ == '__main__':
	main()