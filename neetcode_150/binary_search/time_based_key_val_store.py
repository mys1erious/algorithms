# class TimeMapBruteForce:
#     def __init__(self):
#         self.data = {}
#         self.prev_timestamp = None
#
#     def set(self, key: str, value: str, timestamp: int) -> None:
#         if not self.prev_timestamp:
#             self.prev_timestamp = timestamp
#         elif timestamp < self.prev_timestamp:
#             self.prev_timestamp = timestamp
#
#         if key not in self.data.keys():
#             self.data[key] = {}
#         self.data[key][timestamp] = value
#
#     def get(self, key: str, timestamp: int) -> str:
#         if timestamp < self.prev_timestamp:
#             return ""
#
#         if timestamp not in self.data[key].keys():
#             cts = self.find_closest_timestamp(key, timestamp)
#             return self.data[key][cts]
#
#         return self.data[key][timestamp]
#
#     def find_closest_timestamp(self, key, timestamp):
#         max_dif = None
#         closest_timestamp = None
#         for cur_timestamp in self.data[key].keys():
#             if cur_timestamp > timestamp:
#                 continue
#
#             if not closest_timestamp:
#                 closest_timestamp = cur_timestamp
#                 max_dif = timestamp - cur_timestamp
#
#             dif = timestamp - cur_timestamp
#             if dif < max_dif:
#                 max_dif = dif
#                 closest_timestamp = cur_timestamp
#
#         return closest_timestamp


# T: O(logn) optimization using Binary Search
class TimeMap:
    def __init__(self):
        self.data = {}
        self.lowest_timestamp = None

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.lowest_timestamp:
            self.lowest_timestamp = timestamp
        elif timestamp < self.lowest_timestamp:
            self.lowest_timestamp = timestamp

        try:
            values = self.data[key]
        except KeyError:
            values = self.data[key] = []

        values.append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        try:
            values = self.data[key]
        except KeyError:
            return ""

        if timestamp < self.lowest_timestamp:
            return ""

        lp = 0
        rp = len(values)-1
        while lp <= rp:
            mp = (lp+rp) // 2

            pointers_dif = rp-lp
            if values[mp][1] == timestamp:
                return values[mp][0]
            elif pointers_dif <= 1:
                if values[rp][1] <= timestamp:
                    return values[rp][0]
                return values[lp][0]
            elif values[mp][1] > timestamp:
                rp = mp-1
            else:
                lp = mp+1
        else:
            return values[mp][0]

    def __str__(self):
        return str(self.data)


def tst1():
    time_map = TimeMap()
    time_map.set('foo', 'bar', 1)
    assert time_map.get('foo', 1) == "bar"
    assert time_map.get('foo', 3) == "bar"

    time_map.set('foo', 'bar2', 4)
    assert time_map.get('foo', 4) == "bar2"
    assert time_map.get('foo', 5) == "bar2"


def tst2():
    time_map = TimeMap()
    time_map.set('love', 'high', 10)
    time_map.set('love', 'low', 20)

    assert time_map.get('love', 5) == ""
    assert time_map.get('love', 10) == "high"
    assert time_map.get('love', 15) == "high"
    assert time_map.get('love', 20) == "low"
    assert time_map.get('love', 25) == "low"

    print(time_map)


if __name__ == '__main__':
    tst1()
    tst2()
