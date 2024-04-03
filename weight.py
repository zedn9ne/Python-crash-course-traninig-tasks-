weight = float(input('Weight : '))
unit = str(input("(K)g or (L)bs: ").upper())
if unit == "l":
    converted = weight * .45;
    print(f"your weight in Lbs is : {converted}" );
else: 
    converted = weight / .45;
    print(f"your weight in Kgs is : {converted}");