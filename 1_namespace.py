import random, os, sys, datetime

def last_day_of_month(is_year, is_month):
    is_day = datetime.date(is_year, is_month, 1)
    y_year = is_day.year
    m_month = is_day.month

    if (m_month == 12):
        m_month = 1
        y_year += 1
    else:
        m_month += 1

    #print(datetime.date(y_year,m_month,1))
    
    #print(datetime.timedelta(days=-1))

    return datetime.date(y_year,m_month,1) + datetime.timedelta(days=-1)


def randint():
    print("執行了自訂的randint函數")

a = random.randint(0,99)
print("執行了random模組的randint函數：{}".format(a))

randint()

items = [1,2,3,4,5]

random.shuffle(items)
print(items)


print(os.getcwd())
print(os.path.getsize(os.getcwd()))

print(sys.version)
print(sys.platform)
print('\n'.join(sys.modules))

input_year = int(input("Please enter year:"))
input_month = int(input("Please enter month:"))
print(last_day_of_month(input_year,input_month))
