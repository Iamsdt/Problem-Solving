from typing import List

# Explanation: solution from @kshatriyas
# Initialize two variables, ones and twos, to keep track of the count of each bit position.

# ones: Tracks the bits that have appeared once.
# twos: Tracks the bits that have appeared twice.
# Iterate through the array of numbers.

# For each number i in the array:
# Update ones and twos:

# Let's analyze each step of the update process:

# a. ones = (ones ^ i) & (~twos);:

# ones ^ i XORs the current number i with the previous value of ones. This operation toggles the bits that have appeared an odd number of times, keeping the bits that have appeared twice unchanged.
# (~twos) negates the bits in twos, effectively removing the bits that have appeared twice from consideration.
# The & operation ensures that only the bits that have appeared once (after XOR) and not twice (after negating twos) are retained.
# b. twos = (twos ^ i) & (~ones);:

# twos ^ i XORs the current number i with the previous value of twos. This operation toggles the bits that have appeared an even number of times, effectively removing the bits that have appeared twice.
# (~ones) negates the bits in ones, effectively removing the bits that have appeared once from consideration.
# The & operation ensures that only the bits that have appeared twice (after XOR) and not once (after negating ones) are retained.
# After iterating through all the numbers, the value stored in ones will represent the single number that appears only once in the array.

# Let's understand why this approach works:

# The key idea is to use bitwise operations to keep track of the count of each bit position. By doing so, we can identify the bits that have appeared once, twice, or three times.
# When a bit appears for the first time (ones is 0 and the bit is toggled), it is stored in ones.
# When a bit appears for the second time (ones is 1 and the bit is toggled), it is removed from ones and stored in twos.
# When a bit appears for the third time (ones is 0 and the bit is toggled), it is removed from both ones and twos.
# By the end of the iteration, the bits that remain in ones represent the bits of the single number that appeared only once, while the bits in twos represent bits that appeared three times (which is not possible).
# In summary, the algorithm uses bit manipulation to efficiently keep track of the counts of each bit position. By utilizing XOR and AND operations, it can identify the bits of the single number that appears only once in the array while ignoring the bits that appear multiple times.


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0

        for num in nums:
            ones ^= (num & ~twos)
            twos ^= (num & ~ones)

        return ones


if __name__ == "__main__":
    print(Solution().singleNumber([2, 2, 3, 2]))
