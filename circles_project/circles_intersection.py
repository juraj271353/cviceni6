from circles_project.circles_stats import has_intersection

circle1 = {
    "x": 0,
    "y": 0,
    "r": 5
}

circle2 = {
    "x": 4,
    "y": 0,
    "r": 3
}

result = has_intersection(circle1, circle2)
print(result)