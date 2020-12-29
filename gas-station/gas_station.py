
# There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
# 
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.
# 
# Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.
# 
# Note:
# 
# If there exists a solution, it is guaranteed to be unique.
# Both input arrays are non-empty and have the same length.
# Each element in the input arrays is a non-negative integer.

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if len(gas) == None:
            return -1
        if len(gas) == 1:
            return -1 if gas[0]-cost[0]<0 else 0 
        tank = 0
        total = 0
        index = 0
        for i in range(0, len(gas)):
            consume = gas[i] - cost[i]
            tank += consume
            if tank < 0:
                index=i+1
                tank = 0
            total += consume
            
        return -1 if total<0 else index
        

canCompleteCircuit([1,2,3,4,5,5,70], [2,3,4,3,9,6,2])
