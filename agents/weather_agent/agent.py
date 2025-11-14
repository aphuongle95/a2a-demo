import os
import httpx
from google.adk import Agent
from google.genai import types

OPENWEATHERMAP_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")

async def get_weather(location):
    """Fetch 5-day weather forecast for a city using OpenWeatherMap API."""
    if not OPENWEATHERMAP_API_KEY:
        return "Weather API key is missing. Please set OPENWEATHERMAP_API_KEY."
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={location}&appid={OPENWEATHERMAP_API_KEY}&units=metric"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            if response.status_code != 200:
                return f"Weather API error: {response.status_code} {response.text}"
            data = response.json()
            # Group forecasts by day
            daily = {}
            for entry in data.get("list", []):
                date = entry["dt_txt"].split()[0]
                temp = entry["main"]["temp"]
                desc = entry["weather"][0]["description"]
                if date not in daily:
                    daily[date] = {"high": temp, "low": temp, "desc": set([desc])}
                else:
                    daily[date]["high"] = max(daily[date]["high"], temp)
                    daily[date]["low"] = min(daily[date]["low"], temp)
                    daily[date]["desc"].add(desc)
            # Format summary
            summaries = []
            for date, info in daily.items():
                summaries.append(f"{date}: High {info['high']}°C, Low {info['low']}°C, {'/'.join(info['desc'])}")
            return "\n".join(summaries) if summaries else "No forecast data available."
    except Exception as e:
        return f"Error fetching weather: {e}"

weather_agent = Agent(
    name="weather_agent",
    description="Provides 5-day city weather forecasts using OpenWeatherMap API.",
    instruction="When asked about weather, provide a daily summary with highs, lows, and descriptions for the next 5 days.",
    tools=[get_weather],
)
