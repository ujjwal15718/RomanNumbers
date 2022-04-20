# dictionary roman numbers
 
  
 
 
numerals = { 1 : "I", 4 : "IV", 5 : "V", 9 : "IX", 10 : "X", 40 : "XL",
             50 : "L", 90 : "XC", 100 : "C", 400 : "CD", 500 : "D", 900 : "CM", 1000 : "M" ,1500:"MD",1900:"MCM"
             ,2000:"CMM", 2500:"MMD",2900:"MMCM",3000:"MMM"}
 
num =int(input("enter the number"))
 
roman = ''
 
for k, v in sorted(numerals.items(), reverse=True):
    while num >= k:
        roman += v
        num -= k
 
print(roman)
