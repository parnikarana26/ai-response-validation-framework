def keyword_match(response, keywords):
    """
    Checks if important keywords exist in the AI response
    """

    response = response.lower()

    matched = 0

    for keyword in keywords:
        if keyword.lower() in response:
            matched += 1

    return matched / len(keywords)
