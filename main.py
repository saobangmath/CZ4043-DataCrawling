import pandas as pd
from tripadvcrawler import TripAdvisorCrawler

maxNoReviews = 200

def restaurantLinksRetrieval():
    data = pd.read_csv("./data/Restaurant_List.csv")
    return data["Link"].tolist()


if __name__ == "__main__":
    urls = restaurantLinksRetrieval()
    crawler = TripAdvisorCrawler()
    for url in urls:
        crawler.scrapeRestaurantInfo(url)
        crawler.scrapeReviews(url, maxNoReviews)

