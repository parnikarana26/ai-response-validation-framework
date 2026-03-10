# AI Response Validation Framework

This project demonstrates a testing framework for validating AI-generated chatbot responses.

## Problem

Traditional assertion-based testing fails for LLM responses because:
- AI responses are non-deterministic
- Same prompt can produce different valid outputs
- Synonyms and paraphrasing are common

## Features

- Integration with a real AI model via API
- Semantic similarity evaluation for response meaning
- Keyword-based validation for critical information coverage
- Handling non-deterministic responses by running multiple evaluations
- Threshold-based pass/fail evaluation
- Implemented using Python and PyTest

## Validation Approach

The framework validates AI responses using two primary evaluation methods.

1. Semantic Similarity

The generated response is compared with the expected answer using sentence embeddings. This helps determine whether both responses convey the same meaning even if the wording differs.

2. Keyword Matching

Important domain-specific keywords are defined for each prompt. The generated response is checked to ensure these keywords appear in the response.

3. Combined Evaluation Score

A final score is calculated as the average of:

Semantic similarity score

Keyword match score

The response passes the test if the average score exceeds a predefined threshold.

## Handling Non-Determinism

LLMs can generate slightly different responses for the same prompt. To reduce test flakiness:

Each prompt is evaluated three times

Scores from all runs are collected

The average score is used for final validation

This approach helps stabilize evaluation results.

## Architecture

Dataset → LLM → Response → Evaluation Engine → Pass/Fail

## Thresholds

- Similarity Threshold: 0.6
- Keyword Coverage Threshold: 0.5

## Note on API Rate Limits (429 Error)

During testing, a 429 Rate Limit Error may occur when the API usage exceeds the available quota or rate limits.

Example error:

429: You exceeded your current quota or rate limit.

This can happen due to:

- API usage limits on the OpenAI account
- High request frequency during automated test runs
- Missing or inactive billing configuration
- To address this:
- Ensure your API key is valid and active
- Verify billing or quota availability on the API provider platform
- Reduce request frequency if necessary

## Limitations
While this framework provides a useful automated evaluation strategy, it has several limitations:

- Semantic similarity may not detect factual inaccuracies
- Keyword validation checks presence but not correctness
- Threshold values may require tuning for different domains
- LLM responses may still vary significantly depending on model behavior
- Future improvements could include:
- Fact-checking mechanisms
- LLM-based evaluation (AI-as-a-judge)

## Technologies Used

- Python
- PyTest
- OpenAI API
- Sentence Transformers
- Natural Language Processing (NLP)
