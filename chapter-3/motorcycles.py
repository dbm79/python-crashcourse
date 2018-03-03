motorcyles = ['honda', 'yamaha', 'suzuki', 'HD']
print(motorcyles)

motorcyles[0] = 'ducati'    #This will replace the first element
print(motorcyles)

motorcyles.append('triumph')    # This will add an element at end
print(motorcyles)

del motorcyles[0]   # This will del the entry at index 0
print(motorcyles)

popped_motorcyle = motorcyles.pop() # This will remove last item in motorcyles
print(motorcyles)
print(popped_motorcyle)

popped = motorcyles.pop(1)  # This will pop the 2nd element in list
print(popped)

motorcyles.remove('HD') # This will remove the item by value
print(motorcyles)
