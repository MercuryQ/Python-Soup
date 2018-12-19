from bs4 import BeautifulSoup

# load (open) the html file into bs4
soup = BeautifulSoup(open("C:/Users/Gamer1/Desktop/github uploads/Python WebScrap Example/examplePage.html"), "html.parser")

# print all the text within the html document
print(soup.get_text())

# print all of the links in the html document
for link in soup.find_all('a'):
    print(link.get('href'))

# Navigating the html structure
print("\n")
print(soup.title) # print the title tag
print("\n")
print(soup.p) # print the first p tag
print("\n")
print(soup.find_all('p')) # find all p tags



# Warning! This example is not made to inspire individuals to Web Scrap! 
# Before deciding to parse the contents of an actually website, obtain the proper permission from the correct authorities!
# The html5 file in this example is not part of any actual website and is a creation of my own.