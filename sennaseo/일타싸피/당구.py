import math

# math.acos(x)
# math.asin(x)
# math.atan(x)
# math.degree(x)
# math.radian(x)

def cal_angle(from_ball, to_ball):
    
    if from_ball[0] <= to_ball[0] and from_ball[1] >= to_ball[1]:
        result = abs(math.degrees(math.atan((to_ball[0]-from_ball[0]) / (to_ball[1]-from_ball[1]))))
    
    if from_ball[0] <= to_ball[0] and from_ball[1] <= to_ball[1]:
        result = abs(math.degrees(math.atan((to_ball[1]-from_ball[1]) / (to_ball[0]-from_ball[0]))))
        result += math.degrees((math.pi / 2))
        
    if from_ball[0] >= to_ball[0] and from_ball[1] <= to_ball[1]:
        result = abs(math.degrees(math.atan((to_ball[0]-from_ball[0]) / (to_ball[1]-from_ball[1]))))
        result += math.degrees((math.pi / 2) * 2)
        
    if from_ball[0] >= to_ball[0] and from_ball[1] >= to_ball[1]:
        result = abs(math.degrees(math.atan((to_ball[1]-from_ball[1]) / (to_ball[0]-from_ball[0]))))
        result += math.degrees((math.pi / 2) * 3)
        
    return result
    
def cal_hit_pos(white, target_ball):
    hole1 = (274+3, -3)
    ang = cal_angle(target_ball, hole1)
    
    xxx = target_ball[0] - 2 * 5.73 * math.sin(ang)
    yyy = target_ball[1] + 2 * 5.73 * math.cos(ang)
    
    return [xxx, yyy]

r = 5.73
hole1 = (274+3, -3)

goal_ball1 = (237, 37)

white_ball = (200, 37)


hit_pos = cal_hit_pos(white_ball, goal_ball1)
print(cal_angle((10, 10),(30, 30)))
print(cal_angle(white_ball, hit_pos))