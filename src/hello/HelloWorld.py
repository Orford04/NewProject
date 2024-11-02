class HelloWorld:
    @staticmethod
    def main(args):
        if len(args) == 2:
            print("Hello {}".format(args[1]))
        else:
            print("Hello World")