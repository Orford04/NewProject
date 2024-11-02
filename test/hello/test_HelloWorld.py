from src.hello.HelloWorld import HelloWorld


class TestHelloWorld():
  
    def test_hello_world(self, capsys):
        HelloWorld.main(["HelloWorld"])
        captured = capsys.readouterr()
        assert captured.out == "Hello World\n", "Unexpected Output"

    def test_hello_world_arg(self, capsys):
        HelloWorld.main(["HelloWorld", "CC 410"])
        captured = capsys.readouterr()
        assert captured.out == "Hello CC 410\n", "Unexpected Output"