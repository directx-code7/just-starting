# Logistics
bus, truck, train = 0, 0, 0
n = int(input())
for m in range(0, n):
    weight_tons = int(input())
    if 1 <= weight_tons <= 3:
        bus += weight_tons
    elif 4 <= weight_tons <= 11:
        truck += weight_tons
    else:
        train += weight_tons
sum_bus = bus * 200
sum_truck = truck * 175
sum_train = train * 120
print(f'{((sum_bus + sum_truck + sum_train)/(bus + truck + train)):.2f}')
print(f'{(bus/(bus + truck + train)*100):.2f}%')
print(f'{(truck/(bus + truck + train)*100):.2f}%')
print(f'{(train/(bus + truck + train)*100):.2f}%')
