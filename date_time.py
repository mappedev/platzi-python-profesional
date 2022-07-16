from datetime import datetime

# my_time = datetime.datetime.now()  # * Hora local
# # print(my_time)

# time = datetime.datetime.utcnow()  # * Hora universal
# # print(time)

# my_day = datetime.date.today()  # * Fecha actual
# print(my_day)
# print("Year:", my_day.year)
# print("Month:", my_day.month)
# print("Day:", my_day.day)

my_datetime = datetime.now()
print(my_datetime)

my_str = my_datetime.strftime("%d/%m/%Y")
print("Formato LATAM:", my_str)

my_str = my_datetime.strftime("%m/%d/%Y")
print("Formato USA:", my_str)

my_str = my_datetime.strftime("Estamos en el año %Y")
print("Formato Random:", my_str)
