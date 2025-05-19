from src.source import Source


def test_source() -> None:
    source = Source()

    actual = source.foox
    expected = "bar"
    assert expected == actual
