from time import time
from inspect import currentframe, getframeinfo

class Clock():

    def __init__(self):

        """ Constructor of Clock class"""

        # Initialise laps
        self.laps = []

        # Initialise names
        self.names = []

        # Initialise rows
        self.rows = []

        # Initialise lap counter
        self.n_laps = 0


    def lap(self, name='Block'):

        # Store time at which clock is called
        self.laps.append(time())

        # Increase number of laps
        self.n_laps +=1

        # Store row number where the clock is called
        self.rows.append(currentframe().f_back.f_lineno)

        # Store name
        self.names.append(name)


    def timings(self, initial_block, final_block):

        """ Compute timings for various blocks """

        # Ensure they are correctly ordered
        if initial_block > final_block:
            print("Error: fix block number!")
            return

        # Compute timings
        block_timings = [self.laps[n] - self.laps[n-1] for n in range(initial_block, final_block + 1)]

        return block_timings



    def summary(self):

        # Computer number of blocks
        self.n_blocks = self.n_laps - 1

        # Start writing summary
        print("\nCLOCK RESULTS\n")
        print(f"Number of blocks: {self.n_blocks}\n")

        # Total run time
        total = 0

        for n in range(self.n_blocks):

            if self.names[n] == "Block":
                name = f"Block {n + 1}"
            else:
                name = self.names[n]

            # Print timing and involved rows for each block
            print(f"{name}: {self.laps[n + 1] - self.laps[n]}; Rows {self.rows[n]} to {self.rows[n + 1]}")

            total += self.laps[n + 1] - self.laps[n]

        print(f"\nTotal run time: {total}\n")
        
    def history(self):
        
        """ Similar to summary, returns a dictionary of timings, 
        with no references to rows. To be used for API metadata. """
        
        # Computer number of blocks
        self.n_blocks = self.n_laps - 1
        
        # Init dictionary
        history = {}

        # Total run time
        total = 0

        for n in range(self.n_blocks):

            if self.names[n] == "Block":
                name = f"Block {n + 1}"
            else:
                name = self.names[n]
                
            # Write time of block
            history.update({name: self.laps[n + 1] - self.laps[n]})

            total += self.laps[n + 1] - self.laps[n]
            
        history.update({"Total" : total})

        return history



    def evaluate(self, function, args, iterable, iterable_name):

        """ Evaluate how function scales with varying iterable"""

        # Initialise block number
        if self.n_laps == 0:
            initial_block = 1
        else:
            initial_block = self.n_laps - 1

        # Compute number of final block
        final_block   = initial_block + len(iterable) - 1


        for it in iterable:

            # Update args dictionary
            args[iterable_name] = it
            # Start clocl
            self.lap()
            # Evaluate function
            function(**args)

        # Stop fime
        self.lap()

        # Compute timings
        timings = self.timings(initial_block, final_block)

        return timings

