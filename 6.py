# Knowledge-Based Inference System for disease diagnosis

# === KNOWLEDGE BASE ===
knowledge_base = {
    "cold": {
        "sneezing",
        "runny nose",
        "sore throat"
    },
    "flu": {
        "fever",
        "body pain",
        "headache"
    },
    "diabetes": {
        "frequent urination",
        "excessive thirst",
        "fatigue"
    }
}

# === INFERENCE ENGINE ===
def infer(known_symptoms):
    scores = {}

    for disease, required in knowledge_base.items():
        scores[disease] = len(required.intersection(known_symptoms)) / len(required)

    best_match = max(scores, key=scores.get)
    confidence = scores[best_match]

    if confidence == 0:
        return "No matching disease found"
    elif confidence < 0.5:
        return f"Inconclusive. Possible early symptoms of {best_match}"
    else:
        return f"Diagnosed: {best_match} (confidence: {confidence*100:.1f}%)"


# === MAIN DIALOG SYSTEM ===
def main():
    print("Enter symptoms separated by commas:")
    user_input = input().lower()
    symptoms = set([x.strip() for x in user_input.split(",")])

    print(infer(symptoms))

if __name__ == "__main__":
    main()
