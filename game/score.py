import yaml
import os

class Score:
    def __init__(self, filename='high_scores.yaml'):
        self.filename = filename
        self.current_score = 0 
        self.scores = self.load_scores()

    def load_scores(self):
        if not os.path.exists(self.filename):
            return {
                'Easy': {'Border': [], 'No Border': []},
                'Medium': {'Border': [], 'No Border': []},
                'Hard': {'Border': [], 'No Border': []},
                'Insane': {'Border': [], 'No Border': []},
                'Classic': {'Border': [], 'No Border': []}
            }
        with open(self.filename, 'r') as file:
            return yaml.safe_load(file)
        
    def increase_current_score(self):
        self.current_score += 1
    
    def save_scores(self):
        with open(self.filename, 'w') as file:
            yaml.safe_dump(self.scores, file)

    def add_score(self, difficulty, score, is_border):
        mode = 'Border' if is_border else 'No Border'
        if difficulty not in self.scores:
            self.scores[difficulty] = {'Border': [], 'No Border': []}
        self.scores[difficulty][mode].append(score)
        self.scores[difficulty][mode] = sorted(self.scores[difficulty][mode], reverse=True)[:10]
        self.save_scores()

    def get_high_score(self, difficulty, is_border):
        mode = 'Border' if is_border else 'No Border'
        if difficulty in self.scores and self.scores[difficulty][mode]:
            return self.scores[difficulty][mode][0]
        return 0