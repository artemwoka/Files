def read_file(file_name):
    with open(file_name, 'r') as file:
        print(file.read())
def insert_in_file(file_name, sum_, max_ ):
    with open(file_name, 'a') as file:
        file.write(f'\n{sum_}\n{max_}')
  

def readlines_file(file_name):
        with open(file_name, 'r') as file:
            list_of_file = list(map(lambda x: x.replace('\n', ''),file.readlines()))
            list_of_file = list(map(int,list_of_file))
            sum_ = sum(list_of_file)
            max_ = max(list_of_file)
        insert_in_file(file_name, sum_, max_)

file_name = input()
readlines_file(file_name)
read_file(file_name)
