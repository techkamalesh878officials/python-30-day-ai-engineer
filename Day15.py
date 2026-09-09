# Mini Data Processing System

nos = int(input("Enter how many students: "))

ps = 0
fs = 0
cavg = 0

name = {}
py = {}
math = {}
ai = {}
atten = {}
total = {}
avg = {}
sta = {}

# Highest / Lowest
hp = 0
lp = 0
hatt = 0

hp_name = ''
lp_name = ''
ha_name = ''

# Input
for i in range(1, nos + 1):

    name[i] = input(f"\n{i}) Enter Student name : ")
    py[i] = int(input(f"{i}) Enter python marks : "))
    math[i] = int(input(f"{i}) Enter maths marks : "))
    ai[i] = int(input(f"{i}) Enter AI marks : "))
    atten[i] = int(input(f"{i}) Enter Attendance Percentage : "))

    total[i] = py[i] + math[i] + ai[i]
    avg[i] = total[i] / 3

    cavg = cavg + avg[i]

    # Highest Performer
    if avg[i] > hp:
        hp = avg[i]
        hp_name = name[i]

    # Highest Attendance
    if atten[i] > hatt:
        hatt = atten[i]
        ha_name = name[i]

    # Status
    if py[i] >= 40 and math[i] >= 40 and ai[i] >= 40:
        sta[i] = "PASS"
        ps = ps + 1
    else:
        sta[i] = "FAIL"
        fs = fs + 1


# Class Average
cavg = cavg / nos

# Lowest Performer
lp = min(avg.values())

for i in avg:
    if avg[i] == lp:
        lp_name = name[i]
        break


# Output
print('=' * 50)
print("          MINI DATA PROCESSING SYSTEM")
print('=' * 50)

print()
print("Name\tPython\tMaths\tAI\tAverage\tStatus")
print('-' * 50)

for i in range(1, nos + 1):
    print(f"{name[i]}\t{py[i]}\t{math[i]}\t{ai[i]}\t{avg[i]:.2f}\t{sta[i]}")

print('=' * 50)

print(f"Total Students          : {nos}")
print(f"Passed                  : {ps}")
print(f"Failed                  : {fs}")
print(f"Class Average           : {cavg:.2f}")
print(f"Highest Performer       : {hp_name}")
print(f"Lowest Performer        : {lp_name}")
print(f"Highest Attendance      : {ha_name}")
print(f"Top Attendance Percentage : {hatt}%")

print('=' * 50)
