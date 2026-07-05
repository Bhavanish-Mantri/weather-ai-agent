# 🌦️ Weather AI Agent

A simple AI-powered Weather Agent built using **Python** and the **OpenWeather API**. The application accepts a city name from the user, retrieves real-time weather information, and displays the temperature, humidity, and weather condition. The project also includes **DeepEval**-based evaluation to assess the quality of the AI agent's responses.

---

## Features

- Get real-time weather information for any city.
- Displays:
  - Temperature
  - Humidity
  - Weather Condition
- Simple command-line interface.
- AI Agent evaluation using the **DeepEval** framework.
- Uses **Gemini** as the evaluation model.

---

## Technologies Used

- Python 3
- OpenWeather API
- Requests
- Python Dotenv
- DeepEval
- Google Gemini API

---

## Project Structure

```text
weather-ai-agent/
│
├── weather_agent.py      # Main Weather AI Agent
├── weather_tool.py       # OpenWeather API integration
├── evaluate.py           # DeepEval evaluation script
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/Bhavanish-Mantri/weather-ai-agent.git
cd weather-ai-agent
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file:

```env
OPENWEATHER_API_KEY=YOUR_OPENWEATHER_API_KEY
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

## Run the Weather AI Agent

```bash
python weather_agent.py
```

Example:

```
Hello! I am your AI Weather Agent.

Enter city name:
Jaipur

Weather in Jaipur
Temperature: 36°C
Humidity: 40%
Condition: clear sky
```

---

## Run the DeepEval Evaluation

```bash
python evaluate.py
```

Example evaluation result:

```
Weather Response Quality (GEval)

Total Test Cases : 2
Passed           : 2
Failed           : 0
Pass Rate        : 100%
Average Score    : 1.00
```

---

## Evaluation Criteria

The AI agent is evaluated based on:

- Correctly answering the weather query
- Mentioning the requested city
- Including temperature
- Including humidity
- Including weather condition
- Producing a clear and understandable response

---
