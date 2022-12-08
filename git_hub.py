import json
from urllib.request import urlopen
from tqdm import tqdm
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def repository(stars, forks, page):
    with urlopen(f'https://api.github.com/search/repositories?q=tetris+language:assembly&sort=stars&order=desc&per_page=100&page={page}') as data:
        repo = json.load(data)
        pop_items = repo.pop('items')
        for item in pop_items:
            stars.append(item.pop('stargazers_count'))
            forks.append(item.pop('forks'))
    return

def main():
    stars = []
    forks = []
    page = 10
    maine_page = 1
    while maine_page <= page:
        repository(stars, forks, maine_page)
        maine_page = maine_page+1
    x_stars = np.array([stars]).reshape((-1, 1))
    y_forks = np.array([forks])
    avgx = np.mean(x_stars)
    avgy = np.mean(y_forks)
    m = (np.sum((x_stars-avgx)*(y_forks-avgy)))/(np.sum((x_stars-avgx)*(x_stars-avgx)))
    b = avgy - m*avgx
    x_line = x_stars
    y_line = m*x_stars + b
    	
    plt.scatter(x_stars, y_forks)
    plt.plot(x_line, y_line)
    plt.show()

if __name__=='__main__':
    main()



