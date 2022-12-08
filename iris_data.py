from collections import Counter
import csv
import random

#### returns a read data in tupels from a file ####
def raw_data():
	with open('iris.data') as f:
		reader = csv.reader(f)
		#5.1,3.5,1.4,0.2,Iris-setosa
		data = [([float(i) for i in row[:-1]], row[-1]) for row in reader]
		#array of tuples: [([5.1,3.5,1.4,0.2],Iris-sector),([..]...)]
	return(data)

def train_data(all_data):
    random.shuffle(all_data)
    

#### returns the distance beetwin tow dots ####
def distance(v, w):
	#d=((x1-x2)**2+(y2-y1)**2)**.5
    return sum([(i - j)**2 for i, j in zip(v, w)])**.5

#### get's k neighbors and returns the most common neighbor ####
def majority_vote(labels):
	vote_counts = Counter(labels)
	winner, winner_count = vote_counts.most_common(1)[0]
	num_winners = len([count for count in vote_counts.values() if count == winner_count])# >> len of array whith same num of winner_count. 
	if num_winners == 1:
		return winner
	else:
		return majority_vote(labels[:-1])

#### get's a num of neighbors, list of tupels with details and name of type, array with details. returns the most common neighbor of the num of neighbors ####   
def knn_classify(k, other_data_info, location):
        by_distance = sorted(other_data_info, key=lambda lable_point: distance(lable_point[0], location))# >> [([5.1,3.5,1.4,0.2],Iris-sector),(...),...] Sorted by distance from location.
        k_nearest_labels = [label for _, label in by_distance[:k]]# >> k closes names to location.
        return majority_vote(k_nearest_labels)

#### get's the data in an array with tupels. returns the correct prophets for k neighbors #### 
def different_k(all_data):
    for k in (1, 9, 19, 27, 40):
        num_correct = 0
        for data in all_data:
            location, actual_type = data# >> [5.1,3.5,1.4,0.2], Iris-sector
            other_data_info = [other_data for other_data in all_data if other_data != data]# >> ([5.1,3.5,1.4,0.2],Iris-sector),(...),...
            iris_type = knn_classify(k, other_data_info, location)
            if iris_type == actual_type:
                num_correct += 1
        print ("for", k, "neighbor[s]:", num_correct, "correct out of", len(all_data)-1)



def main():
    all_data = raw_data()
    different_k(all_data)
    train_data(all_data)


if __name__=='__main__':
	main()

