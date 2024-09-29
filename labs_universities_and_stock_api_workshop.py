# -*- coding: utf-8 -*-
"""Labs\Universities_and_Stock_API_Workshop.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/github/fourfeatherz/DS2002F24/blob/main/Labs%5CUniversities_and_Stock_API_Workshop.ipynb

# Using API Calls in Python with JSON and DataFrames - University Data Example
In this notebook, we will make API requests to the Hipolabs Universities API, parse the JSON response, and convert it into Pandas DataFrames for analysis and visualization.

### Step 1: Making the API Call to Fetch University Data
"""

import requests
import json
import pandas as pd

# API endpoint for fetching universities
url = "http://universities.hipolabs.com/search?country=United%20States"

# Make the GET request
response = requests.get(url)

# Check the status code
if response.status_code == 200:
    print("API request successful!")
else:
    print(f"Failed to retrieve data: {response.status_code}")

"""### Step 2: Parsing the JSON Response"""

# Parse the JSON response
university_data = response.json()

# Pretty-print the first university
print(json.dumps(university_data[0], indent=2))

"""### Step 3: Converting the JSON Data to a DataFrame"""

# Convert JSON data to a DataFrame
df = pd.DataFrame(university_data)

# Display the first few rows of the DataFrame
print(df.head())
df

"""### Step 4: Basic Data Analysis"""

# Count the number of universities by state
state_counts = df['state-province'].value_counts()
print(state_counts)

"""### Step 5: Data Visualization"""

import matplotlib.pyplot as plt

# Plot the number of universities per state
state_counts.plot(kind='bar', figsize=(10, 6))
plt.title("Number of Universities per State")
plt.xlabel("State")
plt.ylabel("Number of Universities")
plt.show()

"""### Step 6: Extending to Multiple Countries"""

countries = ["United States", "Canada", "Australia", "United Kingdom"]
university_list = []

for country in countries:
    response = requests.get(f"http://universities.hipolabs.com/search?country={country}")
    data = response.json()

    for uni in data:
        uni['country'] = country
        university_list.append(uni)

# Convert to DataFrame
df_universities = pd.DataFrame(university_list)

# Display the first few rows
print(df_universities.head())

"""### Step 7: Visualizing University Counts by Country"""

# Count the number of universities per country
country_counts = df_universities['country'].value_counts()

# Plot the data
country_counts.plot(kind='bar', figsize=(10, 6))
plt.title("Number of Universities per Country")
plt.xlabel("Country")
plt.ylabel("Number of Universities")
plt.show()

"""###Step 8: Customizing the Workshop

You can experiment further by:



*   Fetching data for specific regions.
*   Analyzing other attributes such as university domains.
*   Creating visualizations to compare universities in different regions.

*For* the followig you will need to get your API key from  https://financeapi.net/
Examine the demo page and sample data to be returned
"""

import json
import pandas as pd
import json
import requests

#get stock from the user
stock=input()

print("The Stock we will research is:" + stock)

apikey="X"

url = "https://yfapi.net/v6/finance/quote"

querystring = {"symbols":stock}

headers = {
    'x-api-key': apikey
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

#print the company name and price
stock_json = response.json()
print(stock_json['quoteResponse']['result'][0]["longName"] + " Price:$" + str(stock_json['quoteResponse']['result'][0]["regularMarketPrice"]))

"""Ask the user for a list of stocks and pass that answer back to the user

> Add blockquote



"""

stocks = input().split(',')

print("The Stocks we will research are: " + ", ".join(stocks))

apikey = "X"

url = "https://yfapi.net/v6/finance/quote"

headers = {
    'x-api-key': apikey
}

for stock in stocks:
    stock = stock.strip()
    querystring = {"symbols": stock}

    response = requests.get(url, headers=headers, params=querystring)

    stock_json = response.json()
    try:
        company_name = stock_json['quoteResponse']['result'][0]["longName"]
        stock_price = stock_json['quoteResponse']['result'][0]["regularMarketPrice"]
        print(f"{company_name} ({stock}) Price: ${stock_price}")
    except (KeyError, IndexError):
        print(f"Error: Unable to fetch information for {stock}. Please check the symbol.")