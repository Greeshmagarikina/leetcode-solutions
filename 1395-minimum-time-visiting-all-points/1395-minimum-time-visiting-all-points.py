class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time=0
        for i in range(len(points)-1):
            p1=points[i]
            p2=points[i+1]
            x_point=abs(p2[0]-p1[0])
            y_point=abs(p2[1]-p1[1])
            time+=max(x_point,y_point)
        return time