import json

folder_path = r"C:\Users\Acer\OneDrive\Desktop\samachar files/json_data.json"

def add_source():
    url = input("Enter the RSS URL = ")


# url = "https://www.ratopati.com/feed"

    with open(folder_path,'r') as file:
        data = json.load(file)

    if url in data:
        print("URL already exists in database!!")

    else:
        data.append(url)
        with open(folder_path,'w') as file:
            json.dump(data,file)








# for url in data:

#     feed =feedparser.parse(url)

#     head = ["Date","Title","summary"]

#     site = feed.feed.title


#     if site == "World":
#         site_name = "The Washington Post"

#     elif site == "NYT > Top Stories":
#         site_name = "The New York Times"

#     elif site == "CNN.com - RSS Channel - App International Edition":
#         site_name = "CNN"

#     elif site == "BBC News":
#         site_name = "BBC News"
    
#     elif site == "World news | The Guardian":
#         site_name = "The Guardian"

#     elif site == "Home - CBSNews.com":
#         site_name = "CBS News"

#     else:
#         site_name = site


#     print(site_name)