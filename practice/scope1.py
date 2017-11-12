message = "hello"

def say():
    print("say:message" + message)
    obj_id = id(message)
    print("sayid:(message)={0:d}".format(obj_id))

def main():
    say()
    print("main:message=" + message)
    obj_id = id(message)
    print("say:id(message)={0:d}".format(obj_id))

if __name__=='__main__':
    main()
