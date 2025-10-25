
def read_file(file_name):
    with open(file_name, 'r') as file:
        print(file.read())
def insert_in_file(file_name, data):
    with open(file_name, 'a') as file:
        for i in data:
            file.write(i+'\n')
list_ = input().split()
file_name = input()
insert_in_file(file_name, list_)
read_file(file_name)