# Vòng lặp while
# Chỉ có câu lệnh while, không có do while
# thực hiện vòng lăp KHÔNG BIẾT TRƯỚC số lần lặp
# kiểm tra đến phần tử cuối cùng có ĐÚNG không
def vong_lap_while():
  print("""[==============================================]
  # Vòng lặp while
  [==============================================]""")
  n = 1
  while n < 100:
    print(n)
    n = n * 2

# Vòng lặp for
# thực hiện vòng lăp BIẾT TRƯỚC số lần lặp
# kiểm tra đến phần tử cuối cùng có TỒN TẠI không
def vong_lap_for():
  print("[==============================================]\n# Vòng lặp for\n[==============================================]")
  for i in range(10):
    print(i)

# thêm điều kiện vào vòng lắp: break - ngưng vòng lặp ngay lập tức
def vong_lap_for_break():
  print("""[==============================================]
  # thêm điều kiện vào vòng lắp: break
  [==============================================]""")
  for i in [12, 10, 22, 11, 64, 73, 99, 100]:
    if i % 2 == 1:
      break
    print(i)
  print("done for")

# thêm điều kiện vào vòng lắp: continues - bỏ qua lần lặp này, để đến vòng lặp tiếp
def vong_lap_for_continues():
  print("""[==============================================]
  # thêm điều kiện vào vòng lắp: continues
  [==============================================]""")
  for char in "Hiphop never dies":
    if char == "e":
      continue
    print(char)

# thêm điều kiện else ở cuối vòng lặp for / while
# được thực hiện nếu vòng lặp không kết thúc vì câu lệnh break
# ít sử dụng
def vong_lap_while_for_break_else():
  print("""[==============================================]
  # thêm điều kiện else ở cuối vòng lặp for / while
  [==============================================]""")
  for char in "Hiphop never dies":
    if char == "e":
      continue
    print(char)
  else:
    print("End")

  number = 1
  while number < 100:
    print(number)
    number = number * 2
  else:
    print("End")

# yêu cầu người dùng nhập vào 1 số tự nhiên
# 1. kiêm tra xem số đó có phải số nguyên tố hay không
# 2. In ra màn hình tất cả số nguyên tố nhỏ hơn hoặc bằng n
def tim_so_nguyen_to():
  print("""[==============================================]
  # Yêu cầu người dùng nhập vào 1 số tự nhiên
  # 1. kiêm tra xem số đó có phải số nguyên tố hay không
  # 2. In ra màn hình tất cả số nguyên tố nhỏ hơn hoặc bằng n
  [==============================================]""")
  n = int(input("Enter a number: "))
  for i in range(2, int(n ** 0.5 + 1)):  # n ** 0.5 đây là căn bậc 2 của số n
    if n % i == 0:
      print(n, " không phải là số nguyên tố")
      break
  else:
    print(n, " là số nguyên tố")

# yêu cầu người dùng nhập vào 1 số tự nhiên n khác 0
# Tính n! theo 2 cách:
# 1. sử dụng vòng lặp for
# 2. sử dụng vòng lặp while
def tinh_so_tu_nhien_one():
  print("""[==============================================]
  # Yêu cầu người dùng nhập vào 1 số tự nhiên n khác 0
  # Tính n! theo 2 cách:
  # 1. sử dụng vòng lặp for
  # 2. sử dụng vòng lặp while
  [==============================================]""")
  n = int(input("Enter a number: "))
  result_for = 1
  i = 1
  for i in range(1, n + 1):
    result_for *= i
  print("for :: ", result_for)

  result_while = 1
  j = 1
  while j <= n:
    result_while *= j
    j += 1
  print("while :: ", result_while)

def gioi_thieu():
  print("Tôi là trợ lý Python. Tôi giúp bạn học lập trình dễ hơn!")

def main():
  while True:
    print("\n🎯 MENU CHƯƠNG TRÌNH")
    print("1. Giới thiệu")
    print("2. Xem vòng lặp while")
    print("3. Xem vòng lặp for")
    print("4. Xem vòng lặp for với break")
    print("5. Xem vòng lặp for với continues")
    print("6. Xem vòng lặp for với break và else")
    print("7. Kiểm tra số nguyên tố")
    print("8. Tính n!")
    print("0. Thoát")
    lua_chon = input("👉 Nhập lựa chọn của bạn: ")

    if lua_chon == "1":
      gioi_thieu()
    elif lua_chon == "2":
      vong_lap_while()
    elif lua_chon == "3":
      vong_lap_for()
    elif lua_chon == "4":
      vong_lap_for_break()
    elif lua_chon == "5":
      vong_lap_for_continues()
    elif lua_chon == "6":
      vong_lap_while_for_break_else()
    elif lua_chon == "7":
      tim_so_nguyen_to()
    elif lua_chon == "8":
      tinh_so_tu_nhien_one()
    elif lua_chon == "0":
      print("👋 Tạm biệt!")
      break
    else:
      print("⚠️ Lựa chọn không hợp lệ!")

if __name__ == "__main__":
  main()
