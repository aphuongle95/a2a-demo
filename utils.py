"""
Utility functions for the Travel Planner agents.
"""
import json
from datetime import datetime

def load_flights_data(path="flights_dataset.json"):
    """Load mock flight data from a JSON file."""
    with open(path) as f:
        return json.load(f)

def query_flights(flights_data, departure_city, arrival_city, date=None, date_range=None, month=None):
    """Filter flights by departure city, arrival city, and date criteria."""
    results = []
    for flight in flights_data:
        if flight["departure_city"].lower() != departure_city.lower():
            continue
        if flight["arrival_city"].lower() != arrival_city.lower():
            continue
        dep_time = flight["departure_time"]  # format: MM-DD HH:MM
        dep_date = dep_time.split()[0]  # MM-DD
        if date and dep_date != date:
            continue
        if date_range:
            start, end = date_range
            if not (start <= dep_date <= end):
                continue
        if month and not dep_date.startswith(month):
            continue
        results.append(flight)
    return results

def query_flights_simple(flights_data, departure_city, arrival_city, date):
    """Return summaries of flights matching the given cities and date."""
    flights = query_flights(flights_data, departure_city, arrival_city, date=date)
    if not flights:
        return "No flights found for your criteria."
    summaries = []
    for f in flights:
        summaries.append(
            f"{f['airline']} {f['flight_number']}: {f['departure_city']} ({f['departure_airport']}) to {f['arrival_city']} ({f['arrival_airport']})\n"
            f"Departure: {f['departure_time']} | Arrival: {f['arrival_time']} | Status: {f['status']}"
        )
    return "\n\n".join(summaries)

def load_hotels_data(path="mock_hotels.json"):
    """Load mock hotel data from a JSON file."""
    with open(path) as f:
        return json.load(f)

def query_hotels(hotels_data, city, min_rating=None, max_price=None):
    """Return hotels in a city, filtered by minimum rating and maximum price."""
    results = []
    for hotel in hotels_data:
        if hotel["city"].lower() != city.lower():
            continue
        if min_rating and hotel["rating"] < min_rating:
            continue
        if max_price and hotel["price"] > max_price:
            continue
        results.append(hotel)
    if not results:
        return "No hotels found for your criteria."
    summaries = [f"{h['name']} (Rating: {h['rating']}, Price: ${h['price']})" for h in results]
    return "\n".join(summaries)
