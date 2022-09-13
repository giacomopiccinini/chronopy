# chronopy

This package implements a clock utility to be used when assessing code performance. The idea is that it works in a way similar to that of a common chronometer.  

## Installation 

To download and install the latest release please use

`pip install chronopy`

## Usage

Once installed, import in your Python session with

```from chronopy.Clock import Clock ```

The clock needs to be initialised at some point in your code

```
# Initialise Clock object (counting not started yet!)
clock = Clock()
```

Note, this initialisation is *not* starting the count of elapsed time. 
To keep track of time use the "lap" method. The first call will initialise counting and the second will stop, e.g.

```
# Start time
clock.lap()

# Code to be executed
... # Block 

# Stop timing
clock.lap()
```

At this point it is possible to get info about timing using 

```
# Print results
clock.summary()
```
This will print on screen something like
```
CLOCK RESULTS 

Number of blocks: 1

Block 1: 0.010825157165527344; Rows 10 to 16

Total run time:  0.010825157165527344
```

In fact, this basic usage can be improved as follows. Everytime you call "lap", you can assign a name to it. This way, when printing the summary
you should get info about the content of the block you are measuring. For instance, if your code consist of some matrix multiplication, you could use

```
# Start time
clock.lap("Matrix Multiplication")

# Code to be executed
... # Block containing matrix multiplication

# Stop timing
clock.lap()
```

Resulting in 

```
CLOCK RESULTS 

Number of blocks: 1

Matrix Multiplication: 0.010825157165527344; Rows 10 to 16

Total run time:  0.010825157165527344
```

Finally, it is very useful to concatenate multiple "lap" calls, so as to keep track of different code blocks. A thorough usage would be the following 

```
from chronopy.Clock import Clock

# Initiate
clock = Clock()

# Start time
clock.lap("Matrix Multiplication")

# Code to be executed
... # Block containing matrix multiplication

# Lap
clock.lap("Matrix Sum")

# Code to be executed
... # Block containing matrix sum

# Lap
clock.lap("Max Pooling")

# Code to be executed
... # Block containing max pooling

# Stop timing
clock.lap()

# Print results
clock.summary()
```
This will print on screen

```
CLOCK RESULTS 

Number of blocks: 3

Matrix Multiplication: 0.01; Rows 10 to 16

Matrix Sum: 0.02; Rows 17 to 24

Max Pooling: 0.03; Rows 25 to 28

Total run time:  0.06
```