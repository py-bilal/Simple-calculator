import math

list = ['bola', 'jide', 'tolu', 'raji']
print(list)
for t  in list:
    print(t)
list.append('jut')
print(list)
list.pop()
print(list)
kod = 'ola'
print(kod * 5)
print(5**2)
print(5//2)
print(int(23.8))
print(float(56))
lur = 45 > 50
print(lur)
# kf = pi
# print(pi)
# hy = log10
# print(hy)
print('#'*10)

# while loop without break
t =  1
while t < 6:
    print(t)
    t += 1
  
# with break    
t =  1
while t < 6:
    print(t)
    if t == 3:
        break
    t += 1
    
# with continue    
t =  0
while t < 6:
    t += 1
    if t == 3:
        continue
    print(t)
    
# with else statement
t =  1
while t < 6:
    print(t)
    t += 1
else:
    print("t is not longer less than 6")  
    
    
# FOR LOOPS
utensils = ["spoon", "pots", "frying pan", "sieve"]
for s in utensils:
    print(s)

for d in "hippopotamus":
    print(d)
    
  # With the break statement 
foods = ["semo", "amala", "tuwo", "rice"]
for y in foods:
    print(y)
    if y == "tuwo":
        break  
    
             
  # With the break statement after the 'print'
foods = ["semo", "amala", "tuwo", "rice"]
for y in foods:
    if y == "tuwo":
        break           
    print(y)
    
  # With the continue statement
foods = ["semo", "amala", "tuwo", "rice"]
for d in foods:
    if d == "tuwo":
        continue
    print(d)

  # With the range function
for t in range(7):
    print(t)
      
  # With the range function of specific range
for t in range(2, 7):
    print(t) 
     
  # With the range function of specific range and increment value
for t in range(2, 30, 3):
    print(t)  
  
  # With the else statement 
foods = ["semo", "amala", "tuwo", "rice"]    
for g in foods:
    print(g)
else:
    print("Finally finished !")    
    
for e in range(5):
    if e == 4:break
    print(e)
else:
    print("Finally finished !") 
    
 # Nested LOOPS
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)   
        
  # With the pass statements
for x in [0, 1, 2]:
    pass    
    
            