class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("This class is singelton!")
        else:
            Singleton.__instance = self

if __name__ == "__main__":

    s = Singleton.getInstance()
    print(s)

    q = Singleton.getInstance()
    print(q)

    if id(s) == id(q):
        print("Singleton is working both variables contain the same instance")
    else:
        print("Singleton failed, variables contain different instances")
