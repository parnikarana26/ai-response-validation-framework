import json
from openai import OpenAI
from evaluator.similarity import similarity_score
from evaluator.keyword_check import keyword_match
from openai import OpenAI
import os

# OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SIMILARITY_THRESHOLD = 0.65
KEYWORD_THRESHOLD = 0.5

# Load dataset
with open("dataset/prompts.json") as f:
    prompts = json.load(f)


def get_ai_response(prompt):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def test_chatbot_responses():

    for item in prompts:

        prompt = item["prompt"]
        expected = item["expected_answer"]
        keywords = item["expected_keywords"]

        scores = []

        # run multiple times to handle non-determinism
        for i in range(3):

            response = get_ai_response(prompt)

            sim_score = similarity_score(expected, response)
            keyword_score = keyword_match(response, keywords)

            combined_score = (sim_score + keyword_score) / 2
            scores.append(combined_score)

        avg_score = sum(scores) / len(scores)

        assert avg_score > SIMILARITY_THRESHOLD
