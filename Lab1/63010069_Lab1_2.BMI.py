'''
Chapter : 1 - item : 2 - BMI Calculate

รับ input 2 จำนวนโดยที่ input ที่ 1 คือ h เป็นค่าความสูง(เมตร) และ Input ที่ 2 คือ w เป็นค่าน้ำหนัก(กิโลกรัม)
โดยให้คำนวณหาค่า BMI ที่คำนวณจากสูตร BMI = w / (h^2) โดยให้แสดงผลตามข้อความข้างล่าง

BMI < 18.50 แสดงผล Less Weight
18.50 <= BMI  < 23 แสดงผล Normal Weight
23 <= BMI  < 25 แสดงผล Morethan Normal Weight
25 <= BMI  < 30 แสดงผล Getting Fat
BMI  >= 30 แสดงผล Fat

'''
H, W = input("Enter your High and Weight : ").split()
BMI = float(W)/(float(H)**2)
if float(BMI) < 18.50:
    print("Less Weight")
elif 18.50 <= float(BMI) < 23:
    print("Normal Weight")
elif 23 <= float(BMI) < 25:
    print("More than Normal Weight")
elif 25 <= float(BMI) < 30:
    print("Getting Fat")
elif float(BMI) >= 30:
    print("Fat")
