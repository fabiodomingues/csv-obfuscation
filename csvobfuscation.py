"""
Usage:
    python csvobfuscation.py <input_csv_file> <column_index_to_obfuscate> [<csv_delimiter>]

Author:
    Fabio Domingues (contato@fabiodomingues.com)
"""

import sys
import csv
import hashlib

def obfuscate(input_csv_file, output_csv_file, csv_delimiter, column_index_to_obfuscate):
    with open(output_csv_file, mode='w') as output_file:
        csv_writer = csv.writer(output_file, delimiter=csv_delimiter)

        with open(input_csv_file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=csv_delimiter)
            line_count = 0

            for row in csv_reader:
                if line_count == 0:
                    csv_writer.writerow(row)
                else:
                    currentColumnIndex = 0
                    newRow = []

                    for column in row:
                        if currentColumnIndex in column_index_to_obfuscate:
                            m = hashlib.md5()
                            m.update(column)
                            column = m.hexdigest()

                        newRow.append(column)
                        currentColumnIndex += 1
                    csv_writer.writerow(newRow)
                line_count += 1

def main():
    input_csv_file = sys.argv[1]
    column_index_to_obfuscate = map(int, sys.argv[2].split(","))
    csv_delimiter = (sys.argv[3] if len(sys.argv) > 3 else ",")

    obfuscate(input_csv_file, "output.csv", csv_delimiter, column_index_to_obfuscate)

if __name__ == '__main__':
    main()