import main


def test_func_main(mocker):
    mocker.patch("main.func_hoge", return_value=[1, 2])
    print(main.func_main())  # [1, 2]
    assert main.func_main() == [1, 2]
