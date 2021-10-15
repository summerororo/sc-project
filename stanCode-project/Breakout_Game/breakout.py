"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
name: Summer黃兆嘉
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.gui.events.mouse import onmouseclicked
from campy.graphics.gobjects import GLabel

FRAME_RATE = 1000 / 120 # 120 frames per second
NUM_LIVES = 3			# Number of attempts

# Global variable
graphics = BreakoutGraphics()
count = NUM_LIVES
switch_on_off = True


def main():
    onmouseclicked(click)


def click(event):
    global switch_on_off, count
    if switch_on_off:
        switch_on_off = False
        # Add animation loop here!
        while count > 0:
            pause(FRAME_RATE)
            graphics.ball.move(graphics.get_dx(), graphics.get_dy())
            # remove or change the direction if collide with an object
            graphics.ball_on_object()
            # wall reflection(up wall, right wall, left wall)
            graphics.wall_reflection()
            # game_out
            if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                count -= 1
                graphics.window.add(graphics.ball, x=graphics.ball_start_position_x, y=graphics.ball_start_position_y)
                switch_on_off = True
                if count == 0:
                    game_over = GLabel('Game Over!', x=115, y=400)
                    game_over.font = '-40'
                    graphics.window.add(game_over)
                break
            #  whether all bricks are removed
            if graphics.are_bricks_all_removed():
                break












if __name__ == '__main__':
    main()
