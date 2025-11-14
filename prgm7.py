# array_scores.py - Works perfectly with Jenkins
import sys

# Check if scores are passed via Jenkins command line
if len(sys.argv) > 1:
    scores = list(map(int, sys.argv[1:]))
else:
    # Default values if no input provided
    scores = [78, 85, 90, 66, 80]
    print("No scores provided. Using default values:", scores)

# Calculate sum and average (main/master branch logic)
total = sum(scores)
average = total / len(scores)

# Display all results
print(f"Scores entered: {scores}")
print(f"Sum of scores: {total}")
print(f"Average score: {average:.2f}")
