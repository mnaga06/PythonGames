message = "hello"

def say():
    print("say:message" + message)

def main():
    say()
    print("main:message=" + message)

if __name__=='__main__':
    main()
