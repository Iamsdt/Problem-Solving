from optparse import Values


# Time: n
class TimeMap2:

    def __init__(self):
        self.keys={}
        self.values={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.keys:
            self.keys[key].append(timestamp)
        else:
            self.keys[key] = [timestamp]
        
        # now save value
        self.values[f"{key}{timestamp}"] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keys:
            return ""
        v = self.keys[key]
        if timestamp in v:
            return self.values[f"{key}{timestamp}"]
        else:
            # v.sort() #already sorted
            ind = -1
            for i in v:
                if i < timestamp:
                    ind = i
                else:
                    break

            if ind == -1:
                return ""
            return self.values[f"{key}{ind}"]
        


# use binary search to 
class TimeMap:

    def __init__(self):
        self.keys={}
        self.values={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.keys:
            self.keys[key].append(timestamp)
        else:
            self.keys[key] = [timestamp]
        
        # now save value
        self.values[f"{key}{timestamp}"] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keys:
            return ""
        v = self.keys[key]

        p = 0
        q = len(v)-1
        ind = -1
        while p <= q:
            mid = (p+q)//2
            if timestamp == v[mid]:
                return self.values[f"{key}{timestamp}"]
            elif timestamp < v[mid]:
                q = mid - 1
            elif timestamp > v[mid]:
                p = mid+1
                ind= v[mid]
        
        if ind > -1:
            return self.values[f"{key}{ind}"]
        else:
            return ""


if __name__ == "__main__":
    timeMap = TimeMap()
    timeMap.set("love", "hight", 10)
    timeMap.set("love", "low", 20)
    print(timeMap.get("love", 5))
    assert timeMap.get("love", 5) == ""
    print(timeMap.get("foo", 3))
    timeMap.set("foo", "bar2", 4)
    print(timeMap.get("foo", 4))
    print(timeMap.get("foo", 5))