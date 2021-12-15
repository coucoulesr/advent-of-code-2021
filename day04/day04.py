class Bingo:
    def __init__(self, board=None):
        self.board = board if board else [[None] * 5] * 5
        self.won = False
        self.score = None
        self.turn = 0

    def print(self):
        for row in self.board:
            print(" ".join([f'{int(val):4d}' for val in row]))

    def set_board(self, board):
        self.board = board

    def has_won(self):
        return self.won

    def get_score(self):
        return self.score

    def get_turn(self):
        return self.turn

    def draw(self, num):
        if self.won: return
        for r_idx, row in enumerate(self.board):
            if num in row:
                c_idx = row.index(num)
                self.board[r_idx][c_idx] *= -1
                if self.board[r_idx][c_idx] == 0:
                    self.board[r_idx][c_idx] = float(0)
                if self._move_wins(r_idx, c_idx):
                    self.won = True
                    self._calc_score(r_idx, c_idx)
        self.turn += 1
    
    def _row_wins(self, y):
        return all([val < 0 or isinstance(val, float) for val in self.board[y]])
    
    def _col_wins(self, x):
        return all([row[x] < 0 or isinstance(row[x], float) for row in self.board])

    def _move_wins(self, y, x):
        return self._row_wins(y) or self._col_wins(x)

    def _calc_score(self, y, x):
        unmarked_sum = 0
        for row in self.board:
            for val in row:
                if val > 0:
                    unmarked_sum += val
        self.score = -1 * self.board[y][x] * unmarked_sum

def part1():
    nums = []
    boards = []
    bingos = []
    with open('input04', 'r') as f:
        nums = [int(val.strip()) for val in f.readline().split(',')]
        line = f.readline()
        while line:
            board = []
            for _ in range(5):
                row = f.readline().strip().split(' ')
                board.append([int(val) for val in row if val != ''])
            boards.append(board)
            line = f.readline()
    for board in boards:
        bingos.append(Bingo(board))
    for num in nums:
        for bingo in bingos:
            bingo.draw(num)
            if bingo.has_won():
                return bingo.get_score()
            
def part2():
    nums = []
    boards = []
    bingos = []
    with open('input04', 'r') as f:
        nums = [int(val.strip()) for val in f.readline().split(',')]
        line = f.readline()
        while line:
            board = []
            for _ in range(5):
                row = f.readline().strip().split(' ')
                board.append([int(val) for val in row if val != ''])
            boards.append(board)
            line = f.readline()
    for board in boards:
        bingos.append(Bingo(board))
    for num in nums:
        for bingo in bingos:
            bingo.draw(num)
    last_bingo = Bingo()
    for bingo in bingos:
        if bingo.has_won() and bingo.get_turn() > last_bingo.get_turn():
            last_bingo = bingo
    return last_bingo.get_score()

print(part1())
print(part2())