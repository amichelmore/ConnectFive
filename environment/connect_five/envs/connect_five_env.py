import gym
from gym import error, spaces, utils
from gym.utils import seeding

class FooEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.state = []
        for i in range(19):
            self.state += [[]]
            for j in range(19):
                self.state[i] += [0]
        self.counter = 0
        self.done = 0
        self.first = 1
        self.turn = self.first
        self.score = [0, 0]
        self.reward = 0

    def check(self):
        if(self.counter<9):
            return 0
        for i in range(2,17):
            for j in range(2,17):
                if self.state[i,j] != 0:
                    if self.state[i,j] == self.state[i-2,j] and self.state[i,j] == self.state[i-1,j] and self.state[i,j] == self.state[i+1,j] and self.state[i,j] == self.state[i+2,j]:
                        return self.state[i,j]
                    elif self.state[i,j] == self.state[i,j-2] and self.state[i,j] == self.state[i,j-1] and self.state[i,j] == self.state[i,j+1] and self.state[i,j] == self.state[i,j+2]:
                        return self.state[i,j]
                    elif self.state[i,j] == self.state[i-2,j-2] and self.state[i,j] == self.state[i-1,j-1] and self.state[i,j] == self.state[i+1,j+1] and self.state[i,j] == self.state[i+2,j+2]:
                        return self.state[i,j]
                    elif self.state[i,j] == self.state[i-2,j+2] and self.state[i,j] == self.state[i-1,j+1] and self.state[i,j] == self.state[i+1,j-1] and self.state[i,j] == self.state[i+2,j-2]:
                        return self.state[i,j]

        for i in range(0,2):
            for j in range(2,17):
                if self.state[i,j] != 0:
                    if self.state[i,j] == self.state[i,j-2] and self.state[i,j] == self.state[i,j-1] and self.state[i,j] == self.state[i,j+1] and self.state[i,j] == self.state[i,j+2]:
                        return self.state[i,j]

        for i in range(2,17):
            for j in range(0,2):
                if self.state[i,j] != 0:
                    if self.state[i,j] == self.state[i-2,j] and self.state[i,j] == self.state[i-1,j] and self.state[i,j] == self.state[i+1,j] and self.state[i,j] == self.state[i+2,j]:
                        return self.state[i,j]

        return[0]

    def step(self, action):
        i = int(action/19)
        j = action%19
        if self.done == 1:
            print("Game Over")
            return [self.state, self.reward, self.done, self.add]
        elif self.state[i, j] != 0:
            print("Invalid Step")
            return [self.state, self.reward, self.done, self.add]
        else:
            self.state[i,j] = self.turn
            self.counter += 1
            if(self.counter == 361):
                self.done = 1
            if self.turn == 1:
                self.turn = -1
            else:
                self.turn = 1
            self.render()

        win = self.check()
        if(win != 0):
            self.done = 1
            print(win, " wins!", sep = "", end = "\n")
            if win == 1:
                self.score[0] += 1
            else:
                self.score[1] += 1
            if win == -1:
                self.reward = 1
            else:
                self.reward = -1
            #work on this

        return [self.state, self.reward, self.done, self.add]


    def reset(self):
        #printing the board in a somewhat pretty way
        for i in range(19):
            for j in range(19):
                self.state[i][j] = 0
        self.counter = 0
        self.done = 0
        if self.first == 1:
            self.first = -1
            self.turn = self.first
        else:
            self.first = 1
            self.turn = self.first
        self.reward = 0
        return self.state

    def render(self, mode='human', close=False):
        #printing the board in a somewhat pretty way
        print('\n')
        print(self.turn, ' to move.')
        print(' ', end='  ')
        print(' ', end='  ')
        for i in range(19):
            if i < 10:
                print(i, end='  ')
            else:
                print(i, end=' ')
        print('')
        print(' ', end='  ')
        print(' ', end='  ')
        for i in range(19):
            print('_', end='  ')
        print('')
        for i in range(19):
            if i < 10:
                print(i, end='  ')
            else:
                print(i, end=' ')
            print('|', end='  ')
            for j in range(19):
                # printing value at each point 
                if(self.state == 1):
                    out = '\u25CB'
                elif(self.state == -1):
                    out = '\u25CF'
                else:
                    out = ' '
                print(out, end='  ')
            print('|')
        print(' ', end='  ')
        print(' ', end='  ')
        for i in range(19):
            print('_', end='  ')
        print('\n')