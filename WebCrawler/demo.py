""""# url library which have methods and functions to open url
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.wikipedia.org")
# print(html.read())   here we use read to make it human readable
bs_object = BeautifulSoup(html.read(), "html.parser")
print(bs_object.title)  # include only those elements which have h1 tag"""
import os


def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating the directory' + directory)
        os.makedirs(directory)


# create_project_dir('the site')
def create_data_files(project_name, base_url):
    queue = os.path.join(project_name, 'queue.txt')
    crawled = os.path.join(project_name, 'crawled.txt')
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')  # firstly crawled file is empty


def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)


def append_to_file(path, data):
    with open(path, 'a') as f:  # opening file in append mode
        f.write(data)


def delete_file_contents(path):
    open(path, 'w').close()


def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


def set_to_file(links, file_name):
    with open(file_name, 'w') as f:
        for _ in sorted(links):
            f.write(_ + '\n')
