class A:

    def say(self):
        return "Аааааа!"

class B:

    def say(self):
        return "Bebebebebeb"

class C:

    def say(self):
        return "Caution!"



if __name__ == '__main__':

    L = [A(), B(), B(),C() ,A() ,C() ,B()]

    for obj in L:
        print(obj.say())