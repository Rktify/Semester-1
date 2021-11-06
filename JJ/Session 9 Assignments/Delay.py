def delay(string,te):
    import time
    time.sleep(te)
    print(string)

msg = input("What message do you want to be printed?: ")
tm = int(input("How long do you want the delay to be?: "))

delay(msg,tm)