class Difficulty:
    def __init__(self, speed, num_obstacles):
        self.speed = speed
        self.num_obstacles = num_obstacles

class Easy(Difficulty):
    def __init__(self):
        super().__init__(speed=10, num_obstacles=5)

class Medium(Difficulty):
    def __init__(self):
        super().__init__(speed=15, num_obstacles=10)

class Hard(Difficulty):
    def __init__(self):
        super().__init__(speed=25, num_obstacles=15)

class Insane(Difficulty):
    def __init__(self):
        super().__init__(speed=40, num_obstacles=20)