"""
Function to determine whether the driver is allowed to enter driver mode
drivers are not allowed to drive a total of 12 hours without an 8 hour break
the function inputs are:
a list of driver shifts as start/end integers,
the integer is relative to lyft launch the current time since Lyft launch as integer
current_time (int): Current time as hour since Lyft launch

Example:

Example:
9 hour break, 1 hour shift, 2 hour break, 10 hour shift
history = [(9, 10), (12, 22)]
current_time = 24
can_drive = True

Example:
history = [(0, 4), (5, 9), (10, 14), (15, 19), (20, 24)]
current_time = 24
can_drive = False
"""

class Lyft:

    def allowDriveMode(self, shifts, current_time):
        driveSoFar = 0
        lastDriveTime = 0
        for start, end in shifts:
            if start - lastDriveTime >= 8:
                driveSoFar = end - start
            else:
                driveSoFar += end - start
            lastDriveTime = end

        return current_time - lastDriveTime >= 8 or driveSoFar < 12

history = [(9, 10), (12, 22)]
curr_time = 24
lyft = Lyft()
print(lyft.allowDriveMode(history, curr_time))

history2 = [(0, 4), (5, 9), (10, 14), (15, 19), (20, 24)]
curr_time = 24
print(lyft.allowDriveMode(history2, curr_time))