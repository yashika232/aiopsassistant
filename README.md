AI Operations Assistant
An intelligent, multi-agent system designed to handle operations tasks like searching GitHub and fetching real-time weather data. Built with FastAPI, Gemini 3 Flash, and Python AsyncIO, it features parallel tool execution, result caching, and granular cost tracking.

**Setup Instructions**
1. Prerequisites
Python 3.10 or higher
A Google AI Studio API Key
A GitHub Personal Access Token
A WeatherAPI.com (https://www.weatherapi.com/my/)

2. Installation
Clone the repository:
Bash
git clone https://github.com/your-username/aiopsassistant.git
cd aiopsassistant

Create a virtual environment:
Bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:
Bash
pip install -r requirements.txt

3. Running the App
Start the FastAPI server:
Bash
uvicorn main:app --reload
Access the API:
Swagger UI: http://127.0.0.1:8000/docs
API Endpoint: POST http://127.0.0.1:8000/run

**Environment Variables**
Create a .env file in the root directory. Use the following structure:

Bash
# LLM Configuration
GEMINI_API_KEY=your_gemini_api_key_here

# Tool Configurations
GITHUB_TOKEN=your_github_pat_here
WEATHER_API_KEY=your_weatherapi_key_here

**Architecture**
The system uses an Orchestrated Multi-Agent Pattern:

Planner Agent (planner.py): Receives the user's natural language request and converts it into a structured JSON execution plan containing specific tool actions and parameters.

Executor (executor.py): The "Hands" of the system. It uses asyncio.gather to run all planned steps in parallel. It also implements a TTL Cache to prevent redundant API calls.

Verifier Agent (verifier.py): Takes the raw tool outputs and the original task to synthesize a clean, human-readable final response.

Tools (tools/): Isolated Python modules for external API interaction.

**Integrated APIs**
Google Gemini API: Powers the reasoning (Planning and Verification).

GitHub Search API: Finds repositories based on queries and star counts.

WeatherAPI: Provides real-time weather data and conditions for any city.

**Example Prompts**
You can test the system using the following queries in the task parameter:

Single Tool: "What is the weather like in Paris?"

Parallel Execution: "Find the top 3 React repositories and tell me the weather in New York."

Complex Multi-Step: "Search for popular Python ML repos and give me the weather for London, Tokyo, and Berlin."

Cache Testing: Run the same complex prompt twice; the second response will be significantly faster as it pulls from the local cache.

**Known Limitations & Tradeoffs**
In-Memory Cache: The current cache is stored in RAM. If the server restarts, the cache is cleared.

Context Window: While Gemini 3 Flash has a massive context window, the verifier may struggle with extremely large tool outputs (e.g., searching for 50+ GitHub repos at once).

Rate Limits: The system is subject to the rate limits of the GitHub and WeatherAPI free tiers.

No Multi-turn Memory: This version is stateless; it does not remember previous questions in a conversation thread.
