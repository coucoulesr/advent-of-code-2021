class LanternFishSchool:
    def __init__(self):
        self.fish = []

    def add_fish(self, timer=8):
        self.fish.append(LanternFish(timer))
    
    def tick(self):
        new_fish_count = 0
        for fish in self.fish:
            if fish.should_spawn():
                new_fish_count += 1
            fish.tick()
        for _ in range(new_fish_count):
            self.add_fish()


class LanternFish:
    def __init__(self, timer=8):
        self.timer = timer
    
    def __repr__(self):
        return str(self.timer)
    
    def tick(self):
        if self.timer == 0:
            self.timer = 7
        self.timer -= 1
    
    def should_spawn(self):
        return self.timer == 0


def part1():
    school = LanternFishSchool()
    with open('input06', 'r') as f:
        fish_timers = [int(val.strip()) for val in f.readline().split(',')]
        for timer in fish_timers:
            school.add_fish(timer)
    for _ in range(80):
        school.tick()
    return len(school.fish)

def part2():
    fish_on_day = [0] * 9 # Maps days until spawn -> number of fish
    with open('input06', 'r') as f:
        fish_timers = [int(val.strip()) for val in f.readline().split(',')]
        for timer in fish_timers:
            fish_on_day[timer] += 1
    for _ in range(256):
        new_fish = fish_on_day[0] # Number of new fish to spawn
        
        # Decrement fish
        for i in range(8):
           fish_on_day[i] = fish_on_day[i+1]
        
        fish_on_day[6] += new_fish # Reset old fish
        fish_on_day[8] = new_fish  # Spawn new fish
    return sum(fish_on_day)

print(part1())
print(part2())