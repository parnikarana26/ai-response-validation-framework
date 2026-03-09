from sentence_transformers import SentenceTransformer, util

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

def similarity_score(expected, actual):
    """
    Calculate semantic similarity between expected and actual responses
    """

    emb1 = model.encode(expected)
    emb2 = model.encode(actual)

    score = util.cos_sim(emb1, emb2)

    return float(score)
