"""
Travel Planner CLI
-----------------
This module connects the CLI to the root agent and manages app execution.
Follow PEP 8 and project coding regulations (see instruction.md).
"""

import warnings
from dotenv import load_dotenv
import asyncio
import google.generativeai as genai
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.artifacts import InMemoryArtifactService
from google.adk.apps import App
from agent import root_agent
from google.genai.types import Content
import os
from datetime import datetime

warnings.filterwarnings("ignore", category=UserWarning)
load_dotenv()  # loads .env into os.environ

# Suppress ADK experimental warnings
warnings.filterwarnings(
    "ignore",
    category=UserWarning,
    module=r"google\.adk\..*"
)

# Optional: suppress only function_call concatenation warnings
warnings.filterwarnings(
    "ignore",
    message=r".*non-text parts in the response.*"
)

LOG_DIR = os.path.join(os.path.dirname(__file__), "run")
LOG_FILE = os.path.join(LOG_DIR, "run.log")
os.makedirs(LOG_DIR, exist_ok=True)

def log_to_file(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now().isoformat()}] {message}\n")

# Task 9: Connect CLI with Root Agent
async def run_cli():
    # Set up in-memory services
    artifact_service = InMemoryArtifactService()
    session_service = InMemorySessionService()
    credential_service = None  # No credential service available

    # Create a session for the TravelPlanner app
    session = await session_service.create_session(app_name="TravelPlanner", user_id="user1")
    session_id = session.id  # Get the string ID

    # Initialize the App with root_agent
    app = App(name="TravelPlanner", root_agent=root_agent)
    runner = Runner(app=app,
                   artifact_service=artifact_service,
                   session_service=session_service,
                   credential_service=credential_service)

    print("\nWelcome to the AI Travel Planner! Type your travel questions below.")
    print("Type 'exit' or 'quit' to end the session.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            log_to_file("Session ended by user.")
            break
        # Send input to the agent and stream responses
        user_message = Content(role="user", parts=[{"text": user_input}])
        log_to_file(f"User: {user_input}")
        final_response = None
        try:
            async for response in runner.run_async(
                user_id="user1",
                session_id=session_id,
                new_message=user_message
            ):
                text = None
                if hasattr(response, "parts") and response.parts:
                    text = response.parts[0].text if hasattr(response.parts[0], "text") else str(response.parts[0])
                elif hasattr(response, "content") and hasattr(response.content, "parts"):
                    text = response.content.parts[0].text if hasattr(response.content.parts[0], "text") else str(response.content.parts[0])
                final_response = text if text else None
            # Print and log only the final agent message
            if final_response:
                print(f"Agent: {final_response}")
                log_to_file(f"Agent: {final_response}")
        except Exception as e:
            error_msg = f"Error: {str(e)}"
            print(error_msg)
            log_to_file(error_msg)

    await runner.close()

if __name__ == "__main__":
    asyncio.run(run_cli())
