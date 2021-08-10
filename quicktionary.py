from inspect import getmembers, isfunction
import blue, red, yellow
import re

function_regex = r'[ryb][0-9]+'

blue_functions = getmembers(blue, isfunction)
blue_functions = [f[1] for f in blue_functions if re.match(function_regex, f[0])]

red_functions = getmembers(red, isfunction)
red_functions = [f[1] for f in red_functions if re.match(function_regex, f[0])]
yellow_functions = getmembers(yellow, isfunction)
yellow_functions = [f[1] for f in yellow_functions if re.match(function_regex, f[0])]

num_solved = 0
num_attempted = 0
for yellow_function in yellow_functions:
    yellow_data = list(yellow_function()) # Only generate this data once
    for blue_function in blue_functions:
        for red_function in red_functions:
            num_attempted += 1
            print(f"Yellow card: {yellow_function.__doc__}")
            print(f"Blue card: {blue_function.__doc__}")
            print(f"Red card: {red_function.__doc__}")
            try:
                solution = next(filter(red_function, filter(blue_function, yellow_data)))
                print(f"Solution: {solution} ({num_solved}/{num_attempted})")
                num_solved += 1
            except StopIteration:
                print(f"No solution found")
            print()
