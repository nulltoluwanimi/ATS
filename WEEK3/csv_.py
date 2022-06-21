import csv

# with open('hours-worked-per-week-in-other-jobs-2018-census-csv.csv', 'r') as f:
#     read_csv = csv.reader(f)
#     for rows in read_csv:
#         print(rows)

#

with open('hours-worked-per-week-in-other-jobs-2018-census-csv.csv', 'w') as f:
    handler = csv.DictWriter(f, fieldnames=['Total', 'Money', 'Way'])
    handler.writeheader()
    handler.writerow({'Total': '100', 'Money': '30', 'Way': 'Right'})
