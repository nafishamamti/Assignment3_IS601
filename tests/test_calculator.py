import sys
from io import StringIO
from app.calculator import calculator

def run_calculator_with_input(monkeypatch, inputs):
    input_iterator = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iterator))

    captured_output = StringIO()
    sys.stdout = captured_output
    calculator()
    sys.stdout = sys.__stdout__  # Reset stdout
    return captured_output.getvalue()


# Positive Tests
def test_addition(monkeypatch):
    """Test addition operation in REPL."""
    inputs = ["2 + 3", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 5.0" in output


def test_subtraction(monkeypatch):
    """Test subtraction operation in REPL."""
    inputs = ["5 - 2", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 3.0" in output


def test_multiplication(monkeypatch):
    """Test multiplication operation in REPL."""
    inputs = ["4 * 5", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 20.0" in output


def test_division(monkeypatch):
    """Test division operation in REPL."""
    inputs = ["10 / 2", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 5.0" in output


# Negative Tests
def test_invalid_operation(monkeypatch):
    """Test invalid operation in REPL."""
    inputs = ["5 % 3", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Invalid operator. Please use +, -, *, or /." in output


def test_invalid_input_format(monkeypatch):
    """Test invalid input format in REPL."""
    inputs = ["two add three", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Invalid input format. Please enter in the format: value1 operator value2" in output


def test_division_by_zero(monkeypatch):
    """Test division by zero in REPL."""
    inputs = ["5 / 0", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Cannot divide by zero." in output
