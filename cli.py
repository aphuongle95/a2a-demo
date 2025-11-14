import warnings
from dotenv import load_dotenv
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

# Task 1: Import Libraries



# Task 9: Connect CLI with Root Agent
async def run_cli():
    return


if __name__ == "__main__":
    asyncio.run(run_cli())
