class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = []

        for i in range(n):
            time = (target - position[i]) / speed[i]
            cars.append((position[i], time))
        
        cars.sort(reverse = True)

        fleet = 0
        max_time = 0.0

        for pos, time in cars:
            if time > max_time:
                fleet += 1
                max_time = time
        
        return fleet

        
