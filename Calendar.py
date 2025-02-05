import calendar

#print(calendar.prcal(2022))

v_year = input("請輸入要查詢年份:")
v_month = input("請輸入要查詢月份：")

print(calendar.month(int(v_year), int(v_month)))

