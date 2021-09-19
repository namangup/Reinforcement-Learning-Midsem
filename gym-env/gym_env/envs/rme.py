import gym
from gym import spaces

class RandomMazeEnvironment(gym.Env):
    
    def __init__(self, rng):
        self.np_random = rng
        self.action_space = spaces.Discrete(4) # up, right, down, left
        self.observation_space = spaces.Discrete(12)
        self.state = 8 # start state


    def up(self):
        if not self.state in [0, 1, 2, 3, 9]: # top row and cell below the wall
            self.state -= 4
    
    def right(self):
        if not self.state in [3, 7, 11, 4]: # right column and cell left to the wall
            self.state += 1

    def left(self):
        if not self.state in [0, 4, 8, 6]: # left column and cell right to the wall
            self.state -= 1

    def down(self):
        if not self.state in [8, 9, 10, 11, 1]: # bottom row and cell above the wall
            self.state += 4


    def step(self, action, print_flag=False):
        p = self.np_random.uniform()
        prev_state = self.state
        if action == 0: # up
            if p < 0.8: # up
                self.up()
            elif p >= 0.8 and p < 0.9: #right
                self.right()
            else: # left
                self.left()
        elif action == 1: # right
            if p < 0.8: # right
                self.right()
            elif p >= 0.8 and p < 0.9: # down
                self.down()
            else: # up
                self.up()
        elif action == 2: # down
            if p < 0.8: # down
                self.down()
            elif p >= 0.8 and p < 0.9: # left
                self.left()
            else: # right
                self.right()
        else: # left
            if p < 0.8: # left
                self.left()
            elif p >= 0.8 and p < 0.9: # up
                self.up()
            else: # down
                self.down()
        
        if print_flag:
            print(prev_state, action, p, self.state)

        if self.state == 3: # goal
            return self.state, 1, True, {}
        
        if self.state == 7: # hole
            return self.state, -1, True, {}

        return self.state, -0.04, False, {}

    def reset(self):
        self.state = 8
        return self.state
