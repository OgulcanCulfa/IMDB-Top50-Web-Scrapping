import requests
from bs4 import BeautifulSoup


# url declaration

url = "https://www.imdb.com/chart/top/"


# library initialization

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")


# scraping the necessary infos

liste = soup.find("tbody",{"class":"lister-list"}).find_all("tr",limit=50)


# add price infos into the list

h_w_y = []

for item in liste:

    header = item.find("td",{"class":"titleColumn"}).find("a").text
    year = item.find("td",{"class":"titleColumn"}).find("span", {"class":"secondaryInfo"}).text.strip("()")
    

    header_with_year = header + " " + "-" + " " + year 

    h_w_y.append(header_with_year)
    
    # print(header_with_year)


# if you want to take datas in a list, uncomment this

    # h_w_y = [x.strip().split("\n") for x in h_w_y]




# Create a txt file and write the datas that we scrapped from website 

file = open("imdb top50 movies.txt", "x")
for files in h_w_y:
    file.write("%s\n" % files)

















