import json
from urllib.request import urlopen
import csv
from tqdm import tqdm

def get_ids():
    with urlopen('https://hacker-news.firebaseio.com/v0/jobstories.json?print=pretty') as data:
        job_ids = json.loads(data.read())
    return job_ids

def get_jobs(id_job):
    with urlopen(f'https://hacker-news.firebaseio.com/v0/item/{id_job}.json?print=pretty') as job:
        json_obj = json.loads(job.read())
    return json_obj

def get_all_jobs(ids):
    all_jobs = [] 
    for id_job in tqdm(ids):
        this_job = get_jobs(id_job)
        clean_job = [this_job.pop('id',None),this_job.pop('type',None)]
        all_jobs.append(clean_job)
    return all_jobs 

def write_to_csv(name_file, data):
    with open(name_file, 'w') as path:
        writer = csv.writer(path)
        for row in data:
            writer.writerow(row)

def main():
    name_file =  input("Enter file name: ")
    ids = get_ids()
    data = get_all_jobs(ids)
    write_to_csv(name_file, data)

if __name__=='__main__':
    main()


