import feedparser 
import json
import pandas as pd
import os
import datetime 
from datetime import datetime



folder_path = r"C:\Users\Acer\OneDrive\Desktop\samachar files"

file_path = r"C:\Users\Acer\OneDrive\Desktop\samachar files/json_data.json"




def get_news(url):
    url = url

    feed =feedparser.parse(url)

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

    for entry in feed.entries:
        date = entry.published
        title = (f"Title:{entry.title}")
        summary = (f"Summary:{entry.summary}")

        data=[{
            "DATE":date,
            "Title":title,
            "Summary":summary
        }]

        df = pd.DataFrame(data)

        print(df)



    # if os.path.exists(full_file_path):
            
    #     existing_data = pd.read_csv(full_file_path)
            
    #     existing_date = pd.to_datetime(existing_data["DATE"])
        
    #     existing_date = existing_date.dt.strftime("%a, %d %b %Y")

    #     new_date =pd.to_datetime(df["DATE"])
    #     new_date = new_date.dt.strftime("%a, %d %b %Y")

    #         # print(new_date)
    #         # print(existing_date)
 
    #     if new_date.isin(existing_date).all():
    #         print("DATE matches")

    #     else:
    #         existing_data = pd.concat([existing_data,df],ignore_index=True)
            
    #         existing_data.to_csv(full_file_path,index=False)
    #         print("data appended")

    # else:
    #     df.to_csv(full_file_path,index=False)
    #     print("file created")

 
# with open (file_path,'r')as file:
#     data = json.load(file)


# for i in data:
#     get_news(i)'

get_news("https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml")

        

    

