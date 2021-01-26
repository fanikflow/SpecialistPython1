# Кассовый аппарат был доработан, теперь он пишет не только цены, но и тип проданных товаров.
# Файл data/items_sold.txt - продажи всех товаров за день.
# Каждая строка файла - покупка одного покупателя.
# Узнайте:
# 1. Какова общая выручка магазина
# 2. Какова выручка магазина по каждому типу товаров
# 3. Какой тип товара был продан на самую большую сумму
# 4. Сколько различных типов товаров было продано за день

f = open('Module6/Practice/items_sold.txt', 'r', encoding="utf-8")

items = [] #список содержимого строк
for line in f:
    items += line.split()
#print(items)

products = {} #словарь содержимого файла
revenue = 0 #выручка
count_products = 0 #счетчик наименований товара
max_revenue = 0 #максимальная выручка по категориям товаров


for el in items:
    el = el.split(":")
    key = el[0]
    value = float(el[1])
    if products.get(key) is None:
        products[key] = value
    else:
        products[key] += value

list_keys = list(products.keys())
first_key = list_keys[0]

max_revenue = products[first_key]

print("Выручка магазина по каждому типу товаров:")
for key,value in products.items():
    print(key,value)
    revenue += value
    count_products += 1
    if max_revenue < value:
        max_revenue = value
        max_r_item = key
    
print("Общая выручка магазина: ", revenue)
print("Количество различных типов товаров было продано за день: ", count_products)
print("Тип товара был продан на самую большую сумму: ", max_r_item)
