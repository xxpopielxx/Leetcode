class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convert_to_minutes(hour):
            hh, mm = map(int, hour.split(":"))
            return hh * 60 + mm
        
        sorted_tab = sorted(timePoints, key = convert_to_minutes)
        mini = float("inf")
        for i in range(1, len(sorted_tab)):
            diff = convert_to_minutes(sorted_tab[i]) - convert_to_minutes(sorted_tab[i - 1])
            if diff < mini:
                mini = diff

        mini = min(mini, (convert_to_minutes(sorted_tab[0]) + 1440 - convert_to_minutes(sorted_tab[-1])))
        return mini
        