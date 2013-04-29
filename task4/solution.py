import re


class InvalidMove(Exception):
    pass


class InvalidValue(Exception):
    pass


class InvalidKey(Exception):
    pass


class NotYourTurn(Exception):
    pass


class TicTacToeBoard(dict):

    def __init__(self, players=None, columns=None, rows=None):
        self.players = players or ('X', 'O')
        self.columns = columns or ('A', 'B', 'C')
        self.rows = rows or range(1, 4)
        self.moves = []
        self.cells_count = len(self.columns) * len(self.rows)

    def __str__(self):
        row_separator = '\n  ' + '-' * int(4 * len(self.columns) + 1) + '\n'
        board_string = row_separator
        for row in reversed(self.rows):
            board_string += '%d |' % row
            for column in self.columns:
                board_string += ' %s |' % dict(
                    self.moves).get('%s%d' % (column, row), ' ')
            board_string += row_separator
        board_string += '   ' + ' '.join(
            [' %s ' % column for column in self.columns]) + ' \n'
        return board_string

    def game_status(self):
        cols = self.columns
        rows = self.rows
        win = [['%s%d' % (col, row) for col in cols] for row in rows] +\
              [['%s%d' % (col, row) for row in rows] for col in cols] +\
              [['%s%d' % (col, dep+1) for dep, col in enumerate(cols)]] +\
              [['%s%d' % (col, dep+1)
                for dep, col in enumerate(reversed(cols))]]
        for player in self.players:
            if any([all([dict(self.moves).get(pattern_item) == player
                    for pattern_item in pattern]) for pattern in win]):
                return '%s wins!' % player
        if len(self.moves) == self.cells_count:
            return 'Draw!'
        else:
            return 'Game in progress.'

    def __setitem__(self, key, value):
        if key in self.keys():
            raise InvalidMove()
        if value not in self.players:
            raise InvalidValue()
        if not re.match('^[%s-%s][%d-%d]$' % (self.columns[0],
                                              self.columns[-1],
                                              self.rows[0],
                                              self.rows[-1]), key):
            raise InvalidKey()
        if self.moves and self.moves[-1][1] == value:
            raise NotYourTurn()

        self.moves.append((key, value))
        return dict.__setitem__(self, key, value)
