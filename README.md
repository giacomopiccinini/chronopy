# Clock
This is a simple implementation of a clock utility to be used when assessing code performance. The idea is that it works in a way similar to that of a common chronometer.  Usage:
 
```from Clock import Clock

# Initialise Clock object (counting not started yet!)
clock = Clock()

# Start time
clock.lap()

# Code to be executed
... # Block 1

# Trigger new counting
clock.lap()

# Code to be executed
... # Block 2

# Terminate counting
clock.lap()

# Print results
clock.summary()

```
