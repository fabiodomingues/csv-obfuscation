# csv-obfuscation
Command-line utility to obfuscate sensitive data in CSV file.

## How to Run It

```
$ python csvobfuscation.py <input_csv_file> <column_index_to_obfuscate> [<csv_delimiter>]
```

- <input_csv_file>, input CSV file path
- <column_index_to_obfuscate>, index of the columns you want to obfuscate, separated by commas
- <csv_delimiter> (optional), column delimiter of CSV file

## Example

```
$ python csvobfuscation.py sample.csv 0,1
```