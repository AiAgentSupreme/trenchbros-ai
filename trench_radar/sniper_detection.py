import requests

TRENCH_RADAR_API = "https://api.trench.bot/sniper-detection"

def detect_snipers(token_address):
    response = requests.get(f"{TRENCH_RADAR_API}?address={token_address}")
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch sniper detection data")

# Example usage
if __name__ == "__main__":
    token_address = "0x123456789abcdef"
    snipers = detect_snipers(token_address)
    print(f"Snipers detected: {snipers['count']}")
