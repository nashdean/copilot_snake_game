class Difficulty:
    def __init__(self, speed, num_obstacles, isBorder):
        self.speed = speed
        self.num_obstacles = num_obstacles
        self.isBorder = isBorder
class Classic(Difficulty):
    def __init__(self):
        super().__init__(speed=10, num_obstacles=0, isBorder=False)

class Easy(Difficulty):
    def __init__(self):
        super().__init__(speed=10, num_obstacles=5, isBorder=True)

class Medium(Difficulty):
    def __init__(self):
        super().__init__(speed=15, num_obstacles=10, isBorder=True)

class Hard(Difficulty):
    def __init__(self):
        super().__init__(speed=25, num_obstacles=15, isBorder=True)

class Insane(Difficulty):
    def __init__(self):
        super().__init__(speed=40, num_obstacles=20, isBorder=True)