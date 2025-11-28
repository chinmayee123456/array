import sys

if len(sys.argv) > 1:
    scores_list = list(map(int, sys.argv[1:]))
    print("User provided values:")
else:
    scores_list = [50, 60, 70, 80, 90]
    print("No input given - using default values:")

total = sum(scores_list)
average = total / len(scores_list)

print("Scores:", scores_list)
print("Sum of Scores:", total)
print("Average Score:", average)
