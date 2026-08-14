import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    print("\n🌐 Fetching Live Quotes from QuotesToScrape.com...")
    url = "http://quotes.toscrape.com/"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            quotes = soup.find_all("div", class_="quote")

            print("\n" + "="*60)
            print(" 📜 TOP QUOTES SCRAPED SUCCESSFULLY")
            print("="*60)

            for idx, q in enumerate(quotes[:5], 1):
                text = q.find("span", class_="text").get_text()
                author = q.find("small", class_="author").get_text()
                print(f"{idx}. {text}")
                print(f"   ✍️ Author: {author}\n" + "-"*60)
            print()
        else:
            print(f"\n❌ Error: Status code {response.status_code}\n")
    except Exception as e:
        print(f"\n⚠️ Network Error: {e}\n")

def main():
    while True:
        print("⚡ SELECT AN OPTION:")
        print("1. 🕷️ Scrape Live Quotes & Authors")
        print("2. 🚪 Exit")

        choice = input("\n👉 Enter choice (1-2): ").strip()

        if choice == "1":
            scrape_quotes()
        elif choice == "2":
            print("\n👋 Goodbye!")
            break
        else:
            print("\n❌ Invalid choice. Try again!\n")

if __name__ == "__main__":
    main()