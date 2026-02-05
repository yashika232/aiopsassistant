# AI Operations Assistant 🤖

An intelligent, multi-agent system designed to automate operational tasks such as searching GitHub and fetching real-time weather data. Built with **FastAPI**, **Gemini 3 Flash**, and **Python AsyncIO**, it features parallel tool execution, result caching, and granular cost tracking.

## 🚀 Quick Start

### 1. Prerequisites
* **Python 3.10+**
* [Google AI Studio API Key](https://aistudio.google.com/) (for Gemini)
* [GitHub Personal Access Token](https://github.com/settings/tokens)
* [WeatherAPI.com Key](https://www.weatherapi.com/my/)

### 2. Installation
```bash
# Clone the repository
git clone [https://github.com/your-username/aiopsassistant.git](https://github.com/your-username/aiopsassistant.git)
cd aiopsassistant

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Running the App
```Bash
# Start the FastAPI server
uvicorn main:app --reload
```
Interactive Documentation: http://127.0.0.1:8000/docsAPI Endpoint: POST http://127.0.0.1:8000/run

## Environment Variables

Create a .env file in the root directory with the following keys:
```Bash# LLM Configuration
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-2.0-flash

# Tool Configurations
GITHUB_TOKEN=your_github_pat_here
WEATHER_API_KEY=your_weatherapi_key_here
```

## Architecture
The system utilizes an Orchestrated Multi-Agent Pattern:
+ Planner Agent (planner.py): The "Brain." It converts natural language into a structured JSON execution plan.
+ Executor (executor.py): The "Hands." It uses asyncio.gather to run all planned steps in parallel and implements a TTL Cache to reduce latency and API costs.
+ Verifier Agent (verifier.py): The "Critic." It synthesizes raw tool outputs into a refined, human-readable response.
+ Tools (tools/): Modular Python scripts for specific API interactions.

##🛠️ Integrated APIs
+ Google GeminiReasoning, planning, and final verification.
+ GitHub SearchRepository discovery and star-count filtering.
+ WeatherAPIReal-time weather data and environmental conditions.

## Example Prompts
Test the system by sending these queries to the task parameter in the Swagger UI:
- Single Tool: "What is the weather like in Paris?"
- Parallel Execution: "Find the top 3 React repositories and tell me the weather in New York."
- Complex Multi-Step: "Search for popular Python ML repos and give me the weather for London, Tokyo, and Berlin."
- Cache Testing: Run the same complex prompt twice; the second response will be near-instant as it bypasses external API calls.

## Known Limitations & Tradeoffs

+ In-Memory Cache: The cache is stored in RAM and will be cleared if the server restarts.
+ Context Window: Extremely large tool outputs (e.g., 50+ GitHub repos) may challenge the Verifier's synthesis logic.
+ Rate Limits: Performance is subject to the free-tier limits of the GitHub and Weather APIs.
+ Stateless: No multi-turn memory; each request is handled in isolation without session history.

