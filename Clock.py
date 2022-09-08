from time import time
from inspect import currentframe, getframeinfo

class Clock():

    def __init__(self):

        """ Constructor of Clock class"""

        # Initialise laps
        self.laps = []

        # Initialise rows
        self.rows = []

        # Initialise lap counter
        self.n_laps = 0


    def lap(self):

        # Store time at which clock is called
        self.laps.append(time())

        # Increase number of laps
        self.n_laps +=1

        # Store row number where the clock is called
        self.rows.append(currentframe().f_back.f_lineno)

    def summary(self):

        # Computer number of blocks
        self.n_blocks = self.n_laps - 1

        # Start writing summary
        print("\nCLOCK RESULTS ")
        print(f"Number of blocks: {self.n_blocks}")
        for n in range(self.n_blocks):

            # Print timing and involved rows for each block
            print(f"Block {n + 1}: {self.laps[n + 1] - self.laps[n]}; Rows {self.rows[n]} to {self.rows[n + 1]}")



