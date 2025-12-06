import requests
from config import ENDPOINTS, API_KEY, TARGET_INDUSTRIES


def fetch_symbols():
    """
    Fetch the list of all stock symbols
    Returns:
        list of symbols (str)
    """
    url = ENDPOINTS["symbols"]
    headers = {"Authorization": f"Bearer {API_KEY}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data.get("symbols", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching symbols: {e}")
        return []


def get_symbol_industry(symbol):
    """
    Fetch the industry of a given symbol from the general endpoint.
    Returns the industry string or None if failed.
    """
    url = ENDPOINTS["general"].format(symbol=symbol)
    headers = {"Authorization": f"Bearer {API_KEY}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        fundemantals = data.get("fundamentals", {})
        profile_data = fundemantals.get("profile", {}).get("data", {})
        if profile_data:
            return profile_data[0].get("industry")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching industry for {symbol}: {e}")
        return None


def filter_symbols_by_industry(symbols):
    """
    Returns a list of symbols that belong to the target industries.
    """
    filtered = []
    for symbol in symbols:
        industry = get_symbol_industry(symbol)
        if industry and any(
            target.lower() in industry.lower() for target in TARGET_INDUSTRIES
        ):
            filtered.append(symbol)
    return filtered


if __name__ == "__main__":
    symbols = fetch_symbols()
    symbols_to_fetch = symbols[:20]
    filtered_symbols = filter_symbols_by_industry(symbols_to_fetch)
    print(f"Filtered symbols: {filtered_symbols}")
