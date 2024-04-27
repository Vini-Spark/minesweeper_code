from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from bs4 import BeautifulSoup
from lxml import html
import time

# Setup Edge driver
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

# Open the webpage
driver.get('https://minesweeper.online/pt/game/3251262823')

# Wait for the webpage to load
time.sleep(10)  # wait for 5 seconds

# Get the HTML content of the page
html_content = driver.page_source

# Parse the HTML with lxml
tree = html.fromstring(html_content)

# Find the cells at the specified XPath
cells = tree.xpath('/html/body/div[3]/div[2]/div/div[1]/div[2]/div/div[4]/div[5]/table/tbody/tr/td[1]/div/div[1]/div[4]/div[2]')

print(f"Cells: {len(cells)}")

# Print the class and screen position of each cell
for cell in cells:
    # Get the class of the cell
    cell_class = cell.get('class')
    
    # Get the screen position of the cell
    cell_position = driver.execute_script("return arguments[0].getBoundingClientRect();", cell)
    
    print(f"Cell class: {cell_class}, Cell position: {cell_position}")

# Close the WebDriver
# driver.quit()
