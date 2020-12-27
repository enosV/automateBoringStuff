def div42by(divideby):
    try:
        return 42 / divideby
    except ZeroDivisionError:
        print('Error: cant divide by zero')

print(div42by(2))
print(div42by(12))
print(div42by(0)) #this will ZeroDivisionError as it can't divide by 0 so div42by(1) never gets called (unless we use th try and except inside the def block)
print(div42by(1))
