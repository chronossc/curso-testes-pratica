from examples.identifier import Identifier
import pytest


@pytest.fixture(scope='module')
def identifier():
    return Identifier()


@pytest.mark.parametrize(
    's,expected', (
        # pytest.param('', False, id='\'\' is invalid'),
        pytest.param('a', True, id='a is valid'),
        pytest.param('ab', True, id='ab is valid'),
        pytest.param('abc', True, id='abc is valid'),
        pytest.param('abcd', True, id='abcd is valid'),
        pytest.param('abcde', True, id='abcde is valid'),
        pytest.param('abcdef', True, id='abcdef is valid'),
        pytest.param('abcdefg', False, id='abcdefg is invalid')
    )
)
def test_identifier_strings(s, expected, identifier):
    result = identifier.validate_identifier(s)
    assert result is expected


def test_zero_length_raises_value_error(identifier):
    with pytest.raises(ValueError, match="Invalid identifier"):
        identifier.validate_identifier('')


@pytest.mark.parametrize(
    's,expected', (
            ('1a', False),
            ('a1', True),
            ('açaí', False)
    )
)
def test_valid_invalid_chars(s, expected, identifier):
    result = identifier.validate_identifier(s)
    assert result is expected
