from settings import *
from random import choice
from time import sleep

from timer import Timer

class Game():

    def __init__(self, get_next_shape):

        # general 
        self.surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.display_surface = pygame.display.get_surface()
        self.rect = self.surface.get_rect()
        self.sprites = pygame.sprite.Group()

        # score
        self.current_lines = 0
        self.current_score = 0

        # game connection
        self.get_next_shape = get_next_shape

        # tetromino
        self.field_data = [[0 for x in range(COLUMNS)] for y in range(ROWS)]
        self.tetromino = Tetromino(
            self.get_next_shape(), 
            self.sprites, 
            self.create_new_tetromino,
            self.field_data)

        # timers
        self.down_pressed = False
        self.timers = {
            'vertical_move': Timer(VERTICAL_MOVE_SPEED, True, self.move_down),
            'horizontal_move': Timer(MOVE_WAIT_TIME),
            'rotate': Timer(ROTATE_WAIT_TIME)
        }
        for timer in self.timers.values():
            timer.activate()


    def calculate_score(self, num_lines):
        self.current_lines += num_lines
        self.current_score += SCORE_DATA[num_lines]

    def draw_grid(self):

        width = self.surface.get_width()
        height = self.surface.get_height()

        for col in range(1, COLUMNS):
            pygame.draw.line(self.surface, LIGHT_GREY, (col * CELL_SIZE, 0), (col * CELL_SIZE, height), 1)

        for row in range(1, ROWS):
            pygame.draw.line(self.surface, LIGHT_GREY, (0, row * CELL_SIZE), (width, row * CELL_SIZE), 1)

        pygame.draw.rect(self.surface, WHITE, self.rect, 2, 2)


    def run(self):

        # updating 
        self.input()
        self.update_timers()
        self.sprites.update()

        # drawing
        self.surface.fill(BLACK)
        self.sprites.draw(self.surface)
        self.draw_grid()
        self.display_surface.blit(self.surface, (PADDING, PADDING))

        # return score to Main class
        return self.current_score, self.current_lines

    def move_down(self):
        self.tetromino.move_down()

    def input(self):
        keys = pygame.key.get_pressed()

        # horizontal movement
        if not self.timers['horizontal_move'].active:
            if keys[pygame.K_RIGHT]:
                self.tetromino.move_horizontal(RIGHT)
                self.timers['horizontal_move'].activate()
            elif keys[pygame.K_LEFT]:
                self.tetromino.move_horizontal(LEFT)
                self.timers['horizontal_move'].activate()

        # down speedup
        if not self.down_pressed and keys[pygame.K_DOWN]:
            self.down_pressed = True
            self.timers['vertical_move'].duration = FAST_VERTICAL_MOVE_SPEED

        if self.down_pressed and not keys[pygame.K_DOWN]:
            self.down_pressed = False
            self.timers['vertical_move'].duration = VERTICAL_MOVE_SPEED

        # rotation
        if not self.timers['rotate'].active:
            if keys[pygame.K_UP]:
                self.tetromino.rotate()
                self.timers['rotate'].activate()

    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    def check_game_over(self):
        for block in self.tetromino.blocks:
            # if we lost, reset game
            if block.pos.y < 0:
                sleep(1)
                self.__init__(self.get_next_shape)
                for sprite in self.sprites:
                    sprite.kill()
                
    def create_new_tetromino(self):
        self.check_game_over()
        self.check_finished_rows()
        self.tetromino = Tetromino(
            self.get_next_shape(), 
            self.sprites, 
            self.create_new_tetromino,
            self.field_data)
    
    def check_finished_rows(self):

        # get row indexes
        delete_rows = []
        for i, row in enumerate(self.field_data):
            if all(row):
                delete_rows.append(i)
            
        if delete_rows:
            for delete_row in delete_rows:

                # delete blocks
                for block in self.field_data[delete_row]:
                    block.kill()
                for col in range(COLUMNS):
                    self.field_data[delete_row][col] = 0
                
                # move blocks down
                for row_i, row in enumerate(self.field_data):
                    for block in row:
                        if block and block.pos.y < delete_row:
                            block.pos.y += 1
                    if row_i < delete_row:
                        self.field_data[delete_row - row_i] = list(
                            self.field_data[delete_row - row_i - 1])
                    self.field_data[0] = [0] * COLUMNS

            # update score
            self.calculate_score(len(delete_rows))

    

class Tetromino():
    def __init__(self, shape, sprite_group, create_new_tetromino, field_data):

        # setup
        self.block_positions = TETROMINOS[shape]['shape']
        self.color = TETROMINOS[shape]['color']
        self.shape = shape
        self.create_new_tetromino = create_new_tetromino
        self.sprite_group = sprite_group
        self.field_data = field_data

        # blocks 
        self.blocks = [Block(sprite_group, pos, self.color) for pos in self.block_positions]
        

    # collisions
    def next_vertical_move_collides(self):
        block_x_pos_list = [int(block.pos.x) for block in self.blocks]
        block_y_pos_list = [int(block.pos.y + 1) for block in self.blocks]
        for y, x in zip(block_y_pos_list, block_x_pos_list):
            # if self.field_data[int(y)][int(x)] != 0, that means
            # it's already occupied by another block
            if y >= ROWS or (self.field_data[y][x] and y >= 0):
                print("Vertical Collides!")
                return True
        return False

    def next_horizontal_move_collides(self, direction):
        block_x_pos_list = [int(block.pos.x + direction) for block in self.blocks]
        block_y_pos_list = [int(block.pos.y) for block in self.blocks]
        for y, x in zip(block_y_pos_list, block_x_pos_list):
            if x < 0 or x >= COLUMNS or self.field_data[y][x]: 
                print("Horizontal Collides!")
                return True   
        return False

    # movement
    def move_down(self):
        
        if not self.next_vertical_move_collides():
            for block in self.blocks:
                block.pos.y += 1
        else:
            for block in self.blocks:
                self.field_data[int(block.pos.y)][int(block.pos.x)] = block
            self.create_new_tetromino()

    def move_horizontal(self, direction):
        if not self.next_horizontal_move_collides(direction):
            for block in self.blocks:
                block.pos.x += direction # RIGHT == 1, LEFT == -1

    def rotate(self):
        if self.shape == 'O':
            return
        
        # 1. pivot point
        pivot_pos = self.blocks[0].pos

        # 2 new block positions
        new_block_positions = [block.rotate(pivot_pos) for block in self.blocks]

        # 3 collision check
        for pos in new_block_positions:
            # horizontal
            if pos.x < 0 or pos.x >= COLUMNS:
                return

            # vertical
            if pos.y <= 0:
                return

            # field check --> collision with oter pieces
            if self.field_data[int(pos.y)][int(pos.x)]:
                return

        # 4 implement new positions
        for i, block in enumerate(self.blocks):
            block.pos = new_block_positions[i]


class Block(pygame.sprite.Sprite):
    def __init__(self, group, pos, color):

        # general
        super().__init__(group)
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill(color)

        # position
        self.pos = pygame.Vector2(pos) + BLOCK_OFFSET
        self.rect = self.image.get_rect(topleft = self.pos * CELL_SIZE)

    def rotate(self, pivot_pos):
        distance = self.pos - pivot_pos
        rotated = distance.rotate(90)
        new_pos = pivot_pos + rotated
        return new_pos

    def update(self):
        self.rect.topleft = self.pos * CELL_SIZE


