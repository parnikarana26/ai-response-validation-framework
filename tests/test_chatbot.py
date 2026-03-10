import json
from openai import OpenAI
from evaluator.similarity import similarity_score
from evaluator.keyword_check import keyword_match
from openai import OpenAI
import os

# Set the key using this command export OPENAI_API_KEY="your_api_key"
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SIMILARITY_THRESHOLD = 0.6
KEYWORD_THRESHOLD = 0.5

# Load dataset
with open("dataset/prompts.json") as f:
    prompts = json.load(f)


def get_ai_response(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as e:
        print("API Error:", e)
        return ""
        
        # simulated the AI response as my OpenAI account has reached the limit of usage allowed
# def get_ai_response(prompt):

#     prompt = prompt.lower()

#     if "reset" in prompt or "password" in prompt:
#         return "You can reset your password by clicking the 'forgot password' option on the login page and following the instructions sent to your email."

#     elif "track" in prompt or "order" in prompt:
#         return "You can track your order by going to the orders section in your account and selecting the order you want to track."

#     return "Please contact customer support for further assistance."


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
            print("\nPrompt:", prompt)
            print("Response:", response)
            print("Similarity:", sim_score)
            print("Keyword Score:", keyword_score)
            print("Combined Score:", combined_score)

        avg_score = sum(scores) / len(scores)

        assert avg_score > SIMILARITY_THRESHOLD, f"Average score too low: {avg_score}"
