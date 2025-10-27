import json
import feedparser
import os

json_folder_path = r"C:\Users\Acer\OneDrive\Desktop\samachar files/json_data.json"

folder_path = r"C:\Users\Acer\OneDrive\Desktop\samachar files/"

with open(json_folder_path,'r') as file:
    data = json.load(file)

# data =["http://rss.cnn.com/rss/edition.rss", "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml", "https://feeds.washingtonpost.com/rss/world", "http://feeds.bbci.co.uk/news/world/rss.xml", "https://www.theguardian.com/world/rss", "https://www.cbsnews.com/latest/rss/main"]

for index,url in enumerate(data,1):

    feed = feedparser.parse(url)

    head = ["Date","Title","summary"]

    site = feed.feed.title


    if site == "World":
        site_name = "The Washington Post"

    elif site == "NYT > Top Stories":
        site_name = "The New York Times"

    elif site == "CNN.com - RSS Channel - App International Edition":
        site_name = "CNN"

    elif site == "BBC News":
        site_name = "BBC News"
    
    elif site == "World news | The Guardian":
        site_name = "The Guardian"

    elif site == "Home - CBSNews.com":
        site_name = "CBS News"

    else:
        site_name = site


    print(f"{index} {site_name}")


delete_input = input("Enter the index of site you want to delete =").split()

delete_input = [int(x) for x in delete_input]

for i in delete_input:

    delete_index = i-1

    print(data[delete_index])

assurance = input(f"Confirm you want to delete these source[y/n]?")

assurance = assurance.lower()

if assurance == "y":
    j = 1
    for i in delete_input:
        
        data_index = i - j

        url = data[data_index]
        feed = feedparser.parse(url)

        site = feed.feed.title

        if site == "World":
            site_name = "The Washington Post"

        elif site == "NYT > Top Stories":
            site_name = "The New York Times"

        elif site == "CNN.com - RSS Channel - App International Edition":
            site_name = "CNN"

        elif site == "BBC News":
            site_name = "BBC News"
    
        elif site == "World news | The Guardian":
            site_name = "The Guardian"

        elif site == "Home - CBSNews.com":
            site_name = "CBS News"

        else:  
            site_name = site

        file_path = site_name
        full_file_path = f"{folder_path}/{file_path}"

        if os.path.exists(full_file_path):
            os.remove(full_file_path)

        else:
            print("file not found")
        

        
        del(data[data_index])
        
        j = j+1
        
        with open(json_folder_path,'w') as file:
            json.dump(data,file)

    

 

    
    

    

    