class Agent:
    def __init__(self, attributes):
        self.emotions = attributes[0]  # Emotions (e.g., happiness, sadness, fear)
        self.personality = attributes[1]  # Personality (e.g., Extravert, Openness, Neuroticism)
        self.physical_exhaustion = attributes[2]  # Physical Exhaustion
        self.interest = attributes[3]  # Interest (e.g., Realistic, Investigative, Artistic, etc.)
        self.culture_preference = attributes[4]  # Culture Preference
        self.dynamic_emotion = attributes[5]  # Dynamic Emotion
        self.positive_affect = attributes[6]  # Positive Affect
        self.short_term_willingness = attributes[7]  # Short-Term Willingness to Interact
        self.long_term_willingness = attributes[8]  # Long-Term Willingness to Interact
        self.readiness_to_interact = attributes[9]  # Readiness to Interact
        self.similarity_culture = attributes[10]  # Similarity of Culture between Agent i and j
        self.similarity_interest = attributes[11]  # Similarity of Interest between Agent i and j
        self.environment = attributes[12]  # Environment
        self.range_of_content = attributes[13]  # Range of Content

# Example usage:
attributes = [0.5, 0.7, 0.2, 0.8, 0.6, 0.4, 0.9, 0.3, 0.5, 0.7, 0.8, 0.6, 0.4, 0.9]
agent = Agent(attributes)
print(agent.emotions)  # Output: 0.5
