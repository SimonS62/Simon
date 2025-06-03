import pytest
from src.decorators import log


def test_log_console_success(capsys):
    @log()
    def add(a, b):
        return a + b

    result = add(2, 3)
    captured = capsys.readouterr()

    assert result == 5
    assert "Начало выполнения функции 'add'" in captured.out
    assert "Функция 'add' успешно завершена. Результат: 5" in captured.out


def test_log_console_exception(capsys):
    @log()
    def div(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        div(1, 0)

    captured = capsys.readouterr()
    assert "Начало выполнения функции 'div'" in captured.out
    assert "Функция 'div' вызвала ошибку ZeroDivisionError." in captured.out
    assert "Аргументы: 1, 0." in captured.out or "Аргументы: 1, b=0." in captured.out


def test_log_file_success(tmp_path):
    log_file = tmp_path / "test.log"

    @log(filename=str(log_file))
    def multiply(a, b):
        return a * b

    result = multiply(4, 5)
    assert result == 20

    content = log_file.read_text(encoding='utf-8')
    assert "Начало выполнения функции 'multiply'" in content
    assert "Функция 'multiply' успешно завершена. Результат: 20" in content


def test_log_file_exception(tmp_path):
    log_file = tmp_path / "test.log"

    @log(filename=str(log_file))
    def sub(a, b):
        if b > a:
            raise ValueError("b should not be greater than a")
        return a - b

    with pytest.raises(ValueError):
        sub(3, 5)

    content = log_file.read_text(encoding='utf-8')
    assert "Начало выполнения функции 'sub'" in content
    assert "Функция 'sub' вызвала ошибку ValueError." in content
    assert "Аргументы: 3, 5." in content or "Аргументы: 3, b=5." in content
