import csv

# with open('hours-worked-per-week-in-other-jobs-2018-census-csv.csv', 'r') as f:
#     read_csv = csv.reader(f)
#     for rows in read_csv:
#         print(rows)

#

with open('hours-worked-per-week-in-other-jobs-2018-census-csv.csv' , 'r') as f:
    handler = csv.Reader(f)
    for rows in handler:
        print(rows)