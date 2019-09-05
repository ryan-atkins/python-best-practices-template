from best_practices_template import best_practices_template


def test_fib() -> None:
    assert best_practices_template.fib(0) == 0
    assert best_practices_template.fib(1) == 1
    assert best_practices_template.fib(2) == 1
    assert best_practices_template.fib(3) == 2
    assert best_practices_template.fib(4) == 3
    assert best_practices_template.fib(5) == 5
    assert best_practices_template.fib(10) == 55
