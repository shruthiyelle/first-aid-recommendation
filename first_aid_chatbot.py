import openai

def get_first_aid_recommendation(symptom):
    # This is a placeholder function that mimics getting recommendations
    recommendations = {
        "burn": "Cool the burn under cold running water for at least 10 minutes. Do not apply ice or creams.",
        "cut": "Clean the wound with running water. Apply pressure to stop bleeding, then cover with a sterile bandage.",
        "choking": "Perform the Heimlich maneuver if the person cannot breathe. Call emergency services if needed.",
        "sprain": "Rest the injured area, apply ice, compress with a bandage, and elevate the limb.",
        "fever": "Keep hydrated, rest, and monitor the temperature. Seek medical advice if fever persists."
    }
    return recommendations.get(symptom.lower(), "I'm not sure about that symptom. Please seek medical advice.")

def main():
    print("Welcome to the First Aid Recommendation Chatbot!")
    print("Type 'exit' to stop.")
    
    while True:
        symptom = input("What symptom are you experiencing? ")
        
        if symptom.lower() == 'exit':
            print("Take care! Goodbye.")
            break
        
        recommendation = get_first_aid_recommendation(symptom)
        print(f"First aid recommendation: {recommendation}")

if __name__ == "__main__":
    main()
