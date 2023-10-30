# For PEP8 you will open Pylint and Pycodestyle

########################################################################################################################

# Aritmetik Operatörler
# +       Toplama
# -       Çıkarma
# *       Çarpma 
# /       Bölme
# %       Bölmeden kalan 
# **      Üst
# //      Bölme sonucu

########################################################################################################################

# Kıyaslama Operatörleri
# <               Küçük
# <=              Küçük eşit
# >               Büyük
# >=              Büyük eşit
# ==              Eşit
# !=              Eşit değil
# is              Nesne kimliği
# is not          İhmal edilen nesne kimliği

########################################################################################################################

# Boolean Operatörleri
# or              Biri veya diğeri doğruysa sonuç doğru 
# and             İkisi de doğruysa sonuç doğru
# not             Yanlışsa sonuç doğru

########################################################################################################################

# abs(x)          Mutlak değer
# bin(x)          Binary'e dönüştürür
# Float(x)        Float'a dönüştürür
# format(x,y)     X'i Y sayı tipine dönüştürür
# hex(x)          0x'in önüne x içeren onaltılık bir sayıya dönüştürür
# int(x)          Ondalık kısmı ve devamını keserek yalnızca tamsayı kısmını integer'a dönüştürür
# max(x,y,z)      Sayıların en büyüğünün değerini döndürür
# min(x,y,z)      Sayıların en küçüğünün değerini döndürür
# oct(x)          X'i oktal sayıya (0o ile başlayan sekizlik sayıya) çevirir
# round(x,y)      X'i y basamak kadar yuvarlar
# str(x)          X'i string'e döndürür
# type(x)         X'in ne tip bir değişken olduğunu döndürür

# import math
# z = 81
# print(math.sqrt(z)) # Sonuç 9

########################################################################################################################

# math.acos(x)            X'in arkkosinüsünü döndürür
# math.atan(x)            X'in tanjantını döndürür   
# math.atan2(x,y)         Dikdörtgen koordinatları kutupsal koordinatlara döndürür    
# math.ceil(x)            X'e eşit veya daha büyüken küçük tamsayı olan X'in tavanını döndürür
# math.cos(x)             X'in cosinüsünü döndürür
# math.degrees(x)         Açıyı radyanlardan dereceye dönüştürür
# math.e(x)               e sabitini döndürür
# math.exp(x)             e'nin X kuvvetini döndürür
# math.factorial(x)       X'in faktöriyelini döndürür
# math.floor(x)           X'in tabanını döndürür
# math.isnan(x)           X'in sayı olmaması halinde doğru döndürür
# math.logaritma(x,y)     X'in y tabanında logaritmasını döndürür
# math.log2(x)            X'in 2 tabanında logaritmasını döndürür
# math.pi                 Pi sayısını döndürür
# math.pow(x,y)           X'in y kuvvetini döndürür
# math.radians(x)         X açısını dereceden radyana döndürür
# math.sin(x)             X'in sinüsünü döndürür
# math.sqrt(x)            X'in karekökünü döndürür
# math.tan(x)             X'in tanjantını döndürür
# math.tau(x)             Tau sabitini döndürür

########################################################################################################################

# import math
# pi = math.pi
# e = math.e
# tau = math.tau
# x = 81
# y = 7
# z = -23234.5454
# print("Pi sabiti: ",pi)
# print("e değeri: ",e)
# print("tau sabiti: ",tau)
# print("x'in karekökü: ",math.sqrt(x))
# print("y'nin faktöriyeli: ",math.factorial(y))
# print("z'nin tabanı: ",math.floor(z))
# print("y'nin derece karşılığı: ",math.degrees(y))
# print("45 derecenin radyan karşılığı: ",math.radians(45))

########################################################################################################################

# sample_tax_rate=0.065
# samplel=f' Sales Tax Rate {sample_tax_rate:.2%}'
# sample2=f" Sales Tax Rate {sample_tax_rate:.2%}"
# sample3=f""" Sales Tax Rate {sample_tax_rate:.2%}"""
# sample4=f''' Sales Tax Rate {sample_tax_rate:.2%}'''

# print(samplel)
# print(sample2)
# print(sample3)
# print(sample4)

########################################################################################################################

# User1 = "Alberto"
# User2 = "Babs"
# User3 = "Carlos"

# output = f"{User1} \n{User2} \n{User3}"
# print(output)

########################################################################################################################

# unit_price = 49.95
# quantity = 32
# sales_tax_rate = 0.065
# subtotal = quantity * unit_price
# sales_tax = sales_tax_rate * subtotal
# total = subtotal + sales_tax
# output = f"""
# Subtotal:   ${subtotal:,.2f}
# Sales Tax:  ${sales_tax:,.2f}
# Total:      ${total:,.2f}
# """
# print(output)

# # Subtotal:   $1,598.40
# # Sales Tax:  $103.90
# # Total:      $1,702.30

# output = f"""
# Subtotal:   ${subtotal:>9,.2f} # > sağa <sola ^ merkeze
# Sales Tax:  ${sales_tax:>9,.2f}
# Total:      ${total:>9,.2f}
# """
# print("Hizalanmış: \n", output)

########################################################################################################################

# x = 255
# # İnteger'ı diğer sayı türlerine döndür
# print(bin(x))
# print(oct(x))
# print(hex(x))
# # Diğer sayı türlerinden integer'a döndür
# print(0o377)
# print(0xff)

# # 0b11111111
# # 0o377
# # 0xff

# # 255
# # 255

########################################################################################################################

# # Karmaşık sayı(gerçek,sanal)
# z = complex(2,-3)
# output=f"""
# Karmaşık Sayı:                  {z:>9}
# Karmaşık Sayının gerçek kısmı:  {z.real:>9}   
# Karmaşık Sayının sanal kısmı:   {z.imag:>9}   
# """
# print(output)

# # Karmaşık Sayı:                     (2-3j)
# # Karmaşık Sayının gerçek kısmı:        2.0
# # Karmaşık Sayının sanal kısmı:        -3.0

########################################################################################################################


# x in s:                 x s'nin içide bulunursa doğru döndürür
# x in not s:             x s'nin içide bulunursa doğru döndürür
# s*n veya n*s:           s stringini n kere döndürür
# s[i]:                   i. S elemanını döndürür (0 başlangıç sayısı)
# s[i:j]:                 s 'nin i'den J'e kadar elemanlarını döndürür
# s[i:j:k]:               s 'nin i'den J'e kadar elemanlarını k adım atlayarak döndürür
# min(s):                 en küçük veya düşük characteri gösterir
# max(s):                 en büyük veya yüksek karakteri gösterir
# s.index(x[,i[,j]]):     i'den j'ye kadar (optinal) ilk x bulunan konumu döndürür
# s.count(x):             kaç tane x olduğunun sayısını döndürür 


# s = "Abracadabra Hocus Pocus you're a turtle dove"


# print("s içerisinde küçük harfli t harfi var mı?:\n", "t" in s)
# print("s içerisinde büyük harfli t harfi var mı?:\n", "T" in s)
# print("s içerisinde büyük harfli t harfi yok mu?:\n", "T" not in s)
# print("15 tane '-' döndür:\n", "-"*15)
# print("s'nin 33.elemanından 39. elemanına kadar yazdır:\n", s[33:39])
# print("0'dan 44. karaktere kadar her 3. karakteri yazdır:\n", s[0:44:3])
# print("En düşük karakteri yazdır. Boşluk a'dan da küçüktür:\n", min(s))
# print("En büyük karakteri yazdır:\n", max(s))
# print("P'nin nerede olduğunu gösterir:\n", s.index("P"))
# print("22 ve 44. karakterler arasındaki ilk o'nun nerede olduğunu gösterir:\n", s.index("o",22,44))
# print("Kaç tane a harfinin s'nin içinde olduğunu gösterir:\n", s.count("a"))

########################################################################################################################
# ASCII Numaraları
########################################################################################################################

# 32 [space]
# 33 !
# 34 "
# 35 #
# 36 $
# 37 %
# 38 &
# 39 '
# 40 (
# 41 )
# 42 *
# 43 +
# 44 ,
# 45 -
# 46 .
# 47 /
# 48 0
# 49 1
# 50 2
# 51 3
# 52 4
# 53 5
# 54 6
# 55 7
# 56 8
# 57 9
# 58 :
# 59 ;
# 60 <
# 61 =
# 62 >
# 63 ?
# 64 @
# 65 A
# 66 B
# 67 C
# 68 D
# 69 E
# 70 F
# 71 G
# 72 H
# 73 I
# 74 J
# 75 K
# 76 L
# 77 M
# 78 N
# 79 O
# 80 P
# 81 Q
# 82 R
# 83 S
# 84 T
# 85 U
# 86 V
# 87 W
# 88 X
# 89 Y
# 90 Z
# 91 [
# 92 \
# 93 ]
# 94 ^
# 95 _
# 96 `
# 97 a
# 98 b
# 99 c
# 100 d
# 101 e
# 102 f
# 103 g
# 104 h
# 105 i
# 106 j
# 107 k
# 108 l
# 109 m
# 110 n
# 111 o
# 112 p
# 113 q
# 114 r
# 115 s
# 116 t
# 117 u
# 118 v
# 119 w
# 120 x
# 121 y
# 122 z
# 123 {
# 124 |
# 125 }
# 126 ~
# 127 (dikdörtgen)
# 128 €

########################################################################################################################

# s.capitalize()              Returns a string with the first letter capitalized and the rest lowercase.
# s.count(x, [y, z])          Returns the number of times string x in string s. Optionally, you can add y as a starting point and z as an ending point to search a portion of the string.
# s.find(x, [y, z))           Returns a number indicating the first position at which stringx can be found in string s. Optionaly and z parameters allow you to limit the search to a portion of the string. Returns —1 if none found.
# s.index(x, [y, z])          Similar to find but returns a "substring not found" error if string x can't be found in string y.
# s.isalpha()                 Returns True if s is at least one character long and contains only letters (A-Z or a-z).
# s.isdecimal()               Returns True if s is at least one character long and contains only numeric characters (0-9).
# s.islower()                 Returns True if s contains letters and all those letters are lowercase.
# s.isnumeric()               Returns True if s is at least one character long and contains only numeric characters (0-9).
# s.isprintable()             Returns True if string s contains only printable characters.
# s.istitle()                 Returns True if strings contains letters and the first letter of each word is uppercase followed by lowercase letters.
# s.isupper()                 Returns True if all letters in the string are uppercase.
# s.lower()                   Returns s with all letters converted to lowercase.
# s.lstrip()                  Returns s with any leading spaces removed.
# s.replace(x, y)             Returns a copy of string s with all characters x replaced by character y.
# s.rfind(x, [y, z])          Similar to s.find but searches backward from the start of the string. If y and z are provided, searches backward from position z to position y. Retums —1 if string x not found.
# s.rindex()                  Same as s.rfind but returns an error if the substring isn't found.
# s.rstrip()                  Returns string x with any trailing spaces removed.
# s.strip()                   Returns string x with leading and trailing spaces removed.
# s.swapcase()                Returns string s with uppercase letters converted to lowercase and lowercase letters converted to uppercase.
# s.title()                   Returns string s with the first letter of every word capitalized and all other letters lowercase.
# s.upper()                   Returns string s with all letters converted to uppercase.

########################################################################################################################

# s = "Abracadabra Hocus Pocus you're a turtle dove"
# x = "a"
# y = 5
# z = 32
# b = 'b'
# c = 'c'
# print("İlk harf büyük diğerleri küçük \n", s.capitalize())
# print("x s'de kaç defa var. Optinal: y başlangıç z bitiş karakteri \n", s.count(x, y, z))
# print("x'in s'de kaçıncı olduğunu bulma. Optinal: y başlangıç z bitiş karakteri \n", s.find(x, y, z))
# print("find ile aynı, yalnızca bulamazsa substring not found hatası verir \n", s.index(x, y, z))
# print("yalnızca harf içeriyorsa True döndürür \n", s.isalpha())
# print("yalnızca rakam içeriyorsa True döndürür \n", s.isdecimal())
# print("bütün harfler küçük ise True döndürür \n", s.islower())
# print("en azından 1 karakter içeriyorsa ve yalnızca rakam içeriyorsa True döndürür \n", s.isnumeric())
# print("Eğer sadece yazdırılabilir karakterler içeriyorsa True döndürür \n", s.isprintable())
# print("harfler içeriyorsa ve yalnızca ilk harfleri büyükse True döndürür \n", s.istitle())
# print("Bütün harfler büyükse True döndürür \n", s.isupper())
# print("Bütün harfler küçükse True döndürür \n", s.islower())
# print("Baştaki takip eden boşlukları kaldırma \n", s.lstrip())
# print("b'yi c ile değiştirme \n", s.replace(b,c))
# print("bul ile aynı ama tersten başlıyor  \n", s.rfind(x, y, z))
# print("bul ile aynı ama eğer bulamazsa substring not found hatası veriyor \n", s.rindex(x, y, z))
# print("Sondaki takip eden boşlukları kaldırma  \n", s.rstrip())
# print("Büyük harfleri küçük harf küçük harfleri büyük harf yapma \n", s.swapcase())
# print("Bütün kelimelerin yalnızca ilk harfleri büyük \n", s.title())
# print("hepsi büyük harf \n", s.upper())

########################################################################################################################

# s1 = "There is no such word as schmeedledorp" 
# s2 = "    a b c   "
# s3 = "ABC"


# print("Capitalize first Letter, the rest lowercase")
# print(s3.capitalize())
# print()
# print("Count the number of spaces in s1")
# print(s1.count(" "))
# print()
# print("Find the dot in S1")
# print(s1.find("."))
# print()
# print("Is s2 all lowercase letters?")
# print(s2.islower())
# print()
# print("Convert s3 to all lowercase") 
# print(s3.lower())
# print()
# print("String leading characters from s2")
# print(s2.lstrip())
# print()
# print("String leading and trailing characters from s2")
# print(s2.strip())
# print()
# print("Swap the case of letters in s1")
# print(s1.swapcase())
# print()
# print("Show s1 in title case (initial caps)")
# print(s1.title())
# print()
# print("Show s1 uppercase")
# print(s1.upper())
# print()

########################################################################################################################
# Date
########################################################################################################################

# import datetime as dt
# today = dt.date.today()
# last_of_teens = dt.date(2019,12,31)

# print()
# print("Bugün:")
# print(today)
# print()
# print("last_of_teens:")
# print(last_of_teens)
# print()
# print("Detaylı last_of_teens:")
# print(f"{last_of_teens: %A, %B %d, %Y}")
# print()
# todays_date=f"{today:%d.%m.%Y}"
# print("todays_date:")
# print(todays_date) 
# print()
# almost_midnight=dt.time(23,59,59,999999)
# print("almost midnight:")
# print(almost_midnight)
# print()
# right_now=dt.datetime.now()
# print("right now:")
# print(right_now)
# print()
# new_years_eve=dt.datetime(2019,12,31,23,59)
# print("new years eve:")
# print(new_years_eve)
# print()

# new_years_day = dt.date(2019, 1, 1)
# memorial_day = dt.date(2019, 5, 27)
# days_between = memorial_day - new_years_day
# print()
# print("memorial_day ile new_years_day arasındaki gün sayısı:")
# print(days_between)
# duration=dt.timedelta(days=146)
# print("duration:")
# print(duration)

########################################################################################################################

# import datetime as dt
# start_time=dt.datetime(2019,3,31,8,0,0)
# finish_time=dt.datetime(2019,3,31,14,34,45)
# time_between=finish_time-start_time
# print("Zaman aralığı:")
# print(time_between)
# print()

########################################################################################################################

# import datetime as dt
# now=dt.datetime.now()
# birthdatetime=dt.datetime(1989,7,6,16,0)
# age=now-birthdatetime
# print(age)
# print(type(age))

########################################################################################################################

# import datetime as dt
# today=dt.date.today()
# birthdate=dt.date(1996,5,16)
# delta_age=today-birthdate
# days_old=delta_age.days
# years=days_old//365
# months=(days_old%365)//30
# print(f"You are {years} years and {months} months old.")

########################################################################################################################

# import datetime as dt
# here_now=dt.datetime.now()
# utc_now=dt.datetime.utcnow()
# time_difference=utc_now-here_now

# print(f"My time: {here_now:%I:%M %p}")
# print(f"UTC time: {utc_now:%I:%M %p}")
# print(f"Difference: {time_difference}")

########################################################################################################################

# import datetime as dt
# from dateutil.tz import gettz

# utc=dt.datetime.now(gettz('Etc/UTC'))
# print(f"{utc:%A AD %I:%M %p %Z}")

# est=dt.datetime.now(gettz('America/New_York'))
# print(f"{est:%A AD %I:%M %p %Z}")

# cst=dt.datetime.now(gettz('America/Chicago'))
# print(f"{cst:%A AD %I:%M %p %Z}")

# mst=dt.datetime.now(gettz('America/Boise'))
# print(f"{mst:%A AD %I:%M %p %Z}")

# pst=dt.datetime.now(gettz('America/Los_Angeles'))
# print(f"{pst:%A AD %I:%M %p %Z}")

########################################################################################################################

# import datetime as dt
# from dateutil.tz import gettz

# event=dt.datetime(2020,7,4,19,0,0)
# print("Local:"+f"{event:%D %I:%M %p %Z}" + "\n")

# event_est=event.astimezone(gettz('America/New_York'))
# print(f"{event_est:%A %D %I:%M %p %Z}")

# event_cst=event.astimezone(gettz('America/Chicago'))
# print(f"{event_cst:%A %D %I:%M %p %Z}")

# event_mst=event.astimezone(gettz('America/Boise'))
# print(f"{event_mst:%A %D %I:%M %p %Z}")

# event_pst=event.astimezone(gettz('America/Los_Angeles'))
# print(f"{event_pst:%A %D %I:%M %p %Z}")

# event_utc=event.astimezone(gettz('Etc/UTC'))
# print(f"{event_utc:%A %D %I:%M %p %Z}")

########################################################################################################################

# %a weekday (Sun)
# %A weekday (Sunday)
# %w weekday number 0-6 (sunday is 0)

# %d number day of the month 01-31 (31)

# %b month (Jan) 
# %B month (January) 
# %m month 01-12 (01)

# %y year (19)
# %Y year (2019)

# %H hour (23)
# %I hour (11)
# %p AM/PM (PM)
# %M minute (01)
# %S second (01)
# %f microsecond (495846)

# %z UTC offset (-0500)
# %Z Time zone (EST)

# %j Day number of year (300)
# %U Week number of year(Sunday first day) (50)
# %W Week number of year(Monday first day) (50)
# %c Local version of date time (Tue Dec 31 23:59:59 2018)
# %x Local version of date (12/31/18)
# %X Local version of time (23:59:59)
# %% a % character (%)

########################################################################################################################
# Sample Date Format Strings
########################################################################################################################

# %I:%M %p
# %H:%M:%S and %f microseconds
# %X

# %A, %B %d at %I:%M%p
# %m/%d/%y at %H : %M%p
# %I:%M %p on %b %d
# %x
# %c
# %m/%d/%y at %I:%M %p
# %I:%M %p on %m/%d/%y

########################################################################################################################
#DÖNGÜLER
########################################################################################################################

# total=100
# sales_tax_rate=0.065
# taxable=True # False
# if taxable:
#     print(f"Subtotal : ${total:.2f}")
#     sales_tax=total*sales_tax_rate
#     print(f"Sales Tax: ${sales_tax:.2f}")
#     total+=sales_tax
# print(f"Total    : ${total:.2f}")

########################################################################################################################

# import datetime as dt
# now = dt.datetime.now()
# if now.hour<12:
#     print("Good morning")
# else:
#     print("Good afternoon")
# print("I hope you are doing well!")

########################################################################################################################

# for x in range(1,11):
#     print(x)
# print("All done!")

# for x in "snorkel":
#     print(x)
# print("All done!")

# for x in ["The","rain","in","Spain"]:
#     print(x)
# print("All done!")

########################################################################################################################

# answers=["A","C","B","D"]
# answers=["A","","B","D"]

# for answer in answers:
#     if answer=="":
#         print("incomplete")
#         break
#     print(answer)
# print("loop is done!")

# for answer in answers:
#     if answer=="":
#         print("incomplete")
#         continue
#     print(answer)
# print("loop is done!")

########################################################################################################################

# for outer in ["First","Second","Third"]:
#     print(outer)
#     for inner in range(3):
#         print(inner+1)
# print("Both loops are done")

########################################################################################################################


# counter=65
# while counter<91:
#     print(str(counter)+"="+chr(counter))
#     counter+=1
# print("All done")

########################################################################################################################


# import random
# print("Numbers that aren't evenly divisible by 5")
# counter=0
# while counter<10:
#     number=random.randint(1,999)
#     if int(number/5)==number/5:
#         break
#     print(number)
#     counter+=1
# print("loop is done")


########################################################################################################################
#LİSTELER
########################################################################################################################


# scores=[88,92,78,90,84]
# for score in scores:
#     print(score)
# print("done")

########################################################################################################################

# students=["Mark","Amber","Todd","Anita","Sandy"]

# has_anita="Anita" in students
# print(has_anita)

# has_bob="Bob" in students
# print(has_bob)

# students.append("Goober")

# new_student="Amanda"
# students.append(new_student)

# students.insert(0,"Lupe")

# new_student="Marta"

# if new_student in students:
#     print(new_student+" already in the list")
# else:
#     students.append(new_student)
#     print(new_student+" added to the list")

# print(students)

########################################################################################################################

# list1=["Zara","Lupe","Hong","Alberto","Jake"]
# list2=["Huey","Dewey","Louie","Nader","Bubba"]

# list1.extend(list2)
# print(list1)

# list1=["Zara","Lupe","Hong","Alberto","Jake"]
# list1[3]="Hobart"
# print(list1)

########################################################################################################################

# letters = ["A","B","C","D","C","E","C"]
# letters.remove("C")
# print(letters) # ilk C gider

# letters = ["A","B","C","D","C","E","C"]
# letters.pop(0) 
# print(letters)

# letters = ["A","B","C","D","C","E","C"]
# letters.pop()
# print(letters)

########################################################################################################################

# letters = ["A","B","C","D","E","F","G"]
# print("letters ilk hal: "+str(letters))

# first_removed=letters.pop(0)
# last_removed=letters.pop()
# print(first_removed + " and " + last_removed + " were removed from list")
# print("letters son hal: "+str(letters))

########################################################################################################################

# letters = ["A","B","C","D","E","F","G"]
# print("ilk hal: "+str(letters))
# while "C" in letters:
#     letters.remove("C")
# print("son hal: "+str(letters))

########################################################################################################################

# letters = ["A","B","C","D","E","F","G"] 
# del letters[2] 
# print(letters)

########################################################################################################################

# letters = ["A","B","C","D","E","F","G"]
# del letters
# print(letters) # liste silindiği için tanımlanamadı hatası alıyoruz.

########################################################################################################################

# letters = ["A","B","C","D","E","F","G"]
# letters.clear()
# print(letters) # içini temizlediği için boş gözüküyor.

########################################################################################################################

# # Create a list of strings.
# grades = ["C","B","A","D","C","B","C",]
# # Count the B's
# b_grades = grades.count("B")
# # Use a variable for value to count.
# look_for = "C"
# c_grades = grades.count(look_for)
# print("There are " + str(b_grades) + " B grades in the list.")
# print("There are " + str(c_grades) + " " + look_for + " grades in the list.")

########################################################################################################################

# grades = ["C","B","A","D","C","B","C",]
# b_index = grades.index("B")

# look_for = "A" # A yerine F yazarsan hata verir
# look_for_index = grades.index(look_for)

# print("the first B index is index "+str(b_index))
# print("the first " + look_for + " index is at "+str(look_for_index))

########################################################################################################################

# grades = ["C","B","A","D","C","B","C",]

# look_for="B"

# if look_for in grades:
#     print(str(look_for) + " is at index " +str(grades.index(look_for)))
# else:
#     print(str(look_for) + " is not in the list")

########################################################################################################################

# names=["Zara","Lupe","Hong","Alberto","Jake","Tyler"]
# numbers=[14,0,56,-4,99,56,11,23]
# names.sort()
# numbers.sort()
# print(names)
# print(numbers)

########################################################################################################################

# import datetime as dt

# datelist=[]

# datelist.append(dt.date(2020,12,31))
# datelist.append(dt.date(2019,1,31))
# datelist.append(dt.date(2018,2,28))
# datelist.append(dt.date(2020,1,1))

# datelist.sort()
# for date in datelist:
#     print(f"{date:%d.%m.%Y}")

########################################################################################################################

# import datetime as dt

# names=["Zara","Lupe","Hong","Alberto","Jake","Tyler"]
# numbers=[14,0,56,-4,99,56,11,23]
# datelist=[]

# datelist.append(dt.date(2020,12,31))
# datelist.append(dt.date(2019,1,31))
# datelist.append(dt.date(2018,2,28))
# datelist.append(dt.date(2020,1,1))

# names.sort(reverse=True)
# print(names)
# print()

# numbers.sort(reverse=True)
# print(numbers)
# print()

# datelist.sort(reverse=True)
# for date in datelist:
#     print(f"{date:%d.%m.%Y}")

########################################################################################################################

# names=["Zara","Lupe","Hong","Alberto","Jake","Tyler"]
# names.reverse()
# print(names)

########################################################################################################################

# names=["Zara","Lupe","Hong","Alberto","Jake","Tyler"]
# backward_names=names.copy()
# backward_names.reverse()
# print(names)
# print(backward_names)

########################################################################################################################
# Liste Metotları
########################################################################################################################

# append()              Adds an item to the end of the list
# clear()               Removes all items from the list, leaving it empty
# copy()                Makes a copy of a list
# count()               Counts how many times an element appears in a list
# extend()              Appends the items from one list to the end of another list
# index()               Returns the index number (position) of an element in a list
# insert()              inserts an item into the list at a specific position
# pop()                 Removes an element from the list, and provides a copy of that item that you can store in a variable
# remove()              Removes one item from the list
# reverse()             Reverses the order of items in the list
# sort ()               Sorts the list in ascending order
# sort (reverse=True)   Sorts the list in descending order

########################################################################################################################
#SETLER
########################################################################################################################

# sample_set={1.98, 98.9, 74.95, 2.5, 1, 16.3}
# print(sample_set)
# ss2=sample_set.copy()
# print(ss2) # setler farklı sırada kopyalanabilir. 

########################################################################################################################

# sample_set={1.98, 98.9, 74.95, 2.5, 1, 16.3}
# print(sample_set)
# print(len(sample_set))
# print(74.95 in sample_set)
# sample_set.add(11.23)
# sample_set.update([88,123.45,2.98])
# print("\nLoop through set and print each item formatted.")
# for price in sample_set:
#     print(f"{price:>6.2f}")

########################################################################################################################
#SÖZLÜKLER
########################################################################################################################

# Key             Value
# htanaka         Haru Tanaka
# ppatel          Priya Patell
# bagarcia        Benjamin Alberto Garcia
# zmin            Zhang Min
# farooqi         Ayesha Farooqi
# hajackson       Hanna Jackson
# papatel         Pratyush Aarav Patel
# hrjackson       Henry Jackson

# Key             Value
# htanaka         ["Haru Tanaka”, 2000, 0, True]
# ppatel          ["Priya Patel", 2015, 1, False]
# bagarcia        ["Benjamin Alberto Garcia", 1999, 2, True]
# zmin            ["Zhang Min", 2017, O, False]
# farooqi         ["Ayesha Farooqi", 2001, 1, True]
# hajackson       ["Hanna Jackson", 1998, 0, False]
# papatel         ["Pratyush Aarav Patel", 2011, 2, True]
# hrjackson       ["Henry Jackson", 2016, 0, False]


# 'htanaka' = 'full name'         = 'Haru Tanaka'
#             'year_hired'        = 2000
#             'dependents'        = 0
#             'has_company_cell'  = True

# 'ppatel' =  'full name'         = 'Priya Patel'
#             'year hired'        = 2015
#             'dependents'        = 1
#             'has_company_cell'  = False

########################################################################################################################

# people={
#     "htanaka":   "Haru Tanaka",
#     "ppatel":   "Priya Patell",
#     "bagarcia":   "Benjamin Alberto Garcia",
#     "zmin":   "Zhang Min",
#     "farooqi":   "Ayesha Farooqi",
#     "hajackson":   "Hanna Jackson",
#     "papatel":   "Pratyush Aarav Patel",
#     "hrjackson":   "Henry Jackson",
# }
# print()
# print(people["zmin"])
# print()
# print(len(people))
# print()
# print("İlk hal hajackson: " + people["hajackson"])
# print()
# people["hajackson"]="Hanna Jackson-Smith"
# print("Son hal hajackson: " + people["hajackson"])

########################################################################################################################

# people={
#     "papatel":   "Pratyush Aarav Patel",
#     "hrjackson":   "Henry Jackson",
# }

# print("ilk hal:")
# for person in people:
#     print(person + " = " + people[person])

# people["hrjackson"]="Henrietta Jackson"
# people.update({'wwiggins':'Wanda Wiggins'})

# print("son hal:")
# for person in people:
#     print(person + " = " + people[person])

########################################################################################################################

# people={}

# people.update({"htanaka":"Haru Tanaka"})
# people.update({"ppatel":"Priya Patell"})
# people.update({"bagarcia":"Benjamin Alberto Garcia"})
# people.update({"zmin":"Zhang Min"})
# people.update({"farooqi":"Ayesha Farooqi"})
# people.update({"hajackson":"Hanna Jackson"})
# people.update({"papatel":"Pratyush Aarav Patel"})
# people.update({"hrjackson":"Henry Jackson"})

# for key,value in people.items():
#     print(key, " = ", value)

########################################################################################################################

# clear()         Empties the dictionary by remove all keys and values. 
# copy()          Returns a copy of the dictionary.
# fromkeys()      Returns a new copy of the dictionary but with only specified keys and values.
# get()           Returns the value of the specified key, or None if it doesn't exist.
# items()         Returns a list of items as a tüple for each key-value pair.
# keys()          Returns a list of all the keys in a dictionary.
# pop()           Removes the item specified by the key from the dictionary, and returns its value.
# popitem()       Removes the last key-value pair.
# setdefault()    Returns the value of the specified key. if the key doesn't exist, inserts the key with the specified value.
# update()        Updates the value of an existing key, or adds a new key-value pair if the specified key isn't already in the dictionary.
# values()        Returns a list of all the values in the dictionary.

########################################################################################################################

# people={
#     "htanaka":   "Haru Tanaka",
#     "ppatel":   "Priya Patell",
#     "bagarcia":   "Benjamin Alberto Garcia",
#     "zmin":   "Zhang Min",
#     "farooqi":   "Ayesha Farooqi",
#     "hajackson":   "Hanna Jackson",
#     "papatel":   "Pratyush Aarav Patel",
#     "hrjackson":   "Henry Jackson",
# }

# people2=people.copy()

# print(people)
# print(people2)

# people2.clear()
# print(people2)

########################################################################################################################

# people={
#     "htanaka":   "Haru Tanaka",
#     "ppatel":   "Priya Patell",
#     "bagarcia":   "Benjamin Alberto Garcia",
#     "zmin":   "Zhang Min",
#     "farooqi":   "Ayesha Farooqi",
#     "hajackson":   "Hanna Jackson",
#     "papatel":   "Pratyush Aarav Patel",
#     "hrjackson":   "Henry Jackson",
# }

# adios=people.pop("zmin")

# print(adios)
# print(people)

########################################################################################################################

# product = {
#     'name': 'Ray—Ban Wayfarer Sunglasses' ,
#     'unit_price': 112.99,
#     'taxable' : True,
#     'in_stock' : 10,
#     'models': ['Black' ,'Tortoise']
# }

# print(product["name"])
# print(product["unit_price"])
# print(product["taxable"])
# print(product["in_stock"])
# print(product["models"])

########################################################################################################################

# DWC001 = dict.fromkeys(['name','unit_price','taxable','in_stock','models'])
# print(DWC001)

########################################################################################################################

# product = {
#     'name': 'Ray—Ban Wayfarer Sunglasses' ,
#     'unit_price': 112.99,
#     'taxable' : True,
#     'in_stock' : 10,
#     'models': ['Black' ,'Tortoise']
# }

# dwc001=dict.fromkeys(product.keys())
# print(dwc001)
# dwc001.setdefault('taxable',True)
# dwc001.setdefault('models',[])
# dwc001.setdefault('reorder_point',100)
# dwc001['taxable']=True
# print(dwc001)

########################################################################################################################

# products={
#     'RB00111':{'name':'Ray-Ban Sunglasses','price':112.98,'models':['black','tortoise']},
#     'DWC0317':{'name':'Drone with Camera','price':72.95,'models':['black','white']},
#     'MTS0540':{'name':'T-shirt','price':2.95,'models':['small','medium','large']},
#     'ECD2989':{'name':'Echo Dot','price':29.99,'models':[]},
# }

# print(f"{'ID':<8} {'Name':<20} {'Price':<8} {'Models'}")
# print("-"*60)

# for product in products.keys():
#     id=product
#     name=products[product]['name']
#     price='$'+f"{products[product]['price']:,.2f}"
#     models=''
#     for m in products[product]['models']:
#         models += m + ', '
#     if len(models) >2:
#         models=models[:-2]
#     else: 
#         models='<none>'
    
#     print(f"{id:<8} {name:<20} {price:<8} {models}")

########################################################################################################################
# FONKSİYONLAR
########################################################################################################################

# def hello():
#     print('Hello')
# hello()

########################################################################################################################

# def hello(): #Practice fonction
#     """ A docstring describing the function """  # Ne olduğunu üstüne gelince gösterir
#     print('Hello')
# hello()

########################################################################################################################

# def hello(user_name): #Practice fonction
#     """ A docstring describing the function """  # Ne olduğunu üstüne gelince gösterir
#     print('Hello '+ user_name)

# this_person='Alan'
# hello(this_person)

########################################################################################################################

# def hello(user_name='nobody'): #Practice fonction
#     """ A docstring describing the function """  # Ne olduğunu üstüne gelince gösterir
#     print('Hello '+ user_name)

# this_person='Alan'
# hello(this_person)
# hello()

########################################################################################################################

# def hello(fname,lname,datestring=''): #Practice fonction
#     """ A docstring describing the function """  # Ne olduğunu üstüne gelince gösterir
#     msg = 'Hello ' + fname + ' ' + lname
#     if len(datestring) > 0:
#         msg += ' birthdate: ' + datestring
#     print(msg)

# hello('Kemal Musab', 'Dayıoğlu', '06/07/1989')
# hello('Ümriye Kevser', 'Dayıoğlu')

########################################################################################################################

# def hello(fname,lname,datestring): #Practice fonction
#     """ A docstring describing the function """  # Ne olduğunu üstüne gelince gösterir
#     msg = 'Hello ' + fname + ' ' + lname
#     if len(datestring) > 0:
#         msg += ' birthdate: ' + datestring
#     print(msg)

# hello(datestring='06/07/1989',lname='Dayıoğlu', fname='Kemal Musab')

# fname='Ümriye Kevser'
# lname='Dayıoğlu'
# datestring=''

# hello(fname=fname,datestring=datestring,lname=lname)

########################################################################################################################

# def alphabetize(original_list=[]):
#     """Pass any list in square brackets, displays a string with items sorted"""
    
#     # inside the function make a working copy of the list passed in.
#     sorted_list = original_list.copy()
#     # Sort the working copy.
#     sorted_list.sort()
#     # Make a new empty string for output
#     final_list = ''
#     # Loop through sorted list and append name and comma and space.
#     for name in sorted_list:
#         final_list += name + ', '
#     # Knock off last comma space if the string is not blank
#     final_list=final_list[:-2]
#     # Print the alphabetized lise.
#     print(final_list)

# names=[ 'McMullen','Keaser', 'Maier', 'Wilson', 'Yudt', 'Gallagher', 'Jacobs']
# alphabetize(names)

########################################################################################################################

# def sorter(*args):
#     """Pass in any number of arguments separated by commas inside the function, they treated as a tuple named args"""

#     # The passed-in
#     # Create a list from the passed-in tuple
#     newlist = list(args)
#     # Sort and Show the list.
#     newlist.sort()
#     print(newlist)

# sorter(1, 0.0001, 100000, -900,2)

########################################################################################################################

# def lowercaseof (anystring):
#     '''Converts string to all lowercase'''
#     return anystring.lower()

# names=['Adams', 'Ma', 'diMeola', 'Zandusky']
# names.sort(key=lowercaseof)
# print(names)

########################################################################################################################

# names=['Adams', 'Ma', 'diMeola', 'Zandusky']
# names_sorted=names.copy()
# names_sorted.sort(key=lambda anystring : anystring.lower())
# print('Names:        ', names)
# print('Names_sorted: ', names_sorted)

########################################################################################################################

# currency = lambda n : f"${n:,.2f}"
# percent = lambda n : f"{n:.2%}"

# # Test currency function 
# print(currency(99))
# print(currency(123456789.09876543))

# # Test percent function 
# print(percent(0.065))
# print(percent(.5))

########################################################################################################################

# # Show number in currency format, specify width.
# def currency(n, w=15):
#     '''Show in currency format, width = 15 or width of your choosing'''
#     s = f"${n:,.2f}"
#     # Pad left of output with spaces to width of w.
#     print(s)
#     return s.rjust(w)
# currency(156.2)

# # Show number in percent format, specify width.
# def percent(n, w=15):
#     '''Show in percent format, width = 15 or width of your choosing'''
#     # Show number in percent format.
#     s = f"{n:.1%}"
#     # Pad left of output with spaces to width of w.
#     print(s)
#     return s.rjust(w)
# percent(0.56)

########################################################################################################################
# SINIFLAR
########################################################################################################################

#         CAR CLASS

# Attributes:     Methods:
# .year           .go()                   
# .make           .stop()
# .model          .turn()
# .color          .heat()
# .doors          .park()


#         Dog Class
# Attributes:     Methods:
# .name           .eat()
# .breed          .sleep()
# .color          .bark()
# .height         .fetch()
# .weight         .chase_tail()


# Member Class

# Attributes:
# .username = Rambo
# .fullname = Rocco Moe
# ,email = rambo@gmail.com
# .date_joined = 01/19/2019
# is_active = True

# Methods:
# .archive()
# .restore()
# .delete()

# ##############################

# Attributes:
# .username = wblomgren
# .fullname = Wilbur Blomgren
# ,email = ww@gmail.com
# .date_joined = 03/2212019
# is_active = True

# Methods:
# .archive()
# .restore()
# .delete()

########################################################################################################################

# class Member:
#     '''Create a new member.'''
#     def __init__(self,uname,fname):
#         self.username = uname
#         self.fullname = fname

# new_guy = Member('Rambo','Rocco Moe')

# print(new_guy)
# print(new_guy.fullname)
# print(new_guy.username)
# print(type(new_guy))

# new_guy.username = 'Princess'

# print(new_guy.fullname)
# print(new_guy.username)

########################################################################################################################

# import datetime as dt

# class Member:
#     '''Create a new member.'''
#     def __init__(self,uname,fname):
#         self.username = uname
#         self.fullname = fname
#         self.date_joined = dt.date.today()
#         self.is_active = True
    
#     # A method to return a formatted string showing date joined.
#     def show_date_joined(self):
#         '''Show date joined'''
#         return f"{self.fullname} joined on {self.date_joined:%d.%m.%Y}"
    
#     # Method to activate (True) or deactive (False) account.
#     def activate(self, yesno):
#         '''True for active, False to make inactive'''
#         self.is_active = yesno

# # The class ends at the first unindented line.
# # Create an instance of the Member class named new_guy.
# new_guy = Member('Rambo', 'Rocco Moe')
# # See what's in the instance, change is active status.
# print(new_guy.show_date_joined())

# # Is the new guy active?
# print(new_guy.is_active)

# # Try out the activate method.
# new_guy.activate(False)

# # Is the new guy still active?
# print(new_guy.is_active)

########################################################################################################################

# import datetime as dt
# # Define a new class name Member.
# class Member:
#     # Default number of free days.
#     free_days=365
#     '''Create a new member.'''
#     def __init__(self, username, fullname) :
#         # Set date joined
#         self.date_joined = dt.date.today()
        
#         # Set an expiration date
#         self.free_expires = dt.date.today() + dt.timedelta(days = Member.free_days)

# # The class ends at the first un-indented I ine.
# # Create an instance of the Member class named new_guy.
# wilbur = Member( 'wblomgren', 'Wilbur Blomegren')
# print(wilbur.date_joined)
# print(wilbur.free_expires)

########################################################################################################################

# import datetime as dt
# # Define a new class named Member.
# class Member:
#     # Default number of free days.
#     free_days = 365
#     '''Create a new member.'''
#     def __init__ (self. username, fullname):
#         self.date_joined = dt.date.today()
#         # Set an expiration date.
#         self.free_expires = dt.date.today() + dt.timedelta(days=Member.free_days)
    
#     # Class methods fol Iow @classmethod decorctor and refer tc cıs rather than to self.
#     @classmethod
#     def setfreedays(cls,days):
#         cls.free_days = days

########################################################################################################################

# import datetime as dt
# # Define a class named Member for making member objects.
# class Member:
#     # This is a class variable that's the same for all instances.
#     free_days = 0
#     '''Create a member object from username and fullname'''
#     def __init__(self, username, fullname):
#         # Define properties and assign default values.
#         self. datejoined = dt.date.today()
#         self.free_expires = dt.date.today() + dt.timedelta(Member.free_days)
    
#     # Class methods follow @classmethods and use cls rathen than self.
#     @classmethod
#     def setfreedays(cls,days):
#         cls.free_days=days
    
#     @staticmethod
#     def currenttime():
#         now = dt.datetime.now()
#         return f"{now:%I:%M %p}"

# # Class definition ends at Last indented line
# # Try out the new static method (no object required)
# print (Member.currenttime())

########################################################################################################################

# import datetime as dt

# # Base cLass is used for all kinds of Members.
# class Member:
#     '''The Member class attributes and methods are for everyone'''
#     # By default, a new account expires in one year (365 days)
#     expiry_days = 365
#     # Initialize a member object.
#     def __init__ (self, firstname, lastname):
#         # Attributes (instance variables) for everybody.
#         self.firstname = firstname
#         self.lastname = lastname
#         # Calculate expiry date from today's date.
#         self.expiry_date = dt.date.today() + dt.timedelta(days=self.expiry_days)

# # Outside the class now.
# Joe = Member('Joe', 'Anybody')
# print(Joe.firstname)
# print(Joe.lastname)
# print(Joe.expiry_date)

########################################################################################################################

# import datetime as dt

# class Member:
#     '''The Member class attributes and methods are for everyone'''
#     # By default, a new account expires in one year (365 days)
#     expiry_days = 365
#     # Initialize a member object.
#     def __init__ (self, firstname, lastname):
#         # Attributes (instance variables) for everybody.
#         self.firstname = firstname
#         self.lastname = lastname
#         # Calculate expiry date from today's date.
#         self.expiry_date = dt.date.today() + dt.timedelta(days=self.expiry_days)

# # SubcLass for Admins.
# class Admin(Member):
#     pass
# # Subclass for Users.
# class User(Member):
#     pass
# Ann = Admin('Annie','Angst')
# print(Ann.firstname)
# print(Ann.lastname)
# print(Ann.expiry_date)
# print()
# Uli = User('Uli','Ungula')
# print(Uli.firstname)
# print(Uli.lastname)
# print(Uli.expiry_date)

########################################################################################################################

# import datetime as dt

# class Member:
#     '''The Member class attributes and methods are for everyone'''
#     # By default, a new account expires in one year (365 days)
#     expiry_days = 365
    
#     # Initialize a member object.
#     def __init__ (self, firstname, lastname):
#         # Attributes (instance variables) for everybody.
#         self.firstname = firstname
#         self.lastname = lastname
#         # Calculate expiry date from today's date.
#         self.expiry_date = dt.date.today() + dt.timedelta(days=self.expiry_days)
#         self.secret_code = ''
    
#     def show_expiry(self):
#         return f"{self.firstname} {self.lastname} expires on {self.expiry_date}"

#     # Method in base class
#     def get_status(self):
#         return f"{self.firstname} is a Member."

# class Admin(Member):
#     '''Admin accounts don't expire for 100 years'''
#     # By default, a new account expires in one year (365 days)
#     expiry_days = 365.2422*100
#     # Subclass parameters.
#     def __init__ (self, firstname, lastname, secret_code):
#         # Pass Member parameters on up to Member Class.
#         super().__init__(firstname, lastname)
#         # Assign th remaining parameter to this object
#         self.secret_code = secret_code
    
#     def get_status(self):
#         return f"{self.firstname} is a Admin."

# # Subclass for users
# class User (Member):
#     def get_status(self):
#         return f"{self.firstname} is a regular User."

# Ann = Admin('Annie','Angst', 'PRESTO')
# print(Ann.firstname, Ann.lastname, Ann.expiry_date, Ann.secret_code)
# print(Ann.show_expiry())

# Uli = User('Uli', 'Ungula')
# print(Uli.firstname, Uli.lastname, Uli.expiry_date, Uli.secret_code)
# print(Uli.show_expiry())


# print()
# print(Ann.get_status())
# print(Uli.get_status())

# Manny = Member('Mindy','Membo')
# print(Manny.get_status())
# print()
# # help(Admin) # Yardım çıktısı
# print(Admin.__dict__)


########################################################################################################################
# HATALARDAN KAÇINMA
########################################################################################################################

# try:
#     # Open file and show its name.
#     thefile = open('train.cvs') #py dosyasıyla aynı klasörde ise yalnızca isim yeterli.
#     print(thefile.name)
# except Exception:
#     print("Sorry, I don't see a file named train.cvs here")

########################################################################################################################

# try:
#     # Open file and show its name.
#     thefile = open('train.csv')
#     print(thefile.name)
#     print(thefile.wookems())
# except FileNotFoundError:
#     print("Sorry, I don't see a file named train.csv here") # Artık yalnıca dosyayı bulamazsa bu uyarıyı veriyor
# except AttributeError:
#     print("Sorry, I don't see the mentioned attribute here") # wookems olmadığı için bu uyarıyı verecek
# except Exception: 
#     print('it is a new exception different than you add') # Eklediğimiz istisnalardan farklı bir istisna olduğunu belirtir 
    
########################################################################################################################

# try:
#     # Open file and show its name.
#     thefile = open('train.csv')
#     # Print a couple blank lines then the first line from the file.
#     print('\n\n', thefile.readline())
#     thefile.wigwam()
# except FileNotFoundError:
#     print("Sorry, I don't see a file named train.csv here")
# except Exception as e:
#     print(e)

########################################################################################################################

# try:
#         # Open the file named people.csv
#         thefile = open('Python/Pandas/train.csv')
# # Watch for common error and stop program if it happens.
# except FileNotFoundError:
#         print("Sorry, I don't see a file named train.csv here")
# # Catch any unexpected error and stop the program if one happens.
# except Exception as e:
#         print(e)
# # Otherwise, if nothing bad has happened by now, just keep going.
# else:
#         # File must be open by now if we got here.
#         print('\n') # Print a blank line.
#         # Print each line from the file.
#         for one_line in thefile:
#                 print(one_line)
#         thefile.close()
#         print("Success!")

########################################################################################################################

# print('Do this first')
# try:
#         open('Python/Pandas/train.csv')
# except FileNotFoundError:
#         print('Cannot find file named people.csv')
# except Exception as e:
#         print(e)
# else:
#         print('Show this if there is no exception.')
# finally:
#         print('This is in the finally block')
# print("This is outside the try...except...else...finally")

########################################################################################################################

# try:
#         # Open the file ]
#         thefile = open('Python/Pandas/train.csv',)
#         # Count the number of lines in file.
#         line_count = len(thefile.readlines())
#         # If there are fewer than 2 lines, raise exception.
#         if line_count < 2:
#                 raise Exception

# # Handles missing file error.
# except FileNotFoundError:
#         print('\nThere is no train.csv file here')
        
# # Handles all other exceptions
# except Exception as e:
#         # Show the error.
#         print('\n\nFailed: The error was ' + str(e))
#         # Close the file.
#         thefile.close()
        
########################################################################################################################

# # Base class for defining your user-defined exceptİons.
# class Error(Exception):
#         '''Base class for other exceptions'''
#         pass
# # Now define your exceptİon as a subclass of
# class EmptyFileError(Error):
#         pass
# try:
#         # Open the file (no error check for this example).
#         thefile= open('Python/Pandas/train.csv')
#         # Count the number of lines in file.
#         line_count=len(thefile.readlines())
#         # If there are are fewer than 2 lines,
#         if line_count < 2:
#                 raise EmptyFileError
# # Handles missing file error.
# except FileNotFoundError:
#         print('\nThere is no train.csv file here')
# # Handles my custom for too few rows
# except EmptyFileError:
#         print("\nYour train.csv file doesn't have enough stuff.")
# # Handles all other exceptions
# except Exception as e:
#         # Show the error.
#         print('\n\nFailed: The error was '+str(e))
#         # Close the file.
#         thefile.close()
# else:
#         # This code runs only if no exception above.
#         print('\n') # Print a blank line.
#         # File must be open by now if we got here, Show content.
#         for one_line in thefile:
#                 print(one_line)
#         thefile.close()
#         print('Success!')
        
########################################################################################################################
# KÜTÜPHANELER
########################################################################################################################


# Text File                               Binary File
# • Plain text: .txt, .csv                • Executable: .exe, .dmg, .bin
# • Source code: .py, .html, .css, .js    • Images: .jpg, .png, .gif, .tiff, .ico
# • Data: .json, .xml                     • Video: .mp4, .m4v, .mp4, .mov
#                                         • Audio: .aif, .mp3, .mpa, .wav
#                                         • Compressed: .zip, .deb, star.gz
#                                         • Font: .woff, .otf, .ttf
#                                         • Document: .pdf, .docx, .xlsx


########################################################################################################################

# » r: (Read): Opens the file but does not allow Python to make any changes. This 
# is the default mode and is used if you don’t specify a mode. If the file doesn’t 
# exist, Python raises a FileNotFoundError exception.
# » r+: (Read/Write): Opens the file and allows Python to read and write to the 
# file.
# » a: (Append): Opens the file and allows Python to add content to the end of 
# the file but not change existing content. If the file doesn’t exist, this mode 
# creates the file.
# » w: (Write): Opens the file and allows Python to make changes to the file. 
# Creates the file if it doesn’t exist.
# » x: (Create): Creates the file if it doesn’t already exist. If the file does exist, it 
# raises a FileExistsError exception.

# If you already specified one of the preceding modes, just add this specification as another letter. 
# » t: (Text): Opens the file as a text file and allows Python to read and write text.
# » b: (Binary): Opens the file as a binary file and allows Python to read and write 
# bytes.

########################################################################################################################

# f = open('quotes.txt')
# filecontents = f.read()
# print(filecontents)
# f.close()

########################################################################################################################

# # ---------------- Contextual syntax - Eğer with ile açarsan wşth sonunda dosyayı otomatik kapar.
# with open('quotes.txt') as f:
#  filecontents = f.read()
#  print(filecontents)
# # The unindented line below is outside the with... block;
# print('File is closed: ', f.closed) 

########################################################################################################################

# # - Basic syntax to open, read, and display file contents.
# f = open('quotes.txt')
# filecontents = f.read()
# print(filecontents)
# # Returns True if the file is closed, otherwise False.
# print('File is closed: ', f.closed)
# # Closes the file.
# f.close() #Close the file.
# print() # Print a blank line.

# # ---------------- Contextual syntax
# with open('quotes.txt') as f:
#  filecontents = f.read()
#  print(filecontents)
# # The unindented line below is outside the with... block;
# print('File is closed: ', f.closed)

########################################################################################################################

# with open('happy.jpg', 'rb') as f: # Ham byte bilgilerini görüntüler. 
#         filecontents = f.read()
#         print(filecontents)

########################################################################################################################

# # Open file with encoding set to utf-8. - Türkçe karakter çözümü
# with open( 'names.txt' , 'r', encoding='utf-8') as f:
#         # Read entire file into variable named content.
#         content=f.read()
#         # Show that content.
#         print(content)

########################################################################################################################

# UTF-8 is short for Unicode Transformation Format, 8-bit, and is a standardized way to 
# represent letters and numbers on computers. The original ASCII set of characters, which 
# contains mostly uppercase and lowercase letters, numbers, and punctuation marks, 
# worked okay in the early days of computing. But when other languages were brought 
# into the mix, these characters were just not enough. Many standards for dealing with 
# other languages have been proposed and accepted over the years. Of those, UTF-8 has 
# steadily grown in use whereas most others declined. Today, UTF-8 is pretty much the 
# standard for all things Internet, and so it’s a good choice if you have to choose a character set for a project.
# If you’re looking for more history or technical info on UTF-8, take a look at these web 
# pages:

# • www.w3.org/International/questions/qa-what-is-encoding
# • https://pythonconquerstheuniverse.wordpress.com/2010/05/30/
# unicode-beginners-introduction-for-dummies-made-simple/
# • https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/

# If you get stuck trying to open a file that’s supposed to be UTF-8 but isn’t cooperating, do 
# a web search for convert file to utf-8 encoding. Then look for a web page or an app that 
# will work with your operating system to make the conversion.

########################################################################################################################

# » read([size]): Reads the entire file if you leave the parentheses empty. If you 
# specify a size inside the parentheses, it reads that many characters (for a text 
# file) or that many bytes (for a binary file).
# » readline(): Reads one line of the contents from a text file — the line ends 
# wherever there’s a newline character. (The newline character, \n, ends the line 
# that’s displayed and moves the cursor down to the next line.)
# » readlines(): Reads all the lines of a text file into a list.

########################################################################################################################

# # reads in all the contents, and then displays it
# with open('quotes.txt') as f:
#  # Read in entire file
#  content = f.read()
#  print(content)

# # read rows as an unit in a list
# with open('quotes.txt') as f:
#       content = f.readlines()
#       print(content)

# # read a row only
# with open('quotes.txt') as f:
#         content = f.readline()
#         print(content)

########################################################################################################################

# # Döngü olarak txt yazdırma 
# with open('quotes.txt') as f:
#         # Reads in all lines first, then loops through.
#         for one_line in f.readlines():
#                 print(one_line, end="") # end satırlar arasında ekstra boşluk vermesin diye kondu. 

########################################################################################################################

# with open('quotes.txt') as f:
#         # Reads in all lines first, then loops through.
#         # Count each line starting at zero.
#         for one_line in enumerate(f.readlines()):
#                 # If counter is even number, print with no extra newline
#                 if one_line[0] % 2 == 0:
#                         print(one_line[1], end='')
#                 # Otherwise print a couple spaces and an extra newline.
#                 else:
#                         print(' ' + one_line[1])

########################################################################################################################

# with open('quotes.txt') as f:
#         one_line = f.readline()
#         while one_line:
#                 print(one_line, end='')
#                 one_line = f.readline()

########################################################################################################################

# # Store a number to use as a loop counter.
# counter = 1
# # Open the file.
# with open('quotes.txt') as f:
#         # Read one line from the file.
#         one_line = f.readline()
#         # As long as there are lines to read...
#         while one_line:
#                 # If the counter is an even number, print a couple spaces.
#                 if counter % 2 == 0:
#                         print(' ' + one_line)
#                 # Otherwise print with no newline at the end.
#                 else:
#                         print(one_line, end='')
#                 # Increment the counter
#                 counter += 1
#                 # Read the next line.
#                 one_line = f.readline()

########################################################################################################################

# # New name to add with in to mark end of line.
# new_name = 'Pena Caldırön'
# # Open names.txt in append mode with encoding.
# with open( 'names.txt', 'a', encoding='utf-8') as f:
#         # Add the new name and in to the end of the file.
#         f.write (new_name)
# # File closes automatically after indentations.
# print( '\nDone ' )
# # Re-open the file with encoding and display contents
# with open('names.txt', encoding='utf-8') as f:
#         print(f. read())

########################################################################################################################

# # Satırların belgedeki kaçıncı karakter ile bittiğini gösterir
# with open('names.txt', encoding='utf-8') as f:
#         # Read first line to get started.
#         print(f.tell())
#         one_line = f.readline()
#         # Keep reading one line at a time until there are no more.
#         while one_line:
#                 print(one_line[:-1], f.tell())
#                 one_line = f.readline()

########################################################################################################################

# # Dosya kopyalayarak kopyayı oluşturma
# # Specify the file to copy
# file_to_copy='happy.jpg'
# #Create new file name with copy before the extension.
# name_parts = file_to_copy.split(".")
# new_file = name_parts[0] + '_copy.' + name_parts[1] # Yeni dosya oluşturuldu
# # Open the original file as read-only binary.
# with open(file_to_copy,'rb') as original_file:
#         # Create or open file to copy into.
#         with open(new_file, 'wb') as copy_to:
#                 # Grab a chunk of the original file (4MB) .
#                 chunk=original_file.read(4096)
#                 # Loop though until no more chunks.
#                 while len(chunk) > 0:
#                         copy_to.write(chunk)
#                         # Make sure you read the next chunk in this loop.
#                         chunk = original_file.read(4096)
# # Close is automatic after loops, Show done message
# print( 'Done! ' )

########################################################################################################################

# import csv
# # Open CSV file with UTF-8 encoding, don't read in newline characters.
# with open('sample.csv', encoding='utf-8', newline='') as f:
#         # Create a CVS row counter and row reader.
#         reader = enumerate(csv.reader(f))
#         # Loop through one row at a time, i is counter, row is entire row.
#         for i, row in reader:
#                 print(i, row)
# print('Done')

########################################################################################################################

# import csv
# # Open CSV file with UTF-8 encoding, don't read in newline characters.
# with open('sample.csv', encoding='utf-8', newline='') as f:
#         # # Create a CVS row counter and row reader.
#         reader = enumerate(csv.reader(f))
#         # Loop through one row at a time, i is counter, row is entire row.
#         for i, row in reader:
#                 # Row 0 is just column headings, ignore it.
#                 if i > 0:
#                         # Whole name split into two at comma.
#                         try:
#                                 full_name = row[0].split(',')
#                                 # Last name, strip extra spaces.
#                                 last_name=full_name[0].strip()
#                                 # First name, strip extra spaces.
#                                 first_name=full_name[1].strip()
#                         except IndexError:
#                                 full_name = last_name = first_name = ""
#                         print(first_name, last_name)
# print('Done!')

########################################################################################################################

# # 3. sütunu tarih olarak belirleme
# import datetime as dt
# date_joined = dt.datetime.strptime(row[2], "%m/%d/%Y").date()

########################################################################################################################

# import csv
# import datetime as dt
# # Open CSV file with UTF-8 encoding, don't read in newline characters.
# with open('sample.csv', encoding='utf-8', newline='') as f:
#         # Create a CVS row counter and row reader.
#         reader = enumerate(csv.reader(f))
#         # Loop through one row at a time, i is counter, row is entire row.
#         for i, row in reader:
#                 # Row 0 is just column headings, ignore it.
#                 if i > 0:
#                         # Whole name split into two at comma.
#                         try:
#                                 full_name = row[0].split(',')
#                                 # Last name, strip extra spaces.
#                                 last_name = full_name[0].strip()
#                                 # First name, strip extra spaces.
#                                 first_name = full_name[1].strip()
#                         except IndexError:
#                                 full_name = last_name = first_name = ""
#                         # Birth year integer, zero for empty string.
#                         birth_year = int(row[1] or 0)
#                         # Date_joined is a date.
#                         try:
#                                 date_joined = dt.datetime.strptime(row[2], "%m/%d/%Y").date()
#                         except ValueError:
#                                 date_joined = None
#                         print(first_name, last_name, birth_year, date_joined)
# print('Done!')

########################################################################################################################

# # Remove $, commas, leading trailing spaces.
# str_balance = (row[4].replace('$', '').replace(',', '')).strip()

########################################################################################################################

# import csv
# import datetime as dt
# # Open CSV file "ith UTF-8 encoding, don' t read in newline characters.
# with open('sample.csv', encoding='utf-8', newline='') as f:
#         # Create a CVS row counter and row reader.
#         reader = enumerate(csv.reader(f))
#         # through one row at a time, i İş counter,
#         for i, row in reader:
#                 # Row 0 is just column headings, ignore it.
#                 if i > 0:
#                         # whole name split into two at comma.
#                         try:
#                                 full_name = row[0].split(',')
#                                 # Last name, strip extra spaces.
#                                 last_name = full_name[0].strip()
#                                 # First name, strip extra spaces.
#                                 first_name = full_name[1].strip()
#                         except IndexError:
#                                 full_name = last_name = first_name = ""
#                         # Birth year integer, zero for empty string.
#                         birth_year = int(row[1] or O)
#                         # Date_joined is a date.
#                         try :
#                                 date_joined = dt.datetime.strptime(row[2], "%m.%d.%Y").date()
#                         except ValueError:
#                                 date_joined = None
#                         # is_active is a Boolean, automatically False for empty string.
#                         is_active = bool(row[3])
#                         # Remove $ , commas, leading and trailing spaces.
#                         str_balance = (row[4].replace('$','').replace(',','').strip())
#                         # Balance is a float or zero for empty string.
#                         balance = float(str_balance or O)
#                         print(first_name,last_name, birth_year, date_joined, is_active,balance)
# print('Done !')

########################################################################################################################

# import datetime as dt
# import csv
# # Use these functions to convert any string to appropriate Python data type.
# # Get just the first name from full name.
# def fname(any):
#         try:
#                 nm = any.split(',')
#                 return nm[1]
#         except IndexError:
#                 return ''
# # Get just the last name from full name.
# def lname(any):
#         try:
#                nm = any.split(',')
#                return nm[0]
#         except IndexError:
#                return ''
# # Convert string to integer or zero if no value.
# def integer(any):
#         return int(any or 0)
# # Convert mm/dd/yyyy date to date or None if no valid date.
# def date(any):
#         try:
#                 return dt.datetime.strptime(any,"%m/%d/%Y").date()
#         except ValueError:
#                 return None
# # Convert any string to Boolean, False if no value.
# def boolean(any):
#         return bool(any)
# # Convert string to float, or to zero if no value.
# def floatnum(any):
#         s_balance = (any.replace('$','').replace(',',''))
#         return float(s_balance or 0)
# # Create an empty list of people.
# people = []
# # Define a class where each person is an object.
# class Person:
#         def __init__(self, id, first_name, last_name, birth_year, date_joined, is_active, balance):
#                 self.id = id
#                 self.first_name = first_name
#                 self.last_name = last_name
#                 self.birth_year = birth_year
#                 self.date_joined = date_joined
#                 self.is_active = is_active
#                 self.balance = balance

# # Open CSV file with UTF-8 encoding, don't read in newline characters.
# with open('sample.csv', encoding='utf-8', newline='') as f:
#         # Set up a csv reader with a counter.
#         reader = enumerate(csv.reader(f))
#         # Skip the first row, which is column names.
#         f.readline()
#         # Loop through remaining rows one at a time, i is counter, row is
#         # entire row.
#         for i, row in reader:
#         # From each data row in the CSV file, create a Person object with unique
#         # id and appropriate data types, add to people list.
#                 people.append(Person(i, fname(row[0]), lname(row[0]), integer(row[1]), date(row[2]), boolean(row[3]), floatnum(row[4])))
# # When above loop is done, show all objects in the people list.
# for p in people:
#         print(p.id, p.first_name, p.last_name, p.birth_year, p.date_joined, p.is_active, p.balance)

########################################################################################################################

# import csv
# import datetime as dt
# # Get just the first name from full name.
# def fname(any):
#         try:
#                 nm = any.split(',')
#                 return nm[1]
#         except IndexError:
#                 return ''
# # Get just the last name from full name.
# def lname(any):
#         try:
#                 nm = any.split(',')
#                 return nm[0]
#         except IndexError:
#                 return ''
# # Convert string to integer or zero if no value.
# def integer(any):
#         return int(any or 0)
# # Convert mm/dd/yyyy date to date or None if no valid date.
# def date(any):
#         try:
#                 return dt.datetime.strptime(any, "%m/%d/%Y").date()
#         except ValueError:
#                 return None
# # Convert any string to Boolean, False if no value.
# def boolean(any):
#         return bool(any)
# # Convert string to float, or to zero if no value.
# def floatnum(any):
#         s_balance = (any.replace('$', '').replace(',', '')).strip()
#         return float(s_balance or 0)
# # Create an empty dictionary of people.
# people = {}
# # Open CSV file with UTF-8 encoding, don't read in newline characters.
# with open('sample.csv', encoding='utf-8', newline='') as f:
#         # Set up a csv reader with a counter.
#         reader = enumerate(csv.reader(f))
#         # Skip the first row, which is column names.
#         f.readline()
#         # Loop through remaining rows one at a time, i is counter, row is
#         # entire row.
#         for i, row in reader:
#                 # From each data row in the CSV file, create a Person object with
#                 # unique id and appropriate data types, add 
#                 # to people dictionary.
#                 newdict = dict({'first_name': fname(row[0]), 'last_name': lname(row[0]), 
#                         'birth_year': integer(row[1]), 'date_joined': date(row[2]), 
#                         'is_active' : boolean(row[3]), 'balance' :floatnum(row[4])})
#                 people[i + 1] = newdict


# # When above loop is done, show all objects in the people list.
# for person in people.keys():
#         id = person
#         print(id, people[person]['first_name'], \
#                   people[person]['last_name'], \
#                   people[person]['birth_year'], \
#                   people[person]['date_joined'], \
#                   people[person]['is_active'], \
#                   people[person]['balance'])

########################################################################################################################

# import csv
# import datetime as dt

# # Get just the first name from full name.
# def fname(any):
#         try:
#                 nm = any.split(',')
#                 return nm[1]
#         except IndexError:
#                 return ''
# # Get just the last name from full name.
# def lname(any):
#         try:
#                 nm = any.split(',')
#                 return nm[0]
#         except IndexError:
#                 return ''
# # Convert string to integer or zero if no value.
# def integer(any):
#         return int(any or 0)
# # Convert mm/dd/yyyy date to date or None if no valid date.
# def date(any):
#         try:
#                 return dt.datetime.strptime(any, "%m/%d/%Y").date()
#         except ValueError:
#                 return None
# # Convert any string to Boolean, False if no value.
# def boolean(any):
#         return bool(any)
# # Convert string to float, or to zero if no value.
# def floatnum(any):
#         s_balance = (any.replace('$', '').replace(',', '')).strip()
#         return float(s_balance or 0)
# # Create an empty list
# people = []
# # Define a class where
# class Person:
#         def __init__ (self, id, first_name, last_name, birth_year, date_joined, is_active, balance) :
#                 self.first_name = first_name
#                 self.last_name = last_name
#                 self.birth_year = birth_year
#                 self.date_joined = date_joined
#                 self.is_active = is_active
#                 self.balance = balance
# # Open CSV file with UT F-8 encodings don' t read in newline characters.
# with open("sample.csv", encoding='utf-8', newline="") as f:
#         # Set up a csv reader with a counter.
#         reader = enumerate(csv.reader(f))
#         # Skip the first row, whİch is column names.
#         f.readline()
#         # Loop through remaining rows one at a time, i is counter, row is entire row.
#         for i, row in reader:
#                 # From each data row in CSV file, create a person object with unique id and appropriate data types, add to people list
#                 people.append(Person(i, fname[row[0]], lname[row[0]], integer(row[1]), date(row[2]), boolean(row[3]), floatnum(row[4])))
# # When above Ioop is done, Show
# for p in people:
#         #the CSV file, create a Person object with unique id and appropriate data types, add to people list.
#         print(p.id, p.first_name, p.last_name, p.birth_year, p.date_joined,p.is_active, p.balance)

########################################################################################################################
# Juggling JSON Data
########################################################################################################################

# CONVERTING EXCEL TO JSON
# In case you’re wondering, to convert that sample Excel spreadsheet to JSON, set your 
# browser to www.convertcsv.com/csv-to-json.htm and follow these steps:
# 1. In Step 1, open the Choose File tab, set the Encoding to UTF-8, click the Choose File 
# button, select your Excel file, and click Open.
# 2. In Step 2, make sure the First Row Is Column Names option is selected and set Skip 
# # of Lines to 1 to skip the column headings row.
# 3. In Step 5, click the CSV to JSON button.
# 4. Next to Save Your Result, type a filename and then click the Download Result 
# button.
# The file should end up in your Downloads folder (or to whatever location you normally 
# download) with a .json extension. It’s a plain text file, so you can open it with any text 
# editor or a code editor such as VS Code. The converter automatically skips empty rows 
# in Excel files, so your JSON file won’t contain any data for empty rows in a spreadsheet. 
# If you often work with Excel, CSV, JSON, and similar types of data, you may want to 
# spend some time exploring the many tools and capabilities that the www.convertcsv.
# com website provides.


########################################################################################################################


# Method                  Purpose
# json.dump()             Write (serialize) Python data to a JSON file (or stream).
# json.dumps()            Write (serialize) a Python object to a JSON string.
# json.load()             Load (deserialize) JSON from a file or similar object.
# json.loads()            Load (deserialize) JSON data from a string.

########################################################################################################################


# Python          JSON
# dict            object
# list,           tuple array
# str             string
# int and float   number
# True            true
# False           false
# None            null

########################################################################################################################

# import json
# # This is the Excel data (no keys)
# filename = 'people_from_excel.json'
# # Open the file (standard file open stuff)
# with open(filename, 'r', encoding='utf-8', newline='') as f:
#  # Load the whole json file into an object named people
#  people = json.load(f)
#  # print(people)
#  for p in people:
#         print(p['Full Name'], p['Birth Year'], p['Date Joined'], p['Is Active'], p['Balance'])
#  print(type(people))

########################################################################################################################

# import json, xlrd
# import datetime as dt
# # This is the Excel data (no keys)
# filename = 'people_from_excel.json'
# # Open the file (standard file open stuff)
# with open(filename, 'r', encoding='utf-8', newline='') as f:
#  # Load the whole json file into an object named people
#  people = json.load(f)
# # Dictionaries are in a list, loop through and display each dictionary.
# for p in people:
#  name = p['Full Name']
#  byear = p['Birth Year']
#  y, m, d, h, i, s = xlrd.xldate_as_tuple(p['Date Joined'], 0)
#  joined = dt.date(y, m, d)
#  # Excel date pretty tricky, use xlrd module.
#  balance = '$' + f"{p['Balance']:,.2f}"
#  print(f"{name:<22} {byear} {joined:%m/%d/%Y} {balance:>12}") # HATA VERİYOR

########################################################################################################################

# import json
# # Here the JSON data is in a big string named json_string.
# # It starts with the first triple quotation marks and extends
# # down to the last triple quotation marks.
# json_string = """
# {
# "people": [
#  {
#  "Full Name": "Angst, Annie",
#  "Birth Year": 1982,
#  "Date Joined": "01/11/2011",
#  "Is Active": true,
#  "Balance": 300
#  },
#  {
#  "Full Name": "Schadenfreude, Sandy",
#  "Birth Year": 2004,
#  "Date Joined": "03/03/2003",
#  "Is Active": true,
#  "Balance": 0
#  }
# ]
# }
# """

# # Load JSON data from the big json_string string.
# peep_data = json.loads(json_string)

# # Now you can loop through the peep_data collection.
# for p in peep_data['people']:
#  print(p["Full Name"], p["Birth Year"], p["Date Joined"],p['Is Active'],p['Balance'])

########################################################################################################################

# import json
# # Here the JSON data is in a big string named json_string.
# # It starts with the first triple quotation marks and extends
# # down to the last triple quotation marks.
# json_string = """
#  {
#  "1": {
#  "count": 9061,
#  "lastreferrer": "https://difference-engine.com/Courses/tml-5-1118/",
#  "lastvisit": "12/20/2018",
#  "page": "/etg/downloadpdf.html"
#  },
#  "2": {
#  "count": 3342,
#  "lastreferrer": "https://alansimpson.me/",
#  "lastvisit": "12/19/2018",
#  "page": "/html_css/index.html"
#  }
#  }
# """
# # Load JSON data from the big json_string string.
# hits_data = json.loads(json_string)
# # Now you can loop through the hits_data collection.
# for k, v in hits_data.items():
#  print(f"{k}. {v['count']:>5} - {v['page']} - {v['lastvisit']} - {v['lastreferrer']}")

########################################################################################################################

# import json
# import datetime as dt
# # This is the Firebase JSON data (keyed).
# filename = 'firebase_hitcounts.json'
# # Open the file (standard file open stuff) .
# with open(filename, encoding='utf-8', newline='') as f:
#         # Load the whole json file into an object named hits.
#         hits = json.load(f)
# # Loop through the new hits data dictionary.
# for k, v in hits.items():
# # Convert the Firebase date to a Python date.
#  pydate= dt.datetime.utcfromtimestamp(v['lastvisit']/1000).date()
# # in the dictionary, replace the Firebase date with string of Python date.
#  v['lastvisit'] = f"{pydate:%m/%d/%Y}"
# # Remove the entire last referrer column.
#  v.pop('lastreferrer', None)
# # Write the modifed data to a JSON file named hitcounts_new.json.
# with open('hitcounts_new.json', encoding='utf-8') as out_file:
#         json.dump(hits, out_file, ensure_ascii=False, sort_keys=True)
# print( 'Done ' )

########################################################################################################################
# Interacting with the Internet
########################################################################################################################

# Protocol        Host or subdomain name          Domain name
# https://        support                         .apple.com/

# https://alansimpson.me/         python/cheatsheets/beginner/index.html
#                                 Path to folder and/or page

# Query string = https://www.google.com/search?   q=python+urllib+tutorial & tbm=vid
#                                                 name = value              name = value

########################################################################################################################

# 
# Code  Meaning         Reason
# 200   Okay            No problems exist.
# 400   Bad             Request The server is available but can’t make sense of your request, usually because something is wrong with your URL.
# 403   Forbidden       The site has detected that you’re accessing it programmatically, which it doesn’t allow.
# 404   Not found       Either the URL is wrong or the URL is right but the content that is no longer there.

########################################################################################################################

# Package         Purpose
# request         Opens URLs
# response        Handles the response that arrived; you don’t need to work with it directly
# error           Handles request exceptions
# parse           Breaks up the url into smaller chunks
# robotparser     Analyzes a site’s robots.txt file, which grants permissions to bots that are trying to access the site programmatically

########################################################################################################################

# # Import the request module from urllib library.
# from urllib import request
# # URL (address) of the desired page.
# sample_url = 'https://AlanSimpson.me/python/sample.html'
# # Request the page and put it in a variable named thepage.
# thepage = request.urlopen(sample_url)
# # Put the response code in a variable named status.
# status = thepage.code
# # What is the data type of the page?
# print(type(thepage))
# # What is the status code?
# print(status)

########################################################################################################################

# import requests
 
# # Making a GET request
# r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
 
# # check status code for response received
# # success code - 200
# print(r)
 
# # print content of request
# print(r.content)

########################################################################################################################

# Note that each link consists of several tags, as summarized here:

# » <a> ... </a>: The a (anchor) tags define where the browser should take 
# users when they click the link. The href= part of the <a> tag is the URL of the 
# page to which users should be taken.

# » <img>: The img tag defines the image that appears for each link. The src=
# attribute in the tag defines the source of the image — in other words, the 
# location and filename to display for that link.

# » <span> ... </span>: At the bottom of the link is text enclosed in 
# <span> ... </span> tags. That text appears at the bottom of each link 
# as white text against a black background.

########################################################################################################################

# import requests
# from bs4 import BeautifulSoup

# page_url = 'https://alansimpson.me/python/scrape_sample.html'
# headers = {
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
# }
# rawpage = requests.get(page_url,headers=headers)
# soup = BeautifulSoup(rawpage.content, 'html.parser')
# content = soup.article

# links_list = []
# for link in content.find_all('a'):
#     try:
#         url = link.get('href')
#         img = link.img.get('src')
#         text = link.span.text
#         links_list.append({'url' : url, 'img' : img, 'text' : text})
#     except AttributeError:
#         pass
# print("Total data scraped: " + str(len(links_list)))

# for link in links_list:
#     print(link)

# # Json'a kaydetme

# # If you want to dump data to the json file.
# import json

# # Save as a JSON file.
# with open('links.json', 'w', encoding='utf-8') as links_file:
#     json.dump(links_list, links_file, ensure_ascii=False)



# # csv'ye kaydetme

# # If you want to save to CSV.
# import csv

# # Save it to a CSV.
# with open('links.csv', 'w', newline='') as csv_out:
#     csv_writer = csv.writer(csv_out)
#     # Create the header row
#     csv_writer.writerow(['url', 'img', 'text'])
#     for row in links_list:
#         csv_writer.writerow([str(row['url']),str(row['img']),str(row['text'])])

# print('done')

########################################################################################################################

# The three items of data we want are as follows:
# » Link url, which is enclosed in quotation marks after the href= in the <a> tag
# » Image source, which is enclosed in quotation marks after src= in the img tag
# » Link text, which is enclosed in <span> ... </span> tags

########################################################################################################################
# Libraries, Packages, and Modules
########################################################################################################################

# print(dir(str))

# sonuç:

# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__',
#  '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', 
#  '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', 
# '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', 
# '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', 
# '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 
# 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 
# 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 
# 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 
# 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 
# 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 
# 'title', 'translate', 'upper', 'zfill']

# print(help(str))

# sonuç:

# Help on class str in module builtins:

# class str(object)
#  |  str(object='') -> str
#  |  str(bytes_or_buffer[, encoding[, errors]]) -> str
#  |
#  |  Create a new string object from the given object. If encoding or
#  |  errors is specified, then the object must expose a data buffer
#  |  that will be decoded using the given encoding and error handler.
#  |  Otherwise, returns the result of object.__str__() (if defined)
#  |  or repr(object).
#  |  encoding defaults to sys.getdefaultencoding().
#  |  errors defaults to 'strict'.
#  |
#  |  Methods defined here:
#  |
#  |  __add__(self, value, /)
#  |      Return self+value.
#  |
#  |  __contains__(self, key, /)
#  |      Return key in self.
#  |
#  |  __eq__(self, value, /)
#  |      Return self==value.
#  |
#  |  __format__(self, format_spec, /)
#  |      Return a formatted version of the string as described by format_spec.
#  |
#  |  __ge__(self, value, /)
#  |      Return self>=value.
#  |
#  |  __getattribute__(self, name, /)
#  |      Return getattr(self, name).
#  |
#  |  __getitem__(self, key, /)
#  |      Return self[key].
#  |
#  |  __getnewargs__(...)
#  |
#  |  __gt__(self, value, /)
#  |      Return self>value.
#  |
#  |  __hash__(self, /)
#  |      Return hash(self).
#  |
#  |  __iter__(self, /)
#  |      Implement iter(self).
#  |
#  |  __le__(self, value, /)
#  |      Return self<=value.
#  |
#  |  __len__(self, /)
#  |      Return len(self).
#  |
#  |  __lt__(self, value, /)
#  |      Return self<value.
#  |
#  |  __mod__(self, value, /)
#  |      Return self%value.
#  |
#  |  __mul__(self, value, /)
#  |      Return self*value.
#  |
#  |  __ne__(self, value, /)
#  |      Return self!=value.
#  |
#  |  __repr__(self, /)
#  |      Return repr(self).
#  |
#  |  __rmod__(self, value, /)
#  |      Return value%self.
#  |
#  |  __rmul__(self, value, /)
#  |      Return value*self.
#  |
#  |  __sizeof__(self, /)
#  |      Return the size of the string in memory, in bytes.
#  |
#  |  __str__(self, /)
#  |      Return str(self).
#  |
#  |  capitalize(self, /)
#  |      Return a capitalized version of the string.
#  |
#  |      More specifically, make the first character have upper case and the rest lower
#  |      case.
#  |
#  |  casefold(self, /)
#  |      Return a version of the string suitable for caseless comparisons.
#  |
#  |  center(self, width, fillchar=' ', /)
#  |      Return a centered string of length width.
#  |
#  |      Padding is done using the specified fill character (default is a space).
#  |
#  |  count(...)
#  |      S.count(sub[, start[, end]]) -> int
#  |
#  |      Return the number of non-overlapping occurrences of substring sub in
#  |      string S[start:end].  Optional arguments start and end are
#  |      interpreted as in slice notation.
#  |
#  |  encode(self, /, encoding='utf-8', errors='strict')
#  |      Encode the string using the codec registered for encoding.
#  |
#  |      encoding
#  |        The encoding in which to encode the string.
#  |      errors
#  |        The error handling scheme to use for encoding errors.
#  |        The default is 'strict' meaning that encoding errors raise a
#  |        UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
#  |        'xmlcharrefreplace' as well as any other name registered with
#  |        codecs.register_error that can handle UnicodeEncodeErrors.
#  |
#  |  endswith(...)
#  |      S.endswith(suffix[, start[, end]]) -> bool
#  |
#  |      Return True if S ends with the specified suffix, False otherwise.
#  |      With optional start, test S beginning at that position.
#  |      With optional end, stop comparing S at that position.
#  |      suffix can also be a tuple of strings to try.
#  |
#  |  expandtabs(self, /, tabsize=8)
#  |      Return a copy where all tab characters are expanded using spaces.
#  |
#  |      If tabsize is not given, a tab size of 8 characters is assumed.
#  |
#  |  find(...)
#  |      S.find(sub[, start[, end]]) -> int
#  |
#  |      Return the lowest index in S where substring sub is found,
#  |      such that sub is contained within S[start:end].  Optional
#  |      arguments start and end are interpreted as in slice notation.
#  |
#  |      Return -1 on failure.
#  |
#  |  format(...)
#  |      S.format(*args, **kwargs) -> str
#  |
#  |      Return a formatted version of S, using substitutions from args and kwargs.
#  |      The substitutions are identified by braces ('{' and '}').
#  |
#  |  format_map(...)
#  |      S.format_map(mapping) -> str
#  |
#  |      Return a formatted version of S, using substitutions from mapping.
#  |      The substitutions are identified by braces ('{' and '}').
#  |
#  |  index(...)
#  |      S.index(sub[, start[, end]]) -> int
#  |
#  |      Return the lowest index in S where substring sub is found,
#  |      such that sub is contained within S[start:end].  Optional
#  |      arguments start and end are interpreted as in slice notation.
#  |
#  |      Raises ValueError when the substring is not found.
#  |
#  |  isalnum(self, /)
#  |      Return True if the string is an alpha-numeric string, False otherwise.
#  |
#  |      A string is alpha-numeric if all characters in the string are alpha-numeric and
#  |      there is at least one character in the string.
#  |
#  |  isalpha(self, /)
#  |      Return True if the string is an alphabetic string, False otherwise.
#  |
#  |      A string is alphabetic if all characters in the string are alphabetic and there
#  |      is at least one character in the string.
#  |
#  |  isascii(self, /)
#  |      Return True if all characters in the string are ASCII, False otherwise.
#  |
#  |      ASCII characters have code points in the range U+0000-U+007F.
#  |      Empty string is ASCII too.
#  |
#  |  isdecimal(self, /)
#  |      Return True if the string is a decimal string, False otherwise.
#  |
#  |      A string is a decimal string if all characters in the string are decimal and
#  |      there is at least one character in the string.
#  |
#  |  isdigit(self, /)
#  |      Return True if the string is a digit string, False otherwise.
#  |
#  |      A string is a digit string if all characters in the string are digits and there
#  |      is at least one character in the string.
#  |
#  |  isidentifier(self, /)
#  |      Return True if the string is a valid Python identifier, False otherwise.
#  |
#  |      Call keyword.iskeyword(s) to test whether string s is a reserved identifier,
#  |      such as "def" or "class".
#  |
#  |  islower(self, /)
#  |      Return True if the string is a lowercase string, False otherwise.
#  |
#  |      A string is lowercase if all cased characters in the string are lowercase and
#  |      there is at least one cased character in the string.
#  |
#  |  isnumeric(self, /)
#  |      Return True if the string is a numeric string, False otherwise.
#  |
#  |      A string is numeric if all characters in the string are numeric and there is at
#  |      least one character in the string.
#  |
#  |  isprintable(self, /)
#  |      Return True if the string is printable, False otherwise.
#  |
#  |      A string is printable if all of its characters are considered printable in
#  |      repr() or if it is empty.
#  |
#  |  isspace(self, /)
#  |      Return True if the string is a whitespace string, False otherwise.
#  |
#  |      A string is whitespace if all characters in the string are whitespace and there
#  |      is at least one character in the string.
#  |
#  |  istitle(self, /)
#  |      Return True if the string is a title-cased string, False otherwise.
#  |
#  |      In a title-cased string, upper- and title-case characters may only
#  |      follow uncased characters and lowercase characters only cased ones.
#  |
#  |  isupper(self, /)
#  |      Return True if the string is an uppercase string, False otherwise.
#  |
#  |      A string is uppercase if all cased characters in the string are uppercase and
#  |      there is at least one cased character in the string.
#  |
#  |  join(self, iterable, /)
#  |      Concatenate any number of strings.
#  |
#  |      The string whose method is called is inserted in between each given string.
#  |      The result is returned as a new string.
#  |
#  |      Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
#  |
#  |  ljust(self, width, fillchar=' ', /)
#  |      Return a left-justified string of length width.
#  |
#  |      Padding is done using the specified fill character (default is a space).
#  |
#  |  lower(self, /)
#  |      Return a copy of the string converted to lowercase.
#  |
#  |  lstrip(self, chars=None, /)
#  |      Return a copy of the string with leading whitespace removed.
#  |
#  |      If chars is given and not None, remove characters in chars instead.
#  |
#  |  partition(self, sep, /)
#  |      Partition the string into three parts using the given separator.
#  |
#  |      This will search for the separator in the string.  If the separator is found,
#  |      returns a 3-tuple containing the part before the separator, the separator
#  |      itself, and the part after it.
#  |
#  |      If the separator is not found, returns a 3-tuple containing the original string
#  |      and two empty strings.
#  |
#  |  removeprefix(self, prefix, /)
#  |      Return a str with the given prefix string removed if present.
#  |
#  |      If the string starts with the prefix string, return string[len(prefix):].
#  |      Otherwise, return a copy of the original string.
#  |
#  |  removesuffix(self, suffix, /)
#  |      Return a str with the given suffix string removed if present.
#  |
#  |      If the string ends with the suffix string and that suffix is not empty,
#  |      return string[:-len(suffix)]. Otherwise, return a copy of the original
#  |      string.
#  |
#  |  replace(self, old, new, count=-1, /)
#  |      Return a copy with all occurrences of substring old replaced by new.
#  |
#  |        count
#  |          Maximum number of occurrences to replace.
#  |          -1 (the default value) means replace all occurrences.
#  |
#  |      If the optional argument count is given, only the first count occurrences are
#  |      replaced.
#  |
#  |  rfind(...)
#  |      S.rfind(sub[, start[, end]]) -> int
#  |
#  |      Return the highest index in S where substring sub is found,
#  |      such that sub is contained within S[start:end].  Optional
#  |      arguments start and end are interpreted as in slice notation.
#  |
#  |      Return -1 on failure.
#  |
#  |  rindex(...)
#  |      S.rindex(sub[, start[, end]]) -> int
#  |
#  |      Return the highest index in S where substring sub is found,
#  |      such that sub is contained within S[start:end].  Optional
#  |      arguments start and end are interpreted as in slice notation.
#  |
#  |      Raises ValueError when the substring is not found.
#  |
#  |  rjust(self, width, fillchar=' ', /)
#  |      Return a right-justified string of length width.
#  |
#  |      Padding is done using the specified fill character (default is a space).
#  |
#  |  rpartition(self, sep, /)
#  |      Partition the string into three parts using the given separator.
#  |
#  |      This will search for the separator in the string, starting at the end. If
#  |      the separator is found, returns a 3-tuple containing the part before the
#  |      separator, the separator itself, and the part after it.
#  |
#  |      If the separator is not found, returns a 3-tuple containing two empty strings
#  |      and the original string.
#  |
#  |  rsplit(self, /, sep=None, maxsplit=-1)
#  |      Return a list of the substrings in the string, using sep as the separator string.
#  |
#  |        sep
#  |          The separator used to split the string.
#  |
#  |          When set to None (the default value), will split on any whitespace
#  |          character (including \\n \\r \\t \\f and spaces) and will discard
#  |          empty strings from the result.
#  |        maxsplit
#  |          Maximum number of splits (starting from the left).
#  |          -1 (the default value) means no limit.
#  |
#  |      Splitting starts at the end of the string and works to the front.
#  |
#  |  rstrip(self, chars=None, /)
#  |      Return a copy of the string with trailing whitespace removed.
#  |
#  |      If chars is given and not None, remove characters in chars instead.
#  |
#  |  split(self, /, sep=None, maxsplit=-1)
#  |      Return a list of the substrings in the string, using sep as the separator string.
#  |
#  |        sep
#  |          The separator used to split the string.
#  |
#  |          When set to None (the default value), will split on any whitespace
#  |          character (including \\n \\r \\t \\f and spaces) and will discard
#  |          empty strings from the result.
#  |        maxsplit
#  |          Maximum number of splits (starting from the left).
#  |          -1 (the default value) means no limit.
#  |
#  |      Note, str.split() is mainly useful for data that has been intentionally
#  |      delimited.  With natural text that includes punctuation, consider using
#  |      the regular expression module.
#  |
#  |  splitlines(self, /, keepends=False)
#  |      Return a list of the lines in the string, breaking at line boundaries.
#  |
#  |      Line breaks are not included in the resulting list unless keepends is given and
#  |      true.
#  |
#  |  startswith(...)
#  |      S.startswith(prefix[, start[, end]]) -> bool
#  |
#  |      Return True if S starts with the specified prefix, False otherwise.
#  |      With optional start, test S beginning at that position.
#  |      With optional end, stop comparing S at that position.
#  |      prefix can also be a tuple of strings to try.
#  |
#  |  strip(self, chars=None, /)
#  |      Return a copy of the string with leading and trailing whitespace removed.
#  |
#  |      If chars is given and not None, remove characters in chars instead.
#  |
#  |  swapcase(self, /)
#  |      Convert uppercase characters to lowercase and lowercase characters to uppercase.
#  |
#  |  title(self, /)
#  |      Return a version of the string where each word is titlecased.
#  |
#  |      More specifically, words start with uppercased characters and all remaining
#  |      cased characters have lower case.
#  |
#  |  translate(self, table, /)
#  |      Replace each character in the string using the given translation table.
#  |
#  |        table
#  |          Translation table, which must be a mapping of Unicode ordinals to
#  |          Unicode ordinals, strings, or None.
#  |
#  |      The table must implement lookup/indexing via __getitem__, for instance a
#  |      dictionary or list.  If this operation raises LookupError, the character is
#  |      left untouched.  Characters mapped to None are deleted.
#  |
#  |  upper(self, /)
#  |      Return a copy of the string converted to uppercase.
#  |
#  |  zfill(self, width, /)
#  |      Pad a numeric string with zeros on the left, to fill a field of the given width.
#  |
#  |      The string is never truncated.
#  |
#  |  ----------------------------------------------------------------------
#  |  Static methods defined here:
#  |
#  |  __new__(*args, **kwargs) from builtins.type
#  |      Create and return a new object.  See help(type) for accurate signature.
#  |
#  |  maketrans(...)

########################################################################################################################

# pip --version
# pip 23.2.1 from D:\Kısayol\venv\kmd\kmd\Lib\site-packages\pip (python 3.11)

########################################################################################################################

# pip list

# Package            Version
# ------------------ ---------
# beautifulsoup4     4.12.2
# bs4                0.0.1
# certifi            2023.7.22
# charset-normalizer 3.2.0
# html5lib           1.1
# idna               3.4
# numpy              1.25.2
# pandas             2.0.3
# pip                23.2.1
# python-dateutil    2.8.2
# pytz               2023.3
# requests           2.31.0
# setuptools         65.5.0
# six                1.16.0
# soupsieve          2.4.1
# tzdata             2023.3
# urllib3            2.0.4
# webencodings       0.5.1
# xlrd               2.0.1

########################################################################################################################

# Halihazırda sahip olmadığınız paketleri kurmak için pip kullanmakta bir sorun olmasa da, 
# tek dezavantajı bu paketlerin Anaconda Navigator'ın kurulu paketler listesinde 
# görünmeyebilmesidir. Bunu aşmak için, yüklemek için bir şeyi pipleme talimatı gördüğünüzde, 
# pip'i conda (Anaconda'nın kısaltması) ile değiştirmeyi deneyin. Bu, paketi koleksiyonunuza 
# ekler, böylece hem pip list yaptığınızda hem de Anaconda Navigator'da listeye baktığınızda 
# görünecektir.

########################################################################################################################

# Tarihleri ve para birimi değerlerini biçimlendirmeyi basitleştirmek için üç işlev 
# istediğinizi varsayalım. Her işlev için istediğiniz adı oluşturabilirsiniz. 
# Çalışan örneğimiz için şu üç adı kullanacağız:

#  to_date(any_str): Pass in any string (any_str) date in mm/dd/yy or mm/dd/
# yyyy format and the function sends back a Python datetime.date that you
# can use for date calculations.
# » mdy(any_date): Pass in any Python date or datetime, and the function
# returns a string date formatted in mm/dd/yyyy format for display on the
# screen.
# » to_curr(any_num, len): Pass in any Python float or integer number and
# the function returns a string with a leading dollar sign, commas in thousands
# places, and two digits for the pennies. len is an optional number for length. If
# provided, the return value will be padded on the left with spaces to match the
# length specified.

# Contains custom functions for dates and currency values.
# import datetime as dt

# def to_date(any_str):
#     """ Convert mm/dd/yy or mm/dd/yyyy string to datetime.date, or None if
#     invalid date. """
#     try:
#         if len(any_str) == 10:
#             the_date = dt.datetime.strptime(any_str,'%m/%d/%Y').date()
#         else:
#             the_date = dt.datetime.strptime(any_str,'%m/%d/%y').date()
#     except (ValueError, TypeError):
#         the_date = None
#     return the_date

# def dmy(any_date):
#     """ Returns a string date in mm/dd/yyyy format. Pass in Python date or string date in mm/dd/yyyy format """
#     if type(any_date) == str:
#         any_date = to_date(anydate)
#     # Make sure a datetime is being forwarded
#     if isinstance(any_date,dt.date):
#         s_date = f"{any_date:'%d.%m.%Y'}"
#     else:
#         s_date = "Invalid date"
#     return s_date

# def to_curr(anynum, len=0):
#     """ Returns a number as a string with $ and commas. Length is optional """
#     s = "Invalid amount"
#     try:
#         x = float(anynum)
#     except ValueError:
#         x= None
#     if isinstance(x,float):
#         s = '$' + f"{x:,.2f}"
#         if len > 0:
#             s=s.rjust(len)
#     return s

# Devam etmek istiyorsanız aynı dosyayı oluşturabilir ve myfunc.py olarak adlandırabilirsiniz. 
# Dosyanın yalnızca işlevleri içerdiğini unutmayın. 
# Yani çalıştırırsanız ekranda herhangi bir işlem yapmayacaktır çünkü herhangi bir işlevi çağıran bir kod yoktur. 
# Bu işlevleri yazdığınız bir Python uygulamasında veya programında kullanmak için, 
# önce myfunc.py dosyasını yazmakta olduğunuz Python kodunun geri kalanıyla aynı klasöre kopyaladığınızdan emin olun. 
# Ardından, yeni bir program oluşturduğunuzda, myfunc'u bir başkası tarafından oluşturulmuş herhangi bir modülde 
# olduğu gibi bir modül olarak içe aktarın:

# import myfunc


# # Import all the code from myfunc.py as my.
# import myfunc as my
# # Need dates in this code
# from datetime import datetime as dt
# # Some simple test data.
# string_date="12/31/2019"
# # Convert string date to datetime.date
# print(my.to_date(string_date))
# today = dt.today()
# # Show today's date in mm/dd/yyyy format.
# print(my.mdy(today))
# dollar_amt=12345.678
# # Show this big number in currency format.
# print(my.to_curr(dollar_amt))

# VEYA

# # Import all the code from myfunc.py by name.
# from myfunc import to_date, mdy, to_curr
# # Need dates in this code
# from datetime import datetime as dt
# # Some simple test data.
# string_date="12/31/2019"
# # Convert string date to datetime.date
# print(to_date(string_date))
# today = dt.today()
# # Show today's date in mm/dd/yyyy format.
# print(mdy(today))
# dollar_amt=12345.678
# # Show this big number in currency format.
# print(to_curr(dollar_amt))

########################################################################################################################
# Using Artificial Intelligence
########################################################################################################################

# Makine öğreniminde aşağıdakiler gibi birçok farklı teknik kullanılır:

# » İstatistiksel analiz
# » Nöral ağlar
# » Karar ağaçları
# » Evrimsel algoritmalar

########################################################################################################################
# Building a Neural Network
########################################################################################################################

# # 2 Layer Neural Network in NumPy
# import numpy as np
# # X = input of our 3 input XOR gate

# # set up the inputs of the neural network (right from the table)
# X = np.array(([0,0,0],[0,0,1],[0,1,0], \
#  [0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]), dtype=float)

# # y = our output of our neural network
# y = np.array(([1], [0], [0], [0], [0], \
#  [0], [0], [1]), dtype=float)

# # what value we want to predict
# xPredicted = np.array(([0,0,1]), dtype=float)

# X = X/np.amax(X, axis=0) # maximum of X input array
# # maximum of xPredicted (our input data for the prediction)
# xPredicted = xPredicted/np.amax(xPredicted, axis=0)

# # set up our Loss file for graphing
# lossFile = open("SumSquaredLossList.csv", "w")

# class Neural_Network (object):
#     def __init__(self):
#         #parameters
#         self.inputLayerSize = 3 # X1,X2,X3
#         self.outputLayerSize = 1 # Y1
#         self.hiddenLayerSize = 4 # Size of the hidden layer
#         # build weights of each layer
#         # set to random values
#         # look at the interconnection diagram to make sense of this
#         # 3x4 matrix for input to hidden
#         self.W1 = \
#         np.random.randn(self.inputLayerSize, self.hiddenLayerSize)
#         # 4x1 matrix for hidden layer to output
#         self.W2 = \
#         np.random.randn(self.hiddenLayerSize, self.outputLayerSize)
    
#     def feedForward(self, X):
#         # feedForward propagation through our network
#         # dot product of X (input) and first set of 3x4 weights
#         self.z = np.dot(X, self.W1)
#         # the activationSigmoid activation function - neural magic
#         self.z2 = self.activationSigmoid(self.z)
#         # dot product of hidden layer (z2) and second set of 4x1 weights
#         self.z3 = np.dot(self.z2, self.W2)
#         # final activation function - more neural magic
#         o = self.activationSigmoid(self.z3)
#         return o

#     def backwardPropagate(self, X, y, o):
#         # backward propagate through the network
#         # calculate the error in output
#         self.o_error = y - o
#         # apply derivative of activationSigmoid to error
#         self.o_delta = self.o_error*self.activationSigmoidPrime(o)
#         # z2 error: how much our hidden layer weights contributed to output
#         # error
#         self.z2_error = self.o_delta.dot(self.W2.T)
#         # applying derivative of activationSigmoid to z2 error
#         self.z2_delta = self.z2_error*self.activationSigmoidPrime(self.z2)
#         # adjusting first set (inputLayer --> hiddenLayer) weights
#         self.W1 += X.T.dot(self.z2_delta)
#         # adjusting second set (hiddenLayer --> outputLayer) weights
#         self.W2 += self.z2.T.dot(self.o_delta)

#     def trainNetwork(self, X, y):
#         # feed forward the loop
#         o = self.feedForward(X)
#         # and then backpropagate the values (feedback)
#         self.backwardPropagate(X, y, o)

#     def activationSigmoid(self, s):
#         # activation function
#         # simple activationSigmoid curve as in the AIO Python book
#         return 1/(1+np.exp(-s))

#     def activationSigmoidPrime(self, s):
#         # First derivative of activationSigmoid
#         # calculus time!
#         return s * (1 - s)

#     def saveSumSquaredLossList(self,i,error):
#         lossFile.write(str(i)+","+str(error.tolist())+'\n')
        
#     def saveWeights(self):
#         # save this in order to reproduce our cool network
#         np.savetxt("weightsLayer1.txt", self.W1, fmt="%s")
#         np.savetxt("weightsLayer2.txt", self.W2, fmt="%s")
        
#     def predictOutput(self):
#         print ("Predicted XOR output data based on trained weights: ")
#         print ("Expected (X1-X3): \n" + str(xPredicted))
#         print ("Output (Y1): \n" + str(self.feedForward(xPredicted)))
    
# myNeuralNetwork = Neural_Network()
# trainingEpochs = 1000
# #trainingEpochs = 100000

# for i in range(trainingEpochs): # train myNeuralNetwork 1,000 times
#     print ("Epoch # " + str(i) + "\n")
#     print ("Network Input : \n" + str(X))
#     print ("Expected Output of XOR Gate Neural Network: \n" + str(y))
#     print ("Actual Output from XOR Gate Neural Network: \n" + \
#     str(myNeuralNetwork.feedForward(X)))
#     # mean sum squared loss
#     Loss = np.mean(np.square(y - myNeuralNetwork.feedForward(X)))
#     myNeuralNetwork.saveSumSquaredLossList(i,Loss)
#     print ("Sum Squared Loss: \n" + str(Loss))
#     print ("\n")
#     myNeuralNetwork.trainNetwork(X, y)
# myNeuralNetwork.saveWeights()
# myNeuralNetwork.predictOutput()

########################################################################################################################

# import tensorflow as tf
# from tensorflow.keras import layers
# from tensorflow.keras.layers import Activation, Dense
# import numpy as np
# # X = input of our 3 input XOR gate
# # set up the inputs of the neural network (right from the table)
# X = np.array(([0,0,0],[0,0,1],[0,1,0],
#     [0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]), dtype=float)
# # y = our output of our neural network
# y = np.array(([1], [0], [0], [0], [0],
#     [0], [0], [1]), dtype=float)
# model = tf.keras.Sequential()
# model.add(Dense(4, input_dim=3, activation='relu',
#     use_bias=True))
# #model.add(Dense(4, activation='relu', use_bias=True))
# model.add(Dense(1, activation='sigmoid', use_bias=True))
# model.compile(loss='mean_squared_error',
#     optimizer='adam',
#     metrics=['binary_accuracy'])
# print (model.get_weights())
# history = model.fit(X, y, epochs=2000,
#  validation_data = (X, y))
# model.summary()
# # printing out to file
# loss_history = history.history["loss"]
# numpy_loss_history = np.array(loss_history)
# np.savetxt("loss_history.txt", numpy_loss_history,
#  delimiter="\n") 
# binary_accuracy_history = history.history["binary_accuracy"]
# numpy_binary_accuracy = np.array(binary_accuracy_history)
# np.savetxt("binary_accuracy.txt", numpy_binary_accuracy, delimiter="\n")
# print(np.mean(history.history["binary_accuracy"]))
# result = model.predict(X ).round()
# print (result)

########################################################################################################################

# The three main types of machine-learning algorithms follow:

# » Supervised learning: This type of algorithm builds a model of data that
# contains both inputs and outputs. The data is known as training data. We
# show this type of machine learning in this chapter.

# » Unsupervised learning: For this type of algorithm, the data contains only
# inputs, and the algorithms look for structures and patterns in the data. The
# algorithms generally have sophisticated statistical and mathematic goals, not
# simple goals such as finding a mountain taller than 1,000 meters.

# » Reinforcement learning: In this type of algorithm, software takes actions
# based on a cumulative reward. The algorithm does not assume knowledge of
# an exact mathematical model and is used when exact models are unavailable.
# Reinforcement learning is the most complex area of machine learning, and
# the one that might be most fruitful in the future. Experimenting with reinforcement 
# learning is the area of robotic vision interpretation research using
# machine learning that is of great interest to co-author John Shovic.

########################################################################################################################

# Fashion-MNIST uses a MNIST-format (a collection of grayscale images with a
# resolution of 28x28 pixels) fashion database of 60,000 images classified into ten
# types of apparel:
# » 0: t-shirt/top
# » 1: trouser
# » 2: pullover
# » 3: dress
# » 4: coat
# » 5: sandal
# » 6: shirt
# » 7: sneaker
# » 8: bag
# » 9: ankle boot

########################################################################################################################

# We use the same five-step approach we used to build layered networks with Keras
# in Chapter 2 of this minibook. TensorFlow and Keras.

# 1. Load and format your data.
# 2. Define your neural network model and layers.
# 3. Compile the model.
# 4. Fit and train your model.
# 5. Evaluate the model.

########################################################################################################################

# #import libraries
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# import seaborn as sns
# import tensorflow as tf
# from tensorflow.python.framework import ops
# from tensorflow.examples.tutorials.mnist import input_data
# from PIL import Image
# # Import Fashion MNIST
# fashion_mnist = input_data.read_data_sets('input/data', one_hot=True)
# fashion_mnist = tf.keras.datasets.fashion_mnist
# (train_images, train_labels), (test_images, test_labels) \
#  = fashion_mnist.load_data()
 
# class_names = ['T-shirt/top', 'Trouser',
#  'Pullover', 'Dress', 'Coat',
# 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# train_images = train_images / 255.0
# test_images = test_images / 255.0

# model = tf.keras.Sequential()

# model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
# model.add(tf.keras.layers.Dense(128, activation='relu' ))
# model.add(tf.keras.layers.Dense(10, activation='softmax' ))

# model.compile(optimizer=tf.train.AdamOptimizer(),
#                 loss='sparse_categorical_crossentropy',
#                 metrics=['accuracy'])
# model.fit(train_images, train_labels, epochs=5)
# # test with 10,000 images
# test_loss, test_acc = model.evaluate(test_images, test_labels)
# print('10,000 image Test accuracy:', test_acc)

########################################################################################################################

#run test image from Fashion_MNIST data
# img = test_images[15]
# img = (np.expand_dims(img,0))
# singlePrediction = model.predict(img,steps=1)
# print ("Prediction Output")
# print(singlePrediction)
# print()
# NumberElement = singlePrediction.argmax()
# Element = np.amax(singlePrediction)
# print ("Our Network has concluded that the image number '15' is a "
#  +class_names[NumberElement])
# print (str(int(Element*100)) + "% Confidence Level")

########################################################################################################################

# # read test dress image
# imageName = "Dress28x28.JPG"
# testImg = Image.open(imageName)
# testImg.load()
# data = np.asarray( testImg, dtype="float" )
# data = tf.image.rgb_to_grayscale(data)
# data = data/255.0
# data = tf.transpose(data, perm=[2,0,1])
# singlePrediction = model.predict(data,steps=1)
# print ("Prediction Output")
# print(singlePrediction)
# print()
# NumberElement = singlePrediction.argmax()
# Element = np.amax(singlePrediction)
# print ("Our Network has concluded that the file '"
#  +imageName+"' is a "+class_names[NumberElement])
# print (str(int(Element*100)) + "% Confidence Level")

########################################################################################################################

# #import libraries
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# import seaborn as sns
# import tensorflow as tf
# from tensorflow.python.framework import ops
# from tensorflow.examples.tutorials.mnist import input_data
# from PIL import Image
# # Import Fashion MNIST
# fashion_mnist = input_data.read_data_sets('input/data',
#  one_hot=True)
# fashion_mnist = tf.keras.datasets.fashion_mnist
# (train_images, train_labels), (test_images, test_labels) \
#  = fashion_mnist.load_data()
# class_names = ['T-shirt/top', 'Trouser',
#  'Pullover', 'Dress', 'Coat',
#  'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
# train_images = train_images / 255.0
# test_images = test_images / 255.0
# # Prepare the training images
# train_images = train_images.reshape(train_images.shape[0], 28, 28, 1)
# # Prepare the test images
# test_images = test_images.reshape(test_images.shape[0], 28, 28, 1)
# model = tf.keras.Sequential()
# input_shape = (28, 28, 1)
# model.add(tf.keras.layers.Conv2D(32, kernel_size=(3, 3), activation='relu',
# input_shape=input_shape))
# model.add(tf.keras.layers.BatchNormalization())
# model.add(tf.keras.layers.Conv2D(32, kernel_size=(3, 3), activation='relu'))
# model.add(tf.keras.layers.BatchNormalization())
# model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))
# model.add(tf.keras.layers.Dropout(0.25))
# model.add(tf.keras.layers.Conv2D(64, kernel_size=(3, 3), activation='relu'))
# model.add(tf.keras.layers.BatchNormalization())
# model.add(tf.keras.layers.Dropout(0.25))
# model.add(tf.keras.layers.Conv2D(128, kernel_size=(3, 3), activation='relu'))
# model.add(tf.keras.layers.BatchNormalization())
# model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))
# model.add(tf.keras.layers.Dropout(0.25))
# model.add(tf.keras.layers.Flatten())
# model.add(tf.keras.layers.Dense(512, activation='relu'))
# model.add(tf.keras.layers.BatchNormalization())
# model.add(tf.keras.layers.Dropout(0.5))
# model.add(tf.keras.layers.Dense(128, activation='relu'))
# model.add(tf.keras.layers.BatchNormalization())
# model.add(tf.keras.layers.Dropout(0.5))
# model.add(tf.keras.layers.Dense(10, activation='softmax'))
# model.compile(optimizer=tf.train.AdamOptimizer(),
#  loss='sparse_categorical_crossentropy',
#  metrics=['accuracy'])
# model.fit(train_images, train_labels, epochs=5)
# # test with 10,000 images
# test_loss, test_acc = model.evaluate(test_images, test_labels)
# print('10,000 image Test accuracy:', test_acc)
# #run test image from Fashion_MNIST data
# img = test_images[15]
# img = (np.expand_dims(img,0))
# singlePrediction = model.predict(img,steps=1)
# print ("Prediction Output")
# print(singlePrediction)
# print()
# NumberElement = singlePrediction.argmax()
# Element = np.amax(singlePrediction)
# print ("Our Network has concluded that the image number '15' is a "
#  +class_names[NumberElement])
# print (str(int(Element*100)) + "% Confidence Level")

########################################################################################################################

# #import libraries
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# import seaborn as sns
# import tensorflow as tf
# from tensorflow.python.framework import ops
# from tensorflow.examples.tutorials.mnist import input_data
# from PIL import Image
# # Import Fashion MNIST
# fashion_mnist = input_data.read_data_sets('input/data', one_hot=True)
# fashion_mnist = tf.keras.datasets.fashion_mnist
# (train_images, train_labels), (test_images, test_labels) = \
# fashion_mnist.load_data()
# class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
#  'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
# train_images = train_images / 255.0
# test_images = test_images / 255.0
# model = tf.keras.Sequential()
# model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
# model.add(tf.keras.layers.Dense(128, activation='relu' ))
# model.add(tf.keras.layers.Dense(10, activation='softmax' ))
# model.compile(optimizer=tf.train.AdamOptimizer(),
#   loss='sparse_categorical_crossentropy',
#   metrics=['accuracy'])
# history = model.fit(train_images, train_labels, epochs=2)
# # Get training and test loss histories
# training_loss = history.history['loss']
# accuracy = history.history['acc']
# # Create count of the number of epochs
# epoch_count = range(1, len(training_loss) + 1)
# # Visualize loss history
# plt.figure(0)
# plt.plot(epoch_count, training_loss, 'r--')
# plt.plot(epoch_count, accuracy, 'b--')
# plt.legend(['Training Loss', 'Accuracy'])
# plt.xlabel('Epoch')
# plt.ylabel('History')
# plt.show(block=False);
# plt.pause(0.001)
# test_loss, test_acc = model.evaluate(test_images, test_labels)
# #run test image from Fashion_MNIST data
# img = test_images[15]
# plt.figure(1)
# plt.imshow(img)
# plt.show(block=False)
# plt.pause(0.001)
# img = (np.expand_dims(img,0))
# singlePrediction = model.predict(img,steps=1)
# print ("Prediction Output")
# print(singlePrediction)
# print()
# NumberElement = singlePrediction.argmax()
# Element = np.amax(singlePrediction)
# print ("Our Network has concluded that the image number '15' is a "
#   +class_names[NumberElement])
# print (str(int(Element*100)) + "% Confidence Level")
# print('Test accuracy:', test_acc)
# # read test dress image
# imageName = "Dress28x28.JPG"
# testImg = Image.open(imageName)
# plt.figure(2)
# plt.imshow(testImg)
# plt.show(block=False)
# plt.pause(0.001)
# testImg.load()
# data = np.asarray( testImg, dtype="float" )
# data = tf.image.rgb_to_grayscale(data)
# data = data/255.0
# data = tf.transpose(data, perm=[2,0,1])
# singlePrediction = model.predict(data,steps=1)
# NumberElement = singlePrediction.argmax()
# Element = np.amax(singlePrediction)
# print(NumberElement)
# print(Element)
# print(singlePrediction)
# print ("Our Network has concluded that the file '"+imageName+"' is a "
#   +class_names[NumberElement])
# print (str(int(Element*100)) + "% Confidence Level")
# plt.show()

########################################################################################################################

# We recommend you check out Machine Learning For Dummies by John Paul Mueller and Luca Massaron
# and Deep Learning with Python by François Chollet (Manning Publications). And for
# a great beginner’s overview of the AI field, read Artificial Intelligence For Dummies
# by John Paul Mueller and Luca Massaron.

########################################################################################################################
# 4 Exploring AI
########################################################################################################################

# If you’re interested in furthering your knowledge and abilities in machine learning and AI, check out the following sources for project inspiration:
# » “Is Santa Claus Real?,” Varun Vohra, https://towardsdatascience.com/is-santa-claus-real-9b7b9839776c
# » “Keras and deep learning on the Raspberry Pi,” Adrian Rosebrock, www.pyimagesearch.com/2017/12/18/keras-deep-learning-raspberry-pi/
# » “MouseAir – Using AI on the Raspberry Pi to Entertain your Cat,” John Shovic,www.switchdoc.com/2019/11/mouseair-raspberry-pi-cat-toy/
# » “How to easily Detect Objects with Deep Learning on Raspberry Pi,” Sarthak Jain, https://medium.com/nanonets/how-to-easily-detect-objectswith-deep-learning-on-raspberrypi-225f29635c74
# » “Building a Cat Detector using Convolutional Neural Network,” Venelin Valkov, https://medium.com/@curiousily/tensorflow-for-hackers-part-iiiconvolutional-neural-networks-c077618e590b
# » “Real time Image Classifier on Raspberry Pi Using Inception Framework,” Bapi Reddy, https://medium.com/@bapireddy/real-time-image-classifieron-raspberry-pi-using-inception-framework-faccfa150909
# In the Dummies tradition, you’ll accelerate your learning in these important technologies by not only reading but also building programs and modifying other people’s programs.

########################################################################################################################
# 5 Doing Data Science
########################################################################################################################

# » Python Numpy — Introduction to ndarray [Part 1] (www.machinelearning
# plus.com/python/numpy-tutorial-part1-array-python-examples/):
# A good introduction to matrices (also known as tensors) and how they fit
# into NumPy

# » NumPy Tutorial (www.tutorialspoint.com/numpy): A nice overview of
# NumPy, including where it comes from and how to use it

# » NumPy Tutorial: Learn with Example (www.guru99.com/numpy-tutorial.
# html): Less theory, but a bunch of great examples to fill in the practical gaps
# after looking at the first two tutorials

########################################################################################################################

# import numpy as np
# x = np.array([[1,2],[3,4]])
# print(np.sum(x)) # Compute sum of all elements; prints "10"
# print(np.sum(x, axis=0)) # Compute sum of each column; prints "[4 6]"
# print(np.sum(x, axis=1)) # Compute sum of each row; prints "[3 7]"

########################################################################################################################

# Columns in the Diamond Database
# Column Header       Type of Data        Description
# Index               counter             Numeric Specific index of record
# carat               Numeric             Carat weight of the diamond
# cut                 Text                Cut quality of the diamond, 
#                                         in increasing order of fair, good, very good, premium, and ideal
# color               Text                Color of the diamond, with D the best and J the worst
# clarity             Text                How obvious inclusions are in the diamond, from best to worst, 
#                                         with FL equal to flawless and I3 equal to level 3 inclusions: 
#                                         FL, IF, VVS1, VVS2, VS1, VS2, SI1, SI2, I1, I2, I3
# depth               Numeric             Percentage depth: The height of a diamond, measured from the culet 
#                                         (the bottom tip of the cut diamond) to the table (the flat facet on top of the cut diamond), 
#                                         divided by its average girdle diameter
# table               Numeric             Percentage table: The width of the diamond’s table expressed as a percentage of its average diameter
# price               Numeric             Price of the diamond
# x                   Numeric             Length in mm
# y                   Numeric             Width in mm
# x                   Numeric             Depth in mm

########################################################################################################################

# # Diamonds are a Data Scientist's Best Friend
# #import the pandas and numpy libraries
# import numpy as np
# import pandas as pd
# # read the diamonds CSV file
# # build a DataFrame from the data
# df = pd.read_csv('diamonds.csv')
# print (df.head(10))
# print()
# # calculate the total value of the diamonds
# sum = df.price.sum()
# print ("Total $ Value of Diamonds: ${:0,.2f}".format( sum))
# # calculate the mean price of the diamonds
# mean = df.price.mean()
# print ("Mean $ Value of Diamonds: ${:0,.2f}".format(mean))
# # summarize the data
# descrip = df.carat.describe()
# print()
# print (descrip)
# descrip = df.describe(include='object')
# print()
# print (descrip)

########################################################################################################################

# # Looking at the Shiny Diamonds
# #import the pandas and numpy libraries
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# # read the diamonds CSV file
# # build a DataFrame from the data
# df = pd.read_csv('diamonds.csv')
# carat = df.carat
# clarity = df.clarity
# plt.scatter(clarity, carat)
# plt.show() # or plt.savefig("name.png")
# for i in range(20): 
#     print(df.iloc[i].clarity)

########################################################################################################################

# # Looking at the Shiny Diamonds
# #import the pandas and numpy libraries
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# # read the diamonds CSV file
# # build a DataFrame from the data
# df = pd.read_csv('diamonds.csv')
# import matplotlib.pyplot as plt
# # count the number of each textual type of clarity
# clarityindexes = df['clarity'].value_counts().index.tolist()
# claritycount= df['clarity'].value_counts().values.tolist()
# print(clarityindexes)
# print(claritycount)
# plt.bar(clarityindexes, claritycount)
# plt.show() # or plt.savefig("name.png")

########################################################################################################################

# # Looking at the Shiny Diamonds
# #import the pandas and numpy libraries
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# # read the diamonds CSV file
# # build a DataFrame from the data
# df = pd.read_csv('diamonds.csv')
# import matplotlib.pyplot as plt
# # count the number of each textual type of color
# colorindexes = df['color'].value_counts().index.tolist()
# colorcount= df['color'].value_counts().values.tolist()
# print(colorindexes)
# print(colorcount)
# plt.bar(colorindexes, colorcount)
# plt.show() # or plt.savefig("name.png")

########################################################################################################################

# # Looking at the Shiny Diamonds
# #import the pandas and numpy libraries
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# # read the diamonds CSV file
# # build a DataFrame from the data
# df = pd.read_csv('diamonds.csv')
# # drop the index column
# df = df.drop('Unnamed: 0', axis=1)
# f, ax = plt.subplots(figsize=(10, 8))
# corr = df.corr(numeric_only=True)
# print (corr)
# sns.heatmap(corr, mask=np.zeros_like(corr, dtype=bool),
#     cmap=sns.diverging_palette(220, 10, as_cmap=True),
#     square=True, ax=ax)
# plt.show()

########################################################################################################################

# Column                                  Type        Description
# provider_id                             STRING      The CMS certification number (CCN) of the provider billing for outpatient hospital services.
# provider_name                           STRING      The name of the provider.
# provider_street_address                 STRING      The street address in which the provider is physically located.
# provider_city                           STRING      The city in which the provider is physically located.
# provider_state                          STRING      The state in which the provider is physically located.
# provider_zipcode                        INTEGER     The zip code in which the provider is physically located.
# drg_definition                          STRING      The code and description identifying the MS-DRG. MS-DRGs are a classification system 
#                                                     that groups similar clinical conditions (diagnoses) and the procedures furnished by the hospital during the stay.
# hospital_referral_region_description    STRING      The hospital referral region (HRR) in which the provider is physically located.
# total_discharges                        INTEGER     The number of discharges billed by the provider for inpatient hospital services.
# average_covered_charges                 FLOAT       The provider’s average charge for services covered by Medicare for all discharges in the MS-DRG. These vary from hospital 
#                                                     to hospital because of differences in hospital charge structures.
# average_total_payments                  FLOAT       The average total payments to all providers for the MS-DRG, including the MS-DRG amount, teaching, disproportionate share, 
#                                                     capital, and outlier payments for all cases. Also included in average total payments are co-payment and deductible amounts 
#                                                     that the patient is responsible for and any additional third-party payments for coordination of benefits.
# average_medicare_payments               FLOAT       The average amount that Medicare pays to the provider for its share of the MS-DRG. Average Medicare payment amounts include 
#                                                     the MS-DRG amount, teaching, disproportionate share, capital, and outlier payments for all cases. Medicare payments do not 
#                                                     include beneficiary co-payments and deductible amounts nor any additional payments from third parties for coordination of benefits.

########################################################################################################################

# LEARNING SQL
# SQL (Structured Query Language) is a query-oriented language used to interface with
# databases and to extract information from those databases. Although it was designed
# for relational database access and management, it has been extended to many other
# types of databases, including data accessed by BigQuery and Google Cloud.
# Here are some excellent tutorials to get your head around how to access data using SQL:
    
# • www.w3schools.com/sql
# • www.sql-tutorial.net
# • SQL For Dummies, 9th Edition, Allen G. Taylor
# • SQL All-in-One For Dummies, 3rd Edition, Allen G. Taylor
# • SQL in 10 Minutes, 4th Edition (Sams Publishing), Ben Forta

########################################################################################################################

# import pandas as pd
# from google.cloud import bigquery
# # set up the query
# QUERY = """
#  SELECT provider_city, provider_state, drg_definition,
#  average_total_payments, average_medicare_payments
#  FROM `bigquery-public-data.cms:medicare.inpatient_charges_2015`
#  WHERE provider_city = "GREAT FALLS" AND provider_state = "MT"
#  ORDER BY provider_city ASC
#  LIMIT 1000
#  """
# client = bigquery.Client.from_service_account_json(
#  'MedicareProject2-122xxxxxf413.json')
# query_job = client.query(QUERY)
# df = query_job.to_dataframe()
# print ("Records Returned: ", df.shape )
# print ()
# print ("First 3 Records")
# print (df.head(3)) 

# Bu dosyayı oluşturur oluşturmaz MedicareProject2-122xxxxf413'ü değiştirin. 
# json dosyasını kendi kimlik doğrulama dosyanızla (daha önce program dizinine kopyaladığınız) oluşturun. 
# MedicareQuery1.py programını çalıştırdığınızda, google.cloud kitaplığı kurulu değilse bir içe aktarma hatası alırsınız. 
# Böyle bir durumda, bilgisayarınızdaki Terminal penceresine aşağıdakini yazın: pip install --upgrade google-cloud-bigquery 

# SQL sorgusunun yapısını görüyor musunuz? 
# Bigquery-public-data.cms:medicare.inpatient_charges_2015 veritabanından istediğimiz sütunları (Tablo 3-1'de listelendiği gibi) 
# yalnızca sağlayıcı_şehrinin GREAT FALLS ve sağlayıcı_durumunun MT olduğu NEREDE SEÇİYORUZ. Son olarak, 
# sisteme sonuçları sağlayıcı_şehire göre artan, alfasayısal sıraya göre sıralamasını söylüyoruz.

# ICD10, faturalama ve analiz için tıp profesyoneli teşhislerini kodlamak için köklü bir yöntemdir. 
# ICD-10'un en son versiyonu 2015 yılında zorunlu hale getirildi ve bu da tıp camiasında büyük bir endişeye neden oldu. 
# M79.603 — Pain in Arm, unspecified'den S92.4 — Fracture of Greater Toe'a kadar 155.000'den fazla koddan oluşur. 
# Bu kodlar, burada incelediğimiz Medicare veritabanlarında kullanılan MS_DRG kodlarıyla birleştirilir. 
# John Shovic bir tıbbi yazılım şirketi kurduğunda, bir aşk geliştirdi

# ICD10 is the well-established method for coding medical professional diagnoses for billing and analysis. 
# The latest version of ICD-10 was made mandatory in 2015, resulting in 
# great angst throughout the medical community. It consists of over 155,000 codes, from 
# M79.603 — Pain in Arm, unspecified to S92.4 — Fracture of Greater Toe. These codes 
# are merged into the MS_DRG codes used in the Medicare databases we examine here. 
# When John Shovic had a medical software startup, he developed a love/hate relationship with ICD 10 codes. His favorite codes follow:
#    • V97.33XD: Sucked into jet engine, subsequent encounter.
#    • Z63.1: Problems in relationship with in-laws.
#    • V95.43XS: Spacecraft collision injuring occupant, sequela.
#    • R46.1: Bizarre personal appearance.
#    • Y93.D1 Activity, knitting and crocheting.

########################################################################################################################

# import pandas as pd
# from google.cloud import bigquery
# # set up the query
# QUERY = """
#         SELECT provider_city, provider_state, drg_definition,
#         average_total_payments, average_medicare_payments
#         FROM `bigquery-public-data.cms:medicare.inpatient_charges_2015`
#         WHERE drg_definition LIKE '554 %'
#         ORDER BY provider_city ASC
#         LIMIT 1000
#         """
# client = bigquery.Client.from_service_account_json(
#     'MedicareProject2-1223283ef413.json')
# query_job = client.query(QUERY)
# df = query_job.to_dataframe()
# print ("Records Returned: ", df.shape )
# print ()
# # find the unique state values
# states = df.provider_state.unique()
# states.sort()
# total_payment = df.average_total_payments.sum()
# medicare_payment = df.average_medicare_payments.sum()
# percent_paid = ((medicare_payment/total_payment))*100
# print("Overall:")
# print ("Medicare pays {:4.2f}% of Total for 554 DRG".format(percent_paid))
# print ("Patient pays {:4.2f}% of Total for 554 DRG".format(100-percent_paid))
# print ("Per State:")
# # now iterate over states
# print(df.head(5))
# state_percent = []
# for current_state in states:
#     state_df = df[df.provider_state == current_state]
#     state_total_payment = state_df.average_total_payments.sum()
#     state_medicare_payment = state_df.average_medicare_payments.sum()
#     state_percent_paid = ((state_medicare_payment/state_total_payment))*100
#     state_percent.append(state_percent_paid)
#     print ("{:s} Medicare pays {:4.2f}% of Total for 554 DRG".format
#     (current_state,state_percent_paid))

########################################################################################################################

# # We could graph this using MatPlotLib with the two lists,
# # but we want to use DataFrames for this example
# data_array = {'State': states, 'Percent': state_percent}
# df_states = pd.DataFrame.from_dict(data_array)
# # Now back in dataframe land
# import matplotlib.pyplot as plt
# import seaborn as sb
# print (df_states)
# df_states.plot(kind='bar', x='State', y= 'Percent')
# plt.show()

########################################################################################################################

# import pandas as pd
# from google.cloud import bigquery
# # sample query from:
# QUERY = """
#         SELECT location, city, country, value, timestamp
#         FROM `bigquery-public-data.openaq.global_air_quality`
#         WHERE pollutant = "pm10" AND timestamp > "2017-04-01"
#         ORDER BY value DESC
#         LIMIT 1000
#         """
# client = bigquery.Client.from_service_account_json(
#     'MedicareProject2-1223283ef413.json')
# query_job = client.query(QUERY)
# df = query_job.to_dataframe()
# print (df.head(3))

########################################################################################################################
# 6 Talking to Hardware 
########################################################################################################################

# from gpiozero import LED
# from time import sleep
# blue = LED(12)
# while True:
#  blue.on()
#  print( "LED On")
#  sleep(1)
#  blue.off()
#  print( "LED Off")
#  sleep(1)

########################################################################################################################

# from gpiozero import PWMLED
# from time import sleep
# led = PWMLED(12)
# while True:
#  led.value = 0 # off
#  sleep(1)
#  led.value = 0.5 # half brightness
#  sleep(1)
#  led.value = 1 # full brightness
#  sleep(1)

########################################################################################################################



########################################################################################################################



########################################################################################################################



########################################################################################################################



########################################################################################################################



########################################################################################################################



########################################################################################################################

# 495 


