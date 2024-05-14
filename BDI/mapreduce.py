from itertools import groupby

# Mapper function
def mapper(_, line):
    words = line.split()
    for word in words:
        yield (word, 1)

# Reducer function
def reducer(key, values):
    yield (key, sum(values))

# Ask for the file name
file_name = input("Enter the name of the text file (including extension): ")

# MapReduce job
mapped_results = []
with open(file_name, 'rb') as file:
    # Read the content of the file using UTF-16LE encoding
    input_text = file.read().decode('utf-16le', errors='ignore').splitlines()

for paragraph in input_text:
    mapped_results.extend(mapper(None, paragraph))

mapped_results.sort(key=lambda x: x[0])

reduced_results = []
for key, group in groupby(mapped_results, lambda x: x[0]):
    values = [x[1] for x in group]
    reduced_results.extend(reducer(key, values))

# Print the result
for result in reduced_results:
    print(result)
