class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def check(value):
            print("Check", value)
            if value == 1:
                return "1"

            # recursively check
            data = check(value-1)
            print("Return for", value, data)
            # calculate for current value
            temp = ""
            prev = data[0]
            count = 1
            for i in range(1,len(data)):
                if data[i]==prev:
                    count += 1
                else:
                    temp += str(count) + str(prev)
                    prev = data[i]
                    count=1
            print("Calculated for", value, temp+str(count)+ prev)
            return temp+str(count)+ prev

        return check(n)

if __name__ == "__main__":
    print(Solution().countAndSay(4))
