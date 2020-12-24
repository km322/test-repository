# Test file for this branch

SENTINEL = 1

while True:
  val = int(input("Whats is your number? "))
  if val == SENTINEL:
    break
  val = val+1
  print(val)
print("All Done!")
