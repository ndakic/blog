import csv

OUTPUT_FILE = "output.csv"
OUTPUT_HEADER = "Index,Organization Id,Name,Website,Country,Description,Founded,Industry,Number of employees\n"
SOME_LARGE_FILE = "organizations-2000000.csv"


def read_large_csv_file(file_path):
    with open(file_path, 'r') as file:
        csvreader = csv.reader(file)
        next(csvreader)  # skip the header
        for line in csvreader:
            yield line


if __name__ == "__main__":
    organizations = read_large_csv_file(SOME_LARGE_FILE)  # generator object
    with open(OUTPUT_FILE, "wt", encoding="utf-8") as output:
        output.write(OUTPUT_HEADER)
        for organization in organizations:
            if int(organization[8]) >= 9900:  # do some filtering
                output.write(f"{','.join(organization)}\n")
