# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 11:44:02 2023

@author: diguitarrista
"""

# In[ ] Libraries

import csv
import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# In[ ] Converting a xlsx file to csv using pandas

# Convert the file
input_excel_file ="pokemon_kanto_v1_exc.xlsx"

# Reading an excel file
excel_file = pd.read_excel(input_excel_file)

# Converting excel file into CSV file
excel_file.to_csv ("pokemon_kanto_v1_csv.csv", index = None, header=True)

# Reading and Converting the output csv file into a dataframe object
pokedex = pd.DataFrame(pd.read_csv("pokemon_kanto_v1_csv.csv"))

    
# In[ ] Merge two columns

# Read the CSV file into a DataFrame
df = pd.read_csv('pokemon_kanto_v1_csv.csv')

# Specify the columns to be merged
column1 = 'Type 1'  # Replace with the actual name of the first column
column2 = 'Type 2'  # Replace with the actual name of the second column

# Convert NaN values in column2 to empty string
df[column2].fillna('', inplace=True)

# Convert NaN values in column2 to empty string
df[column2].fillna('', inplace=True)

# Merge column2 into column1
df[column1] = df[column1] + ' ' + df[column2]

# Drop column2
df.drop(column2, axis=1, inplace=True)

# Remove trailing spaces from the 'Type' column
df[column1] = df[column1].str.rstrip()

# Rename column1 to 'Type'
df.rename(columns={column1: 'Type'}, inplace=True)

# Write the updated DataFrame back to a CSV file
df.to_csv('pokemon_kanto_v2_csv.csv', index=False)

# In[ ] "Pokedex" Iterate through the csv file

def find_pokemon():
    # Load the CSV file
    with open('pokemon_kanto_v2_csv.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        # User input for Pokemon name
        pokemon_name = input("Enter the name of the Pokemon from Kanto Region: ")
        found = False
        # Iterate through each row in the CSV file
        for row in csv_reader:
            # Check if the Pokemon name matches
            if row['Pokemon'].lower() == pokemon_name.lower():
                # Retrieve the type and status information
                pokemon_type = row['Type']
                pokemon_hp = row['HP']
                pokemon_attack = row['Attack']
                pokemon_defense = row['Defense']
                pokemon_speed = row['Speed']
                pokemon_special = row['Special']
                # Print the retrieved information
                print(f"Type: {pokemon_type}")
                print(f"HP: {pokemon_hp}")
                print(f"Attack: {pokemon_attack}")
                print(f"Defense: {pokemon_defense}")
                print(f"Speed: {pokemon_speed}")
                print(f"Special: {pokemon_special}")
                found = True
                break
        if not found:
            print("Pokemon not found.")

# In[ ] "Pokedex" Iterate through the csv file

def best_status():
    # Define the attribute options
    attribute_options = ['HP', 'Attack', 'Defense', 'Special', 'Speed']

    # Take user input for the attribute
    while True:
        attribute = input(f"Enter the attribute ({', '.join(attribute_options)}): ")
        if attribute in attribute_options:
            break
        else:
            print("Invalid attribute. Please try again.")

    highest_value = 0
    highest_value_pokemon = None

    # Load the CSV file
    with open('pokemon_kanto_v2_csv.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        # Iterate through each row in the CSV file
        for row in csv_reader:
            # Retrieve the value of the chosen attribute for the current Pokemon
            pokemon_value = int(row[attribute])
            # Compare the current value with the highest value so far
            if pokemon_value > highest_value:
                highest_value = pokemon_value
                highest_value_pokemon = row['Pokemon']

    # Print the Pokemon with the highest value for the chosen attribute
    print(f"The Pokemon with the highest {attribute} is: {highest_value_pokemon} with {attribute} {highest_value}")
        
# In[ ] Plotting the data

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv('pokemon_kanto_v2_csv.csv')

# Extract HP and Attack columns from the DataFrame
hp = df['HP']
attack = df['Attack']
defense = df['Defense']
speed = df['Speed']
special = df['Special']

# Create a scatter plot of HP vs Attack
plt.scatter(attack, hp, s = 5, color="red")

# Add labels and title
plt.xlabel('Attack')
plt.ylabel('HP')
plt.title('HP x Attack')

# Show the plot
plt.show()

# In[ ] Iterate through the csv file and plot the data

# Open the CSV file
with open('pokemon_kanto_v2_csv.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    type_counts = {}  # Dictionary to store type counts

    # Iterate through each row in the CSV file
    for row in reader:
        pokemon_types = row['Type'].split(' ')  # Split types by space
        # Ignore rows with NaN values in the 'Type' column
        for pokemon_type in pokemon_types:
            pokemon_type = pokemon_type.strip()  # Remove leading/trailing whitespaces
            # Iterate through each type in the list
            if pokemon_type:
                # If the type is already in the dictionary, increment the count by 1
                if pokemon_type in type_counts and pokemon_type != 'nan':
                    type_counts[pokemon_type] += 1
                # Otherwise, add the type to the dictionary with count 1
                else:
                    type_counts[pokemon_type] = 1

# Create a bar chart of type counts with custom colors
types = list(type_counts.keys())
counts = list(type_counts.values())
colors = ['green', 'purple', 'red', 'lightblue', 'blue', 'limegreen', 'gray', 'yellow', 'saddlebrown', 
          'pink', 'darkorange', 'darkviolet', 'dimgrey', 'lightgrey', 'white', 'lavender', 'darkblue']
# Customize bar width, color, and edge color
plt.figure(figsize=(16, 6))  # Adjust figure size
plt.bar(types, counts, width=0.8, color=colors, edgecolor='black')
plt.xlabel('Pokemon Type')
plt.ylabel('Count')
plt.title('Pokemon Type Counts')
plt.show()

# In[ ] Webscrapping

# Send a request to the webpage
url = "https://pokeoneguide.com/kanto-guides/kanto-pokemon-locations/"
response = requests.get(url)

# Parse the HTML content of the webpage
soup = BeautifulSoup(response.content, 'html.parser')

# Find the HTML table element
table = soup.find('table')

# Extract data from the HTML table
data = []
if table:
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        row_data = [col.get_text(strip=True) for col in cols]
        data.append(row_data)

# Save the extracted data as a CSV file
filename = "pokemon_locations.csv"
with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

print(f"Data saved as {filename}")

# In[ ] Support functions to create a pokedex location

# Create a list with pokemons' names
pokemon_list = []

for pokemon in pokedex['Pokemon']:
    pokemon_list.append(pokemon)

def get_locations():
    # Open the CSV file
    with open('pokemon_filtered_location.csv', 'r') as csv_file:
        # Create a CSV reader object
        csv_reader = csv.reader(csv_file)
        # Skip the first row (header)
        next(csv_reader)
        # Create an empty dictionary to store the data
        locations = []
        # Initialize a variable to store the current name
        current_name = ''
        # Loop through each row in the CSV file
        for row in csv_reader:
            # Check if the row starts with a name
            if row[0] != '':
                # Update the current name
                current_name = row[0]
                if current_name not in pokemon_list:
                    locations.append(current_name)    
    return locations

def filter_pokemon_location():
    # CSV file name
    csv_file = 'pokemon_locations.csv'
    
    # Function to filter rows based on name
    def filter_csv(pokemon_list, csv_file):
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)  # Read header row
            rows_to_keep = []
            for row in reader:
                if len(row) > 0 and row[0] != '':
                    rows_to_keep.append(row)
                elif len(row) > 1 and row[1] in pokemon_list:  
                    rows_to_keep.append(row)
            return header, rows_to_keep
    
    # Filter CSV based on name list
    header, rows_to_keep = filter_csv(pokemon_list, csv_file)
    
    # Write filtered rows to a new CSV file
    filtered_csv_file = 'pokemon_filtered_location.csv'
    with open(filtered_csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows_to_keep)
    
    print("Filtered CSV file has been created successfully!")

# In[ ] Creates the pokedex with the locations

def create_dictionary():      
    pokemon_location = get_locations()
    # Open the CSV file
    with open('pokemon_filtered_location.csv', 'r') as csv_file:
        # Create a CSV reader object
        csv_reader = csv.reader(csv_file)
        # Skip the first row (header)
        next(csv_reader)
        # Create an empty dictionary to store the data
        data_dict = {}
        # Initialize a variable to store the current name
        current_name = ''
        # Loop through each row in the CSV file
        for row in csv_reader:
            # Check if the row starts with a name
            if row[0] != '':
                # Update the current name
                if row[0] in pokemon_location:
                    current_name = row[0]
                    # Create a list to store the values for the current name
                values = []
            else:
                # If the row starts with an empty string, append the next column value to the list of values
                if len(row) > 1:
                    # Use the next column value as the value and append to the list of values
                    value = row[1]
                    if value in pokemon_list:
                        values.append(value)
                else:
                    # If there is no value in the next column, use an empty string as the value
                    value = ''
                # Add the key-value pair to the dictionary only if the list of values is not empty
                if values:
                    data_dict[current_name] = values
    
    return data_dict

# In[ ] Search pokemon in the pokedex location

pokedex_location = create_dictionary()

def search_by_value(dictionary, value):
    keys = []
    for key, val in dictionary.items():
        if value in val:
            keys.append(key)
    return keys

def search_pokemon():
    search = input("Type a Pokemon: ")
    location = search_by_value(pokedex_location, search)
    
    print(search, 'is found in: ', end="")
    for loc in location:
        # There's an error in the table that some pokemon for other generations appear in the location.
        # All the locations have space character. 
        if " " in loc: 
            print(loc)