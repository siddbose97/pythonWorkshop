fitnessTestScore = 0
fitnessTestValue = ""
fitnessTestCash = 0
fitnessTestOffs = 0

if fitnessTestScore >= 85:
fitnessTestValue = "gold"
fitnessTestCash = 300
    fitnessTestOffs = 3
elif fitnessTestScore < 85 and fitnessTestScore >= 75:
    fitnessTestValue = "silver"
    fitnessTestCash = 200
    fitnessTestOffs = 2
elif fitnessTestScore < 75 and fitnessTestScore >= 60:
    fitnessTestValue = "pass"
    fitnessTestCash = 0
    fitnessTestOffs = 1 
else:
    fitnessTestValue = "FAIL"
    fitnessTestCash = 0
    fitnessTestOffs = 0

