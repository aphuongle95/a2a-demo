"""
Travel Planner Agent
-------------------
This module defines agents and tools for the travel planner app.
Follow PEP 8 and project coding regulations (see instruction.md).
"""

import json
import os
import random
from datetime import datetime

import google.generativeai as genai
from google.adk.agents import Agent  # Removed RemoteA2aAgent import
from google.adk.tools.example_tool import ExampleTool
from google.adk.tools.function_tool import FunctionTool
from utils import load_flights_data, query_flights_simple, load_hotels_data, query_hotels
from agents.weather_agent.agent import weather_agent

# Attractions Agent: provides tourist attractions and sightseeing spots for a given city
attractions_agent = Agent(
    name="attractions_agent",
    description="Provides information about tourist attractions and sightseeing spots for a given city.",
    instruction="When asked about attractions, suggest popular sightseeing spots and points of interest for the specified city.",
    model="gemini-2.5-flash",
)

# Load mock flight data
flights_data = load_flights_data()

def flight_query(dep: str, arr: str, date: str):
    return query_flights_simple(flights_data, dep, arr, date)

flight_agent = Agent(
    name="flight_agent",
    description="Answers flight-related queries using a mock flight dataset.",
    instruction="Provide clear summaries of available flights between cities on specific dates, including airline, flight number, departure/arrival cities, times, and status. If no flights match, politely inform the user.",
    model="gemini-2.5-flash",
    tools=[FunctionTool(flight_query)],
)

# Load mock hotel data
hotels_data = load_hotels_data()

def hotel_query(city: str, min_rating: float = None, max_price: float = None):
    return query_hotels(hotels_data, city, min_rating, max_price)

hotel_agent = Agent(
    name="hotel_agent",
    description="Provides hotel recommendations using a mock hotel dataset.",
    instruction="Suggest hotels in a city, applying filters for minimum rating and maximum price. Respond with hotel name, rating, and price. If no hotels match, inform the user.",
    model="gemini-2.5-flash",
    tools=[FunctionTool(hotel_query)],
)

# ExampleTool: Demonstrates multi-agent interactions for travel planning
example_tool = ExampleTool([
    {
        "input": {
            "role": "user",
            "parts": [{"text": "Plan a trip to Paris including flights, hotels, and attractions."}],
        },
        "output": [
            {"role": "model", "parts": [{"text": "Flight Agent: Found flights to Paris."}]},
            {"role": "model", "parts": [{"text": "Hotel Agent: Recommended hotels in Paris."}]},
            {"role": "model", "parts": [{"text": "Attractions Agent: Suggested top sights."}]},
            {"role": "model", "parts": [{"text": "Root Agent: Here is your complete Paris trip plan with flights, hotels, and attractions."}]}
        ],
    },
    {
        "input": {
            "role": "user",
            "parts": [{"text": "Find hotels near the Eiffel Tower."}],
        },
        "output": [
            {"role": "model", "parts": [{"text": "Hotel Agent: Listed hotels near the Eiffel Tower."}]},
            {"role": "model", "parts": [{"text": "Root Agent: Refined recommendations based on proximity to the attraction."}]}
        ],
    },
    {
        "input": {
            "role": "user",
            "parts": [{"text": "Create a daily itinerary for Rome."}],
        },
        "output": [
            {"role": "model", "parts": [{"text": "Attractions Agent: Proposed activities for each day."}]},
            {"role": "model", "parts": [{"text": "Root Agent: Finalized the daily schedule for Rome."}]}
        ],
    },
    {
        "input": {
            "role": "user",
            "parts": [{"text": "Book a return flight from Tokyo."}],
        },
        "output": [
            {"role": "model", "parts": [{"text": "Flight Agent: Provided return flight options."}]},
            {"role": "model", "parts": [{"text": "Root Agent: Confirmed the selected return flight."}]}
        ],
    }
])

root_agent = Agent(
    name="root_agent",
    description="Central coordinator for the AI travel planner. Delegates tasks to weather, hotel, flight, and attractions agents using A2A.",
    instruction="Coordinate all travel planning tasks by delegating to sub-agents. Confirm plans with the user and ensure all information is accurate and safe.",
    global_instruction="You are the root agent for an AI travel planner. Delegate queries to the appropriate sub-agent (weather, hotel, flight, attractions) and confirm the final plan with the user.",
    model="gemini-2.5-flash",  # Use Gemini 1.5 pro model
    sub_agents=[weather_agent, hotel_agent, flight_agent, attractions_agent],
    tools=[example_tool],  # Add example_tool for demonstration scenarios
)

