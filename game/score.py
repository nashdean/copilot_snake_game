import yaml
import os

class Score:
    def __init__(self, filename='high_scores.yaml'):
        self.filename = filename
        self.scores = self.load_scores()

    def load_scores(self):
        if not os.path.exists(self.filename):
            return {'Easy': [], 'Medium': [], 'Hard': [], 'Insane': []}
        with open(self.filename, 'r') as file:
            return yaml.safe_load(file)

    def save_scores(self):
        with open(self.filename, 'w') as file:
            yaml.safe_dump(self.scores, file)

    def add_score(self, difficulty, score):
        if difficulty not in self.scores:
            self.scores[difficulty] = []
        self.scores[difficulty].append(score)
        self.scores[difficulty] = sorted(self.scores[difficulty], reverse=True)[:10]
        self.save_scores()

    def get_high_score(self, difficulty):
        if difficulty in self.scores and self.scores[difficulty]:
            return self.scores[difficulty][0]
        return 0