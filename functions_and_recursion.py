import time

print("Lets go!")

testCounter = 0

def test_func_recurs():
    print("Now inside test_func_recurs")
    
    global testCounter
    testCounter = testCounter+1

    if testCounter < 2:
        test_func_recurs()

def test_func_return():
    print("Now inside test_func_return")
    return "abc123456789"

def main():
    ts = time.time()
    print("MAIN: "+str(ts))

    test = test_func_return()
    print(test)

    test_func_recurs()

main()
#if __name__ == "__main__":
 #   main()

