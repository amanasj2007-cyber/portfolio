import requests
from datetime import date

def get_weather():
    city = "Kochi"
    url = f"https://wttr.in/{city}?format=3"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        return f"Weather error: {e}"

def get_quote():
    try:
        response = requests.get(
            "https://zenquotes.io/api/random",
            timeout=10
        )
        response.raise_for_status()

        data = response.json()
        return f"{data[0]['q']} — {data[0]['a']}"

    except Exception as e:
        return f"Quote error: {e}"

def build_summary():
    weather = get_weather()
    quote = get_quote()

    summary = f"""
Date: {date.today()}

Weather:
{weather}

Quote:
{quote}
"""
    return summary

def run():
    summary =  print(build_summary())



print("Pulse ran successfully.")

if __name__ == "__main__":
    run()
