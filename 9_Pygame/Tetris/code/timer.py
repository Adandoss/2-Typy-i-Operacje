from settings import *

class Timer():
    def __init__(self, duration, repeated = False, func = None):

        # setup
        self.duration = duration
        self.repeated = repeated
        self.func = func

        self.active = False
        self.start_time = 0

    def activate(self):
        self.active = True
        self.start_time = pygame.time.get_ticks()      

    def deactivate(self):
        self.active = False
        self.start_time = 0

    def update(self):
        current_time = pygame.time.get_ticks()

        if current_time - self.start_time >= self.duration and self.active:
            # call a function
            if self.func and self.start_time != 0:
                self.func()

            # repeat timer
            if self.repeated:
                self.activate() 
            else:
                self.deactivate()

