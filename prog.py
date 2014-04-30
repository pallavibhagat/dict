import csv

def main():
    reader = csv.DictReader(open("dic.csv", "rb"))
    for row in reader:
        print row

if __name__ == "__main__":
    main()
