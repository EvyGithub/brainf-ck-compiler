import time

# ass key table

ascii = []
for asskeyNum in range(127):
    ascii.append(chr(asskeyNum))

# vars
memory = ([0] * 32)
acceptedChars = ['+', '-', '<', '>', '[', ']', '.', ',']
memoryPointer = 0


code = open('code.bf', 'r').readlines()[0]

print("code:\n")

# just to show what the code is
for char in code:
    print(char, end="")

# output
print("\n\nexecution:\n\n")


# compiler
for char in code:
    # print(char)
    
    if char == "+":
        memory[memoryPointer] += 1
        if memory[memoryPointer] > 255:
            memory[memoryPointer] = 0

    elif char == "-":
        memory[memoryPointer] -= 1
        if memory[memoryPointer] < 0:
            memory[memoryPointer] = 255
        
    elif char == ".":
        # print ascii letter of the value of current cell pointer is at
        try:
            charToPrint = ascii[memory[memoryPointer]]
        except IndexError:
            charToPrint = " "

        print(charToPrint, end="")

    elif char == ",":
        # input (hard, because you have to limit to one character and ascii is stupid)

        charInput = ""

        while len(charInput) != 1:
            charInput = input("input: ")

        asciiToReplace = ascii.index(charInput)

        memory[memoryPointer] = asciiToReplace

    elif char == ">":
        memoryPointer += 1
    elif char == "<":
        memoryPointer -= 1

    # the hard part: loops

    elif char == "[":
        pass # TODO
    
    elif char == "]":
        pass # TODO


    else:
        pass # if this runs, then you didn't enter proper brainf*ck code


    # print(memoryPointer)

    # time.sleep(1/128) # XD