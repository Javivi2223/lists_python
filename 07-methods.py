# método append
list = []
list.append("Xiaomi")
list.append("Motorola")
print(list)

#método insert
list.insert(1, "Huawei")
print(list)

#método extend: agrega elementos de otro iterable (como otra lista) al final e la lista actual.
list_2 = ["Samsung", "Apple", "Toshiba"]
list.extend(list_2)

print(list)