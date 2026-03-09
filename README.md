# AI Response Validation Framework

This project demonstrates a testing framework for validating AI-generated chatbot responses.

## Problem

Traditional assertion-based testing fails for LLM responses because:
- AI responses are non-deterministic
- Same prompt can produce different valid outputs
- Synonyms and paraphrasing are common

## Validation Approach

This framework validates responses using:

1. Semantic Similarity
Compares the meaning of expected and generated responses using sentence embeddings.

2. Keyword Validation
Ensures critical keywords appear in the response.

3. Multiple Execution Runs
Each prompt is executed multiple times and average score is used to reduce flakiness.

## Architecture

Dataset → LLM → Response → Evaluation Engine → Pass/Fail

## Thresholds

- Similarity Threshold: 0.65
- Keyword Coverage Threshold: 0.5

## Limitations

- Embedding models may misinterpret context
- Keyword checks may miss paraphrased answers
- Running multiple tests increases API cost
- LLM responses can still vary significantly
