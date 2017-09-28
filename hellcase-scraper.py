import requests
import argparse
from lxml import html
from bs4 import BeautifulSoup
url = "https://hellcase.com/en/open/"

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("command")
parser.add_argument("case")
args = parser.parse_args()

case = args.case # Assign the case argument to a variable.
command = args.command # Assignt the command argument to a variable.

url += case # Concatenate the case to the url. Pseudo restful api.
page = requests.get(url) # HTTP GET Request to the given case.
soup = BeautifulSoup(page.content, "html.parser") # Parse the HTML.

if command == "available":
    spans = soup.find_all("span") # Find all <span> ... </span> elements on the page.
    available = False

    # Iterate over the spans to see if you can find the 'Open case' button.
    for span in spans:
        span = span.getText().strip() # Get the text from the Soup object, and strip it (remove some spaces)
        if "Open case  $" in span: # If the 'Open case $' string is contained in a span, we can confirm it is available.
            available = True

    if available:
        print("Yes, the " + case + " case is available! :)")
    else:
        print("The " + case + " case is not available.... :(")
else:
    print("Could not parse command...")