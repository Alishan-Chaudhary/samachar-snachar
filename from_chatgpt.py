import requests
from bs4 import BeautifulSoup

# Local store for news items
news_list = []

def fetch_news():
    """Scrape or fetch news headlines."""
    global news_list
    url = "https://www.bbc.com/news"   # Example source
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = soup.select('h2')  # Simplified headline selector
    news_list = [h.get_text(strip=True) for h in headlines if len(h.get_text(strip=True)) > 5]
    print(f"\n✅ Fetched {len(news_list)} headlines from BBC News.\n")

def show_news():
    """Display current news list."""
    if not news_list:
        print("\n⚠️ No news available. Try fetching first.\n")
        return
    print("\n📰 Current News:\n")
    for i, item in enumerate(news_list, start=1):
        print(f"{i}. {item}")

def add_news():
    """Add a custom news headline manually."""
    new_item = input("\nEnter new headline: ").strip()
    if new_item:
        news_list.append(new_item)
        print("✅ News added successfully!")

def delete_news():
    """Delete a news headline by index."""
    show_news()
    try:
        idx = int(input("\nEnter news number to delete: "))
        if 1 <= idx <= len(news_list):
            removed = news_list.pop(idx - 1)
            print(f"🗑️ Deleted: {removed}")
        else:
            print("❌ Invalid index.")
    except ValueError:
        print("❌ Please enter a valid number.")

def main():
    while True:
        print("""
============================
📰 NEWS CLI APPLICATION
============================
1. View News
2. Add News
3. Delete News
4. Fetch Latest News
5. Exit
""")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            show_news()
        elif choice == '2':
            add_news()
        elif choice == '3':
            delete_news()
        elif choice == '4':
            fetch_news()
        elif choice == '5':
            print("👋 Exiting program...")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    fetch_news()  # Automatically fetch once at start
    main()
