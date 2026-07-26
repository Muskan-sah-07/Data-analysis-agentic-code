from src.main import main


def test_main_no_numbers(capsys):
    main([])
    captured = capsys.readouterr()
    assert "Hello from Data Analytics Agent" in captured.out


def test_main_with_numbers(capsys):
    main(["--numbers", "1", "2", "3"])
    captured = capsys.readouterr()
    assert "Mean of" in captured.out
