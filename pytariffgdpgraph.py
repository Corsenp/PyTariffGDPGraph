import plotly.express as px
import csv
import sys
import matplotlib.pyplot as plt
import random

def create_graph(country_ten):
    try:
        for country in country_ten:
            plt.scatter(country[3], country[2], label=country[0])
        plt.ylabel('GDP')
        plt.legend()
        plt.xlabel('Tariff')
        plt.show()
    except:
        print('ERROR : can\'t create graph')

def add_tariff(country_ten, country_gdp):
    for line_tariff in country_gdp:
        for line_ten in country_ten:
            if (line_tariff[1] == line_ten[1]):
                line_ten.append(line_tariff[2])

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
        sys.exit(1)

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
        sys.exit(1)

def main():

    arguments = len(sys.argv) - 1
    
    if (arguments < 2):
        print("You need at least two argument")
        sys.exit(1)
    
    country_gdp = read_csv(sys.argv[1])
    country_tariff = read_csv(sys.argv[2])

    country_ten = get_ten_countries(country_tariff)
    add_tariff(country_ten, country_gdp)
    country_ten.sort()
    print(country_ten)
    create_graph(country_ten)
    return


main()