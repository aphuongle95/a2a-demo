# AI Travel Planner Project Overview & Python Coding Regulations

## Project Description

The AI Travel Planner is a hands-on project for building an intelligent trip planning assistant using multi-agent coordination. At its core is a root agent that orchestrates specialized sub-agents for flights, hotels, attractions, and weather, all communicating via the Agent2Agent (A2A) protocol.

Key features include:
- Flight suggestions between cities using a mock dataset
- Hotel recommendations based on city-specific mock data
- Tourist attraction ideas for your destinations
- Real-time weather forecasts from the OpenWeatherMap API

Agents work together, sharing information and delegating tasks, to provide seamless travel planning. This project offers practical experience in designing and implementing multi-agent systems for real-world applications.

## 1. Code Style
- Follow PEP 8 for Python code formatting.
- Use 4 spaces per indentation level.
- Limit lines to 79 characters.
- Use meaningful variable and function names.

## 2. Imports
- Group imports in the following order: standard library, third-party, local modules.
- Avoid unused imports.

## 3. Environment
- Use `.env` files for secrets and API keys.
- Load environment variables using `python-dotenv`.

## 4. Error Handling
- Use try/except blocks for external API calls and critical operations.
- Log errors or print meaningful messages for debugging.

## 5. Dependencies
- List all required packages in `requirements.txt`.
- Use virtual environments (e.g., conda, venv) for project isolation.

## 6. Git
- Commit code regularly with clear messages.
- Do not commit secrets or sensitive data.
- Use `.gitignore` to exclude unnecessary files.

## 7. Documentation
- Add docstrings to all functions and classes.
- Use comments to explain complex logic.
- Maintain an up-to-date `README.md` for project overview and setup instructions.

## 8. Testing
- Write tests for critical functions and modules.
- Use `pytest` or `unittest` for automated testing.

## 9. Security
- Never hardcode secrets or credentials in code.
- Validate and sanitize all user inputs.

## 10. Collaboration
- Use branches for new features and bug fixes.
- Review code before merging to main branch.

---
For more details, refer to the official Python documentation and PEP guidelines.
