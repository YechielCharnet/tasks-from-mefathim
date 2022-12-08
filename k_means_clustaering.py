import csv
import random
import numpy as np

def raw_data():
	with open('iris.data') as f:
		reader = csv.reader(f)
		data = [([float(i) for i in row[:-1]]) for row in reader]
	with open('iris.data') as f:
		reader = csv.reader(f)
		labels = [(row[-1]) for row in reader]
	return data, labels
		
def random_k(data, k):
	return random.sample(data, k)

def distance(v, w):
	return sum([(i-j)**2 for i,j in zip(v,w)])**.5


#### returns the index of the closses k to point ####
def classify(means, point):
	distances = []
	for elt in means:
		distances.append(distance(elt, point))
	return np.argmin(distances), min(distances)

#### creating the clusters ####	
def clustering(data, means):
	sum_all_distances = 0
	clusters = [[] for i in means]
	for point in data:
		index, dmin = classify(means, point)
		sum_all_distances += dmin
		clusters[index].append(point)
	return clusters, sum_all_distances
		
def ceneter_m(clusters):
	cm = []
	for cluster in clusters:
#		if len(cluster) == 0:
#			continue
		a = [0,0,0,0]
		for point in cluster:
			for i in range(4):
				a[i] += point[i]
		a = [(i / len(cluster)) for i in a]
		cm.append(a)
	return cm
	
def best_means(data, means, means1):
	while means1 != means:
		clusters, sum_all_distances = clustering(data, means)
		means = ceneter_m(clusters)
		means1 = means
	return sum_all_distances, clusters
	
def variance(data, k):
	best_random = []
	best_clusters = []
	for i in range(10):
		means1 = None
		means = random_k(data, k)
		sum_all_distances, clusters = best_means(data, means, means1)
		best_random.append(sum_all_distances)
		best_clusters.append(clusters)
	index = np.argmin(best_random)
	return best_clusters[index]
	

def test(data, labels, best_clusters):
	types = list(set(labels))
	accuracy_results = [[0]*len(best_clusters) for i in range(len(types))]
	for i in range(len(best_clusters)):
		for point in best_clusters[i]:
			accuracy_results[types.index(labels[data.index(point)])][i] += 1
	for i in range(len(accuracy_results)):
		print(accuracy_results[i])
	

	
def main():
	k = 3
	data, labels = raw_data()
	best_clusters = variance(data, k)
	test(data, labels, best_clusters)
	
	
if __name__=='__main__':
	main()
