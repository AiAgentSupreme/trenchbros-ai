import requests

TWEETSCOUT_API_URL = "https://api.tweetscout.io/v2/analyze"

def fetch_sentiment(token_name):
    response = requests.post(TWEETSCOUT_API_URL, json={"token": token_name})
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Error fetching sentiment data from TweetScout")

# Example usage
if __name__ == "__main__":
    token_name = "TrenchBros"
    sentiment_data = fetch_sentiment(token_name)
    print(f"Sentiment analysis for {token_name}: {sentiment_data}")
