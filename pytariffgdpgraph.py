import plotly.express as px
import csv
import sys
import random

def add_tariff(Country_gdp, csv_name):
    print("tariff")

def read_csv(csv_name):
    csv_list = []
    try:
        with open(csv_name, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for line in csv_reader:
                if not line[2]:
                    continue
                csv_list.append(line)
        
        return csv_list
    
    except:
        print("ERROR : can't open file")
        exit

def get_ten_countries(countries):
    countries_random = [] 
    i = 0
    try:
        while i < 10:
            country = random.choice(countries)
            countries_random.append(country)
            i = i + 1
            
        return countries_random

    except:
        print("ERROR : couldn't pick 10 random countries")

def main():

    arguments = len(sys.argv) - 1
    
    if (arguments < 2):
        print("You need at least two argument")
        return 1
    
    country_gdp = read_csv(sys.argv[1])

    print(get_ten_countries(country_gdp))
    return

main()