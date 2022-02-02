print("RunningTally(tm")
print("Enter a number to start the tally, enter 'quit' to stop")
run = True
total = 0

while run:
    try:
        inp = input()
        if (inp == "quit"):
            run = False
        else:
            val = int(inp)
            total += val
            print(f"Result: {total}")
    except ValueError:
        print("An error was found. Please type a number or enter 'quit' to stop")
        pass