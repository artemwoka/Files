def read_file(file_name):
    with open(file_name, 'r') as file:
        print(file.read())
def insert_in_file(file_name, sum_, max_ ):
    with open(file_name, 'a') as file:
        file.write(f'\n{sum_}\n{max_}')
  
def readlines_file(file_name):
        with open(file_name, 'r') as file:
            list_of_file = file.readlines()
            list_to_sum = []
            for line in list_of_file:
                if line.replace('\n', '').replace('.', '').isnumeric():
                    list_to_sum.append(line.replace('\n', ''))
            list_to_sum = list(map(float, list_to_sum))
            sum_ = sum(list_to_sum)
            max_ = max(list_to_sum)
        insert_in_file(file_name, sum_, max_)
file_name = input()
readlines_file(file_name)
read_file(file_name)