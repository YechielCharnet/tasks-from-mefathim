import csv
import random


def open_data():
    data = []
    with open('agaricus-lepiota.data') as f:
        file_data = csv.reader(f)
        for i in file_data:
            data.append(i)
        random.shuffle(data)
    return(data)

def separator(data):
    idx_type = [i[0] for i in data]
    idx_details = [i[1:] for i in data]
    types = []
    for i in range(22):
        t = []
        for j in range(len(idx_details)):
            t.append(idx_details[j][i])
        types.append(set(t))
    return idx_type, idx_details, types

def creat_dictionary(types):
    dictionary = {}
    for i in range(len(types)):
        dictionary[i] = {}
        for t in types[i]:
            dictionary[i][t] = [0,0]
    return dictionary

def train_test(idx_details):
    train_data, test_data = idx_details[:int(len(idx_details)*0.8)], idx_details[int(len(idx_details)*0.8):]
    return train_data, test_data

def count_attribute(dictionary, train_data, idx_type):
    for i in range(len(train_data)):
        for j in range(22):
            attribute = train_data[i][j]
            dictionary[j][attribute][0 if idx_type[i] == 'p' else 1] +=1

def sum_poisonous(idx_type, train_data):
	sum_poisonous = sum_non_poisonous = 0
	for i in range(len(train_data)):
		if idx_type[i] == 'p':
			sum_poisonous += 1
		else:
			sum_non_poisonous += 1
	return sum_poisonous, sum_non_poisonous

def attributes_probability(dictionary, sum_poisonous_1, sum_non_poisonous):
    k = 0.5
    probabilities = [0]*(22)
    for i in range(22):
        probabilities[i] = []
        for j, (poisonous, non_poisonous) in dictionary[i].items():
            probabilities[i].append((j, (poisonous + k) / (sum_poisonous_1 + 2 * k), (non_poisonous + k) / (sum_non_poisonous + 2 * k)))
    return probabilities


def main():
    data = open_data()
    idx_type, idx_details, types = separator(data)
    dictionary = creat_dictionary(types)
    train_data, test_data = train_test(idx_details)
    count_attribute(dictionary, train_data, idx_type)
    sum_poisonous_1, sum_non_poisonous = sum_poisonous(idx_type, train_data)
    types_probability = attributes_probability(dictionary, sum_poisonous_1, sum_non_poisonous)


if __name__=='__main__':
    main()
