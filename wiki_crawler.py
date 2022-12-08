from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from pathlib import Path
import os
from tqdm import tqdm
import urllib.request
import sys
import random

def url_parser(main_url):
    with urlopen(main_url) as ourl:
        read = ourl.read()
        parser = bs(read, 'html.parser')
    return parser

def image_urls(parser):
    img_urls = set()
    imgs = parser.find_all('img')
    for img in imgs:
        img_src = img.get('src')
        if img_src.startswith('//'):
            img_urls.add(f'https:{img_src}')
        else:
            img_urls.add(f'https://en.wikipedia.org{img_src}')
    return img_urls

def creat_folder(name):
    Path(name).mkdir(exist_ok=True)
    os.chdir(name)

def download_img(img_urls):
	for a,i in tqdm(enumerate(img_urls)):
#		if a == 10:
#			break
		try:
			urllib.request.urlretrieve(i, f"{a}.jpg")
		except:
			print(i)

def width_links(parser, width):
    links = []
    link = parser.find_all('a', href = True)
    for i in link:
        tag = i.get('href')
        if tag.startswith('/wiki/'):
            links.append(f'https://en.wikipedia.org{tag}')
        else:
            continue
    return random.choices(links, k=width)
    
def download_img_width(parser, width, dipth):
	for i in width_links(parser, width):
		main_url = i
		a = i.split('/')
		name = a[-1]
		parser = url_parser(main_url)
		img_urls = image_urls(parser)
		creat_folder(name)
		download_img(img_urls)
#		if dipth > 0:
#			while dipth > 0:
#				
#				dipth -= 1
		os.chdir('..')
    

def main():
    main_url = sys.argv[1] # https://en.wikipedia.org/wiki/Chess
    if not main_url.startswith('https://en.wikipedia.org/wiki/'):
    	print('arg[1] supposed start with: https://en.wikipedia.org/wiki/')
    name = 'chess'
    width = int(sys.argv[2])
    dipth = int(sys.argv[3])

    parser = url_parser(main_url)
    img_urls = image_urls(parser)
    creat_folder(name)
    download_img(img_urls)
    
    if width > 0:
    	download_img_width(parser, width, dipth)

if __name__=='__main__':
    main()

