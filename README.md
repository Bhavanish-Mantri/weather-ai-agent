#  Weather AI Agent

An AI-powered Weather Agent built using **Python**, **LangChain**, **Ollama (Llama 3)**, and the **OpenWeather API**. The agent interacts with the user, asks for a city name, retrieves real-time weather information, and presents the results in a natural and user-friendly format.

##  Features

* Interactive AI agent interface
* Asks the user for a city name
* Retrieves real-time weather data
* Uses LangChain with a local Llama 3 model via Ollama
* Generates natural language weather responses
* Runs completely locally without requiring OpenAI API credits
* Easy to extend with additional tools and capabilities

---

##  Technologies Used

* Python 3
* LangChain
* Ollama
* Llama 3
* OpenWeather API
* Requests
* Python Dotenv

---

##  Project Structure

```text
WhetherAgent/
│
├── weather_agent.py      # Main AI agent
├── weather_tool.py       # Weather API integration
├── .env                  # Environment variables (not committed)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Bhavanish-Mantri/weather-ai-agent.git
cd weather-ai-agent
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama

Download and install Ollama from:

https://ollama.com/download

### 5. Download Llama 3

```bash
ollama pull llama3
```

### 6. Configure Environment Variables

Create a `.env` file in the project root:

```env
OPENWEATHER_API_KEY=YOUR_API_KEY_HERE
```

Get a free API key from:

https://openweathermap.org/api

---

## Running the Project

```bash
python weather_agent.py
```

Example:

```text
Hello! I am your AI Weather Agent.

Which city would you like the weather for?

Jaipur
```

Output:

```text
AI Agent Response:

The current weather in Jaipur is:

🌡 Temperature: 36°C
💧 Humidity: 42%
☀ Condition: Clear Sky

Have a great day!
```

---

##  How It Works

```text
User
  │
  ▼
Weather Agent
  │
  ▼
Weather Tool
  │
  ▼
OpenWeather API
  │
  ▼
Weather Data
  │
  ▼
Llama 3 (Ollama)
  │
  ▼
Natural Language Response
  │
  ▼
User
```

---

##  Security

API keys are stored in a local `.env` file and are not committed to the repository. Make sure to add `.env` to `.gitignore` before pushing code to GitHub.

---

##  Assignment Objective

Create an AI agent that asks the user for a city name and returns current weather information. Python was used as the implementation language, with LangChain and Ollama providing the AI capabilities.

---

