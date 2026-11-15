# Bean & Brew - week 5, Module 3: Cleaning the order data
# Task 1.1 Convert between types
print("Order data script ready")

qty_text = '12'
print(int(qty_text) + 3)
print(float(qty_text))
print(str(15) + ' cups')

print(int(7.9)) # rounded down to 7
print(type(12/3),12/3) 
print(type(12//3),12//3)

print("=" * 55)

print("# Task 1.2 Slice an order ")

order_code = 'BB-BOS-0042'
print(order_code[0:2])
print(order_code[3:6])
print(order_code[-4:])
print(len(order_code))
print(int(order_code[-4:]))
print(int(order_code[-2:]))


print("=" * 55)

# Task 1.3 Split a messy line(.strip, .split)
# I need the name,category, and price separately

raw_line = ' Caramel Latte,Coffee,4.95 '
clean_line = raw_line.strip()
fields = clean_line.split(',')
print(clean_line)
print(fields)
print(fields[0])
print(float(fields[2])* 2)

print("=" * 55)
# Task 1.4 Clean price and names (.replace, .lower, .upper, .title)
price_text = '$1,250.00'
answer = 'YES'
name = ' maria LOPEZ '

    
price = price_text.replace('$', '').replace(',','')
float_price = float(price)
print(float_price)
print(answer.lower())

clean_name = name.strip().title()
print(clean_name)

print("=" * 55)

# Task 1.5 . Predit, then run: ask the barista(input)
Lattes = int(input('How many lattes?'))
print(f'Total: ${Lattes * 4.95:.2f}')

print("=" * 55)

# Collection Data Types
# Task 2.1 Today's drinks in a list
drinks = ['Latte', 'Cold Brew', 'Chai']
drinks.append('Espresso')
drinks.insert(1, 'Mocha')
drinks.remove('Chai')
print(drinks)
print(len(drinks),drinks[0], drinks[-1])
drinks.sort()

print(drinks)
print('Mocha' in drinks)

sales = [13.40, 4.50, 8.25]
print(sum(sales), max(sales), min(sales))


print("=" * 55)

# Task 2.2 Predict, then run: a fixed record (tuple, unpacking)

record = ('BB-BOS-0042', 'Maria', 13.40)
code, customer, amount = record
print(customer, amount)
_, _, amount = record
print(amount)

#record[2] = 15.00

# Task 2.3: Unique customers(set)
visits = ['Maria', 'James', 'Maria', 'James', 'Aisha' ,'Maria']
regulars = set(visits)
print(len(visits), len(regulars))
print('Aisha' in regulars)
print('Tom' not in regulars)
regulars.add('Tom')
print(sorted(regulars))

print("=" * 55)

# Task 2.4 Predict, then run: the menu as a dictionary
menu = {'latte': 4.95,'cold brew': 4.50, 'chai': 4.75 }
print(menu['latte'])
print(menu.get('mocha'))
print(menu.get('mocha', 'not on the menu'))

menu['mocha'] = 5.25
menu.update({'latte': 5.10})
menu.pop('chai')
print(menu)
print(menu.keys())


