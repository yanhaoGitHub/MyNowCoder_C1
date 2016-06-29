#-*- encoding=UTF-8 -*-
def log(func):
    def wrapper():
        print "before calling", func.__name__
        func()
        print "end calling", func.__name__
    return wrapper

@log
def hello():
    print "enter&code&here"

if __name__ == "__main__":
    hello()
