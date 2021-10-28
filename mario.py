# Implement a program that prints out a double half-pyramid of a specified height

while True: # If a numerical value isn't entered, the program will run again until a numerical value set within the condition is passed
    try:
        height = int(input("Height: "))
        if height > 0 and height < 9:
            break
    except ValueError:
        print("Enter a numerical value between 1 and 8")

count = 0
for i in range(height): # 'i' checks the so-called "length" of 'height', and will keep looping until 'i' is greater than 'height'
    if count != height:
        var = (height - 1) - count
        jump = count + 1
        for s in range(var, 0, -1):
            print(" ", end="")
        print("#" * jump, end="")
        print("  ", end="")
        print('#' * jump, end="")
        count += 1
        print()