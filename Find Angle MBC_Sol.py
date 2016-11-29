import math

AB, BC = (int(raw_input()) for _ in range(2))
print str(int(round(math.degrees(math.atan2(AB, BC))))) + "°"