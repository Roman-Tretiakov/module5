import multiprocessing
from datetime import datetime


def read_info(file_name):
    all_data = []
    with open(file_name, 'r') as file:
        while True:
            _str = file.readline()
            if _str == '':
                break
            all_data.append(_str)


files = [f'./file {num}.txt' for num in range(1, 5)]

# Линейный вызов

start = datetime.now()
for file in files:
    read_info(file)
end = datetime.now()
print(end - start)

# Многопроцессный

if __name__ == '__main__':
    start = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, files)
    end = datetime.now()
    print(end - start)
