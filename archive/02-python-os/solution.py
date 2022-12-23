from urllib.request import urlretrieve
import os
os.getcwd()

# help(os.listdir)

path = "./archive/02-os/data"
dir_list = os.listdir(path)
print(dir_list)

# os.makedirs('./db', exist_ok=True)
# print(os.listdir('.'))

url1 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans1.txt'
urlretrieve(url1, path+'/file.txt')

# file read
file1 = open(path+'/file.txt', mode='r')
file1_contents = file1.read()
print(file1_contents)
file1.close()

# important functions


def parse_headers(header_line):
    return header_line.strip().split(',')


def parse_values(data_line):
    values = []
    for item in data_line.strip().split(','):
        if item == '':
            values.append(0.0)
        else:
            try:
                values.append(float(item))
            except ValueError:
                values.append(item)
    return values


def create_item_dict(values, headers):
    result = {}
    for value, header in zip(values, headers):
        result[header] = value
    return result


def read_csv(path):
    result = []
    # Open the file in read mode
    with open(path, 'r') as f:
        # Get a list of lines
        lines = f.readlines()
        # Parse the header
        headers = parse_headers(lines[0])
        # Loop over the remaining lines
        for data_line in lines[1:]:
            # Parse the values
            values = parse_values(data_line)
            # Create a dictionary using values & headers
            item_dict = create_item_dict(values, headers)
            # Add the dictionary to the result
            result.append(item_dict)
    return result


# emi
def write_csv(items, path):
    # Open the file in write mode
    with open(path, 'w') as f:
        # Return if there's nothing to write
        if len(items) == 0:
            return

        # Write the headers in the first line
        headers = list(items[0].keys())
        f.write(','.join(headers) + '\n')

        # Write one item per line
        for item in items:
            values = []
            for header in headers:
                values.append(str(item.get(header, "")))
            f.write(','.join(values) + "\n")


movies_url = "https://gist.githubusercontent.com/aakashns/afee0a407d44bbc02321993548021af9/raw/6d7473f0ac4c54aca65fc4b06ed831b8a4840190/movies.csv"

urlretrieve(movies_url, path+'/movies.csv')
movies = read_csv(path+'/movies.csv')
print(movies[0])
