#BMI = 体重/（身高**2）
a=float(input("请输入身高(m)"));
b=int(input("请输入体重(kg)"));

BMI=b/(a**2)
print("你的BMI",float(BMI));

if BMI<=18.5:
    print("偏瘦")
elif BMI<=25:
    print("正常")
elif BMI<=30:
    print("偏胖")
else:
    print("肥胖")