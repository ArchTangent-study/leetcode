from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Length needed to travel for loop
        loop_length = len(gas)
        # Dynamic values that are updated/reset
        distance = loop_length
        start_ix = 0
        fuel = 0

        # Double and zip for easy looping [(gas, cost), (gas, cost), ...]
        for station, (fillup, loss) in enumerate(zip(gas * 2, cost * 2)):
            # Arrived at destination
            if distance == 0:
                return start_ix
            # Add fuel from this station
            fuel += fillup
            # Can't move from this station -> reset all
            if fuel < loss:
                # start over again at *next* station
                distance = loop_length
                start_ix = station + 1
                fuel = 0
            else:
                # Move to next station (index) in track
                distance -= 1
                fuel -= loss

        # Failed to loop around track
        return -1
