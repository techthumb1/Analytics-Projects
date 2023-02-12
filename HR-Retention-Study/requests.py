# Import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the base URL and the URLs for each source
base_url = "https://www.glassdoor.com/research/employee-satisfaction-research/"
urls = [
    "https://www.bls.gov/emp/",
    "https://www.bls.gov/emp/employee-turnover.htm",
    "https://www.gallup.com/services/178514/employee-engagement.aspx",
    "https://www.census.gov/topics/employment/employment-demographics.html",
    "https://www.indeed.com/data",
    "https://www.diversityinc.com/",
    "https://www.shrm.org/research/surveys",
    "https://www.workplacedynamics.com/",
    "https://www.aon.com/human-capital-consulting/thought-leadership/engagement-at-work.jsp"
]

# Define an empty list to store the data
data = []

# Loop through each URL and scrape the data
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract the relevant data from each page and append it to the data list
    for tag in soup.find_all("div"):
        if "employee satisfaction" in tag.text.lower():
            data.append(tag.text)
        elif "employee engagement" in tag.text.lower():
            data.append(tag.text)
        elif "employee turnover" in tag.text.lower():
            data.append(tag.text)
        elif "employee demographics" in tag.text.lower():
            data.append(tag.text)
        elif "job postings" in tag.text.lower():
            data.append(tag.text)
        elif "diversity" in tag.text.lower():
            data.append(tag.text)

# Convert the data list into a Pandas DataFrame
df = pd.DataFrame(data, columns=["Data"])

# Export the DataFrame to a CSV file
df.to_csv("hr_data.csv", index=False)
