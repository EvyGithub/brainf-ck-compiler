# ass key table

ascii = []
for asskeyNum in range(127):
    ascii.append(chr(asskeyNum))

# vars
memory = ([0] * 32)
acceptedChars = ['+', '-', '<', '>', '[', ']', '.', ',']
memoryPointer = 0
loopPositions = []
loopAmount = 0
loopStack = []
codePointer = 0


code = open('code.bf', 'r').readlines()[0]

print("code:\n")

# just to show what the code is
for char in code:
    print(char, end="")

# output
print("\n\nexecution:\n\n")


# compiler
while codePointer < len(code):
    cmd = code[codePointer]
    
    if cmd == "+":
        memory[memoryPointer] += 1
        if memory[memoryPointer] > 255:
            memory[memoryPointer] = 0

    elif cmd == "-":
        memory[memoryPointer] -= 1
        if memory[memoryPointer] < 0:
            memory[memoryPointer] = 255
        
    elif cmd == ".":
        # print ascii letter of the value of current cell pointer is at
        try:
            charToPrint = ascii[memory[memoryPointer]]
        except IndexError:
            charToPrint = " "

        print(charToPrint, end="")

    elif cmd == ",":
        # input (hard, because you have to limit to one character and ascii is stupid)

        charInput = ""

        while len(charInput) != 1:
            charInput = input("input: ")

        asciiToReplace = ascii.index(charInput)

        memory[memoryPointer] = asciiToReplace

    elif cmd == ">":
        memoryPointer += 1
    elif cmd == "<":
        memoryPointer -= 1

    # the hard part: loops

    elif cmd == "[":
        if memory[memoryPointer] == 0:
            # skip loop
            loopAmount = 1
            while loopAmount > 0:
                codePointer += 1
                if code[codePointer] == '[':
                    loopAmount += 1
                elif code[codePointer] == ']':
                    loopAmount -= 1
        else:
            # enter loop
            loopStack.append(codePointer)
    
    elif cmd == "]":
        if memory[memoryPointer] != 0:
            # go back to to the '['
            codePointer = loopStack[-1]
        else:
            # exit
            loopStack.pop()


    else:
        pass # if this runs, then you didn't enter proper brainf*ck code


    codePointer += 1