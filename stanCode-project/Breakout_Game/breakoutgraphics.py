"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
name: Summer黃兆嘉
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.

BRICK_COLORS = ['darkslategray', 'lightseagreen', 'turquoise', 'paleturquoise', 'lightcyan']

# Global variable
brick_count = BRICK_ROWS*BRICK_COLS
score = 0
score_label = GLabel(f"Score: {str(score)}")


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        self.row = brick_rows
        self.col = brick_cols

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.color = 'cyan'
        self.paddle.fill_color = 'cyan'
        self.window.add(self.paddle, x=(window_width-paddle_width)/2, y=window_height-paddle_height-paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.ball.color = 'grey'
        self.ball.fill_color = 'grey'
        self.window.add(self.ball, x=(window_width-ball_radius*2)/2, y=(window_height-ball_radius*2)/2)
        self.ball_start_position_x = (window_width-ball_radius*2)/2
        self.ball_start_position_y = (window_height-ball_radius*2)/2

        # Default initial velocity for the ball
        self._dy = INITIAL_Y_SPEED
        self._dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self._dx *= -1

        # Initialize our mouse listeners
        onmousemoved(self.move)

        # Put in the bricks
        color_index = -1
        for row in range(BRICK_ROWS):
            if row % 2 == 0:
                color_index += 1
            for col in range(BRICK_COLS):
                brick = GRect(BRICK_WIDTH, BRICK_HEIGHT,
                              x=col * (BRICK_WIDTH + BRICK_SPACING),
                              y=BRICK_OFFSET + row * (BRICK_HEIGHT+BRICK_SPACING))
                brick.filled = True
                color = BRICK_COLORS[color_index % len(BRICK_COLORS)]
                brick.fill_color = color
                brick.color = color
                self.window.add(brick)

        # score label
        score_label.font = '-30'
        self.window.add(score_label, 0, score_label.height)

    # Getter dx
    def get_dx(self):
        return self._dx

    # Getter dy
    def get_dy(self):
        return self._dy

    # Move the paddle
    def move(self, mouse):
        if self.paddle.width/2 < mouse.x < self.window.width-self.paddle.width/2:
            self.window.add(self.paddle, x=mouse.x-(self.paddle.width/2),
                            y=self.window.height-self.paddle.height-PADDLE_OFFSET)
        elif mouse.x <= self.paddle.width/2:
            self.window.add(self.paddle, x=0, y=self.window.height-self.paddle.height-PADDLE_OFFSET)
        elif mouse.x >= self.window.width-self.paddle.width/2:
            self.window.add(self.paddle, x=self.window.width-self.paddle.width,
                            y=self.window.height-self.paddle.height-PADDLE_OFFSET)

    # 是否有碰到paddle或brick，有的話則改變方向或消除物件
    def ball_on_object(self):
        global brick_count, score

        first = self.window.get_object_at(self.ball.x, self.ball.y)
        second = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y)
        third = self.window.get_object_at(self.ball.x+self.ball.height, self.ball.y+self.ball.height)
        fourth = self.window.get_object_at(self.ball.x, self.ball.y+self.ball.height)
        if self.ball.y + self.ball.height >= self.window.height-15:
            pass
        else:
            if first is not None:
                self._dy *= -1
                self.window.remove(first)
                brick_count -= 1
                score += 1
            elif second is not None:
                self._dy *= -1
                self.window.remove(second)
                brick_count -= 1
                score += 1
            elif third is not None:
                if third == self.paddle:
                    self._dy *= -1
                else:
                    self._dy *= -1
                    self.window.remove(third)
                    brick_count -= 1
                    score += 1
            elif fourth is not None:
                if fourth == self.paddle:
                    self.window.add(self.ball, x=self.ball.x, y=self.paddle.y+self.ball.height)  #解決球卡在paddle的問題
                    self._dy *= -1
                else:
                    self._dy *= -1
                    self.window.remove(fourth)
                    brick_count -= 1
                    score += 1
        # score label
        score_label.text = 'Score: ' + str(score)

    # wall reflection
    def wall_reflection(self):
        if self.ball.x + self.ball.width >= self.window.width or self.ball.x <= 0:
            self._dx *= -1
        elif self.ball.y <= 0:
            self._dy *= -1

    # count the bricks
    @staticmethod
    def are_bricks_all_removed():
        global brick_count
        if brick_count == 0:
            return True














































