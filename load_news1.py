import feedparser 
import os 
import datetime
from datetime import datetime
import json
import pandas as pd


folder_path = r"C:\Users\Acer\OneDrive\Desktop\samachar files"

json_file_path = r"C:\Users\Acer\OneDrive\Desktop\samachar files/json_data.json"


# with open(json_file_path,'r') as file:
#     site_list = json.load(file)


site_list = ["http://feeds.bbci.co.uk/news/world/rss.xml"]


for url in site_list:

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

    # duplicated_data = []

    for entry in feed.entries:
        date = entry.get('published')
        title = entry.get('title')
        summary = entry.get('summary')


        data = [{
            "DATE":date,
            "Title":title,
            "Summary":summary
        }]

        data_df = pd.DataFrame(data)

       
        
        duplicated_data_site = []

        if os.path.exists(full_file_path):
            
            existing_data = pd.read_csv(full_file_path)
        
            old_date = pd.to_datetime(existing_data["DATE"])

            old_date = old_date.dt.strftime("%a, %d %b %Y")

            new_date =pd.to_datetime(data_df["DATE"])
            new_date = new_date.dt.strftime("%a, %d %b %Y")

            if new_date.isin(old_date).all():
                duplicated_data_site.append(site)

            else:
                
                existing_data = pd.concat([existing_data,data_df],ignore_index=False)
            
                existing_data.to_csv(full_file_path,index=False)
                print("data appended")

        else:
            data_df.to_csv(full_file_path,index=False)
            print("file created")
    
    print(f"duplicated data = {duplicated_data_site}")

    


