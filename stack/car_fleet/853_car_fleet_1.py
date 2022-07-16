from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """Stack approach."""
        answer = 0
        # Stack of (pos, vel) of each car/fleet, sorted to have closest at top of stack
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort()
        # Start with front car, comparing against any other in the stack (min: 1 car)
        while cars:
            pos, vel = cars.pop()
            answer += 1
            # Check for collision w/other cars by comparing:
            # - time to target for current fleet
            # - time to collsion (w/current fleet) for next car
            while cars:
                next_pos, next_vel = cars[-1]
                time_to_target = (target - pos) / vel
                time_to_collide = (pos-next_pos) / (next_vel-vel) if next_vel > vel else None
                # Next car catches up w/current fleet
                # - pop next car to add to current fleet
                if time_to_collide and time_to_collide <= time_to_target:
                    cars.pop()
                    continue
                # Next car does *not* catch up w/current fleet - go to next
                break

        return answer
