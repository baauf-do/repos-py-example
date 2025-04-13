"""
Yêu cầu người dùng nhập vào 3 ô số nguyên dương
1. Kiểm tra xem đây có phải là số đo 3 cạnh của 1 tam giác không?
2. Nếu có thì kiểm tra tiếp xem đây là tam giác cân, tam giác đều,
tam giác vuông hay tam giác thường
3. Kiểm tra tiếp xem tam giác này có góc tù hay không?
4. Tính diện tích của tam giác
"""
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter b: "))

if a + b > c and b + c > a and a + c > b:  # Bất đẳng thức tam giác
  if a == b and b == c:
    print("Đây là tam giác đều")
  elif a == b or b == c or c == a:
    if (a ** 2 + b ** 2 == c ** 2) or (b ** 2 + c ** 2 == a ** 2) or (a ** 2 + c ** 2 == b ** 2):
      print("Đầy là tam giác vuông cân")
    else:
      print("Đây là tam giác cân")
  elif (a ** 2 + b ** 2 == c ** 2) or (b ** 2 + c ** 2 == a ** 2) or (a ** 2 + c ** 2 == b ** 2):
    print("Đây là tam giác vuông")
  else:
    print("Đây là tam giác thường")
else:
  print("Đây không phải là số đo 3 cạnh của 1 tam giác")
