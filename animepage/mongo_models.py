from django.conf import settings

class Vote:
    def __init__(self, name, score, observation):
        self.name = name
        self.score = score
        self.observation = observation

    def to_dict(self):
        return {
            "name": self.name,
            "score": self.score,
            "observation": self.observation
        }
