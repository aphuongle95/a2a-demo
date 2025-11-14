# A2A Demo: Modular Multi-Agent AI Travel Planner

This project is a modular multi-agent travel planner using Google ADK and Gemini models. It features agents for flights, hotels, weather, and attractions, with a CLI for user interaction.

## Features
- Modular agent architecture
- Google ADK integration
- Gemini model support
- CLI interface
- Logging to run/run.log

## Installation
```bash
# Clone the repo
# Create and activate a conda environment (Python 3.11+)
# Install dependencies
pip install -r requirements.txt
```

## Usage
```bash
python cli.py
```

## Project Structure
- `agent.py`: Defines agents and orchestration
- `cli.py`: CLI interface
- `run/run.py`: Entrypoint script
- `agents/`: Sub-agent implementations
- `requirements.txt`: Python dependencies
- `run/run.log`: CLI and agent logs

## License
MIT
