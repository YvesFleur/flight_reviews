import csv

def data_cleaning(input, output):
    """
    To remove "❎", "|", "✅" which cannot be decoded in [input] and rewrite the cleand data into [output]
    - input: input file,
    - output: output file
"""
    # Define the set of special characters to replace
    conversion = set('❎|✅')

    with open(input, 'r', encoding='utf-8') as input_file:
        reader = csv.reader(input_file)
        output_lines = []

        for row in reader:
            new_row = [''.join('_' if c in conversion else c for c in entry) for entry in row]
            output_lines.append(new_row)

    with open(output, 'w', newline='', encoding='utf-8') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(output_lines)

