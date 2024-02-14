import random

class Snake:
    start = 0
    end = 0
    def __init__(self, x, y):
        self.start = x
        self.end = y

    def __repr__(self)->str:
        s = "" + str(self.start) + "->" + str(self.end)
        return s

class Ladder:
    start = 0
    end = 0
    def __init__(self, x, y):
        self.start = x
        self.end = y

    def __repr__(self)->str:
        s = "" + str(self.start) + "->" + str(self.end)
        return s


class Board: 
    size = 0
    n_ladders = 0
    n_snakes = 0
    ladders = []
    snakes = []
    def __init__(self, size):
        self.size = size
        self.n_ladders = random.randint(5, 10)
        self.n_snakes = random.randint(5, 10)
        for _ in range(self.n_ladders): 
            while True : 
                x = random.randint(1, self.size-1)
                y = random.randint(1, self.size-1)
                if x==y: 
                    continue
                elif x>y:
                    tmp = y
                    y = x
                    x = tmp
                exists = self._check_existing(x, y)
                if not exists:
                    self.ladders.append(Ladder(x, y))
                    break

        for _ in range(self.n_snakes): 
            while True : 
                x = random.randint(1, self.size-1)
                y = random.randint(1, self.size-1)
                if x==y: 
                    continue
                elif x<y:
                    tmp = y
                    y = x
                    x = tmp
                exists = self._check_existing(x, y)
                if not exists:
                    self.snakes.append(Snake(x, y))
                    break
        
        print("board size", size)
        print("n_ladders", self.n_ladders)
        print("n_snakes", self.n_snakes)
        print("ladders", self.ladders)
        print("snakes", self.snakes)
    
    def _check_existing(self, x, y):
        for ladder in self.ladders:
            if ladder.start==x or ladder.end==y or ladder.start==y or ladder.end==x : 
                return 1
        for snake in self.snakes:
            if snake.start==x or snake.end==y or snake.start==y or snake.end==x : 
                return 1
        return 0

class Dice: 
    faces = 0
    def __init__(self, faces):
        self.faces = faces
    def roll(self) -> int:
        result = random.randint(1, self.faces)
        return result

class Player:
    player_id = 0
    position = 0
    won = 0
    def __init__(self, player_id):
        self.player_id = player_id

    def move(self, board, dice):
        result = dice.roll()
        print("Player {} at {} got {} on dice".format(self.player_id, self.position, result))

        new_position = self.position + result
        if new_position > board.size:
            pass
        elif new_position == board.size:
            self.position = new_position
            self.won = 1
        else:
            self.position = new_position

        for ladder in board.ladders:
            if ladder.start==self.position:
                self.position = ladder.end
                print("Player {} took ladder |||||||||||| {}".format(self.player_id, ladder))

        for snake in board.snakes:
            if snake.start==self.position:
                self.position = snake.end
                print("Player {} bit by snake ---------- {}".format(self.player_id, snake))

        print("Player {} moved to {}".format(self.player_id, self.position))
        
    