import sys
scores = [85, 90, 78, 92]
if not all(isinstance (score, (int, float)) for score in scores):
print("Error: All scores must be numeric.")
sys.exit(1)
total = sum(scores)
average total / len(scores) if scores else None
maximum = max(scores) if scores else None
minimum = min(scores) if scores else None
print(f"Total Score: {total}")
print(f"Average Score: (average:.2f}")
print(f"Maximum Score: {maximum}")
