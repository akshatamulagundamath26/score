import sys

if len(sys.argv) > 1:
    script_name = sys.argv[0]
    scores = sys.argv[1:]

    # Convert all arguments (strings) into float
    scores = [float(x) for x in scores]
else:
    # Default values when no command-line input is given
    scores = [85,90,78,95]
    print("No input given, using default scores:", scores)

# Calculate total and average
total = sum(scores)
average = total / len(scores)

print("Scores:", scores)
print("Sum of Scores:", total)
print("Average of Scores:", average)

# Calculate minimum and maximum
minimum = min(scores)
maximum = max(scores)

print("Minimum score:", minimum)
print("Maximum score:", maximum)
