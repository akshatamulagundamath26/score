import sys

scores = [85, 90, 78, 92]

# Validate that all elements are numeric
if not all(isinstance(score, (int, float)) for score in scores):
    print("Error: All scores must be numeric.")
    sys.exit(1)

# Calculate total, average, max, and min
total = sum(scores)
average = total / len(scores) if scores else None
maximum = max(scores) if scores else None
minimum = min(scores) if scores else None

# Display results
print(f"Total Score: {total}")
print(f"Average Score: {average:.2f}")
print(f"Maximum Score: {maximum}")
print(f"Minimum Score: {minimum}")
