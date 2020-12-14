"""daily_temps = [61.2, 59.0, 59.4, 58.9, 60.1, 55.3, 55.6]

def calculate_mean(daily_temps):
  mean = 0
  numerator = 0
  for idx, elem in enumerate(daily_temps):
    numerator += elem
    idx +=1
    mean += numerator/(len(daily_temps))
  return mean

print(calculate_mean(daily_temps))"""

lst = [5, 4, 9, 3, 1, 0]
sorted(lst)
print(lst)