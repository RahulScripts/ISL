# ------------------- KNOWLEDGE BASE -------------------

knowledge_base = {
    "cold": {"sneezing", "runny nose", "sore throat"},
    "flu": {"fever", "body pain", "headache"},
    "diabetes": {"frequent urination", "excessive thirst", "fatigue"},
    "covid": {"fever", "dry cough", "loss of taste"},
    "tuberculosis": {"persistent cough", "weight loss", "night sweats"}
}

# ----------------- INFERENCE ENGINE -------------------

def infer(symptoms):
    symptoms = set(symptoms)
    scores = {}

    for disease, req in knowledge_base.items():
        scores[disease] = len(req & symptoms) / len(req)

    best = max(scores, key=scores.get)
    confidence = scores[best]

    if confidence == 0:
        return "No match found"
    elif confidence < 0.5:
        return f"Possibility of {best} (low confidence: {confidence*100:.1f}%)"
    else:
        return f"Diagnosed: {best} (confidence {confidence*100:.1f}%)"

# -------------------- INPUT SECTION --------------------

def main():
    print("Enter symptoms separated by commas:")
    s = input().lower()
    symptoms = [x.strip() for x in s.split(",")]
    print(infer(symptoms))

if __name__ == "__main__":
    main()
