from weather_tool import get_weather

from deepeval import evaluate
from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCase, SingleTurnParams

# -------------------------------
# Test Cases
# -------------------------------

cities = [
    "Jaipur",
    "Delhi",
    "Mumbai",
    "London",
    "Tokyo"
]

test_cases = []

for city in cities:

    weather_response = get_weather(city)

    test_case = LLMTestCase(
        input=f"What is the weather in {city}?",
        actual_output=weather_response,
        expected_output=(
            f"The response should contain the weather information for {city}, "
            "including the city name, temperature, humidity, and weather condition."
        )
    )

    test_cases.append(test_case)

# -------------------------------
# Evaluation Metric
# -------------------------------

weather_metric = GEval(
    name="Weather Response Quality",
    criteria="""
Evaluate the weather response using the following criteria:

1. The response answers the user's weather query.
2. The requested city name is mentioned.
3. Temperature information is present.
4. Humidity information is present.
5. Weather condition is present.
6. The response is clear, readable, and easy to understand.

Assign a high score only if all the above conditions are satisfied.
""",
    evaluation_params=[
        SingleTurnParams.ACTUAL_OUTPUT,
        SingleTurnParams.EXPECTED_OUTPUT,
    ],
    threshold=0.7,
    async_mode=False
)

# -------------------------------
# Run Evaluation
# -------------------------------

evaluate(
    test_cases=test_cases,
    metrics=[weather_metric]
)