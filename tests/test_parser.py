from decimal import Decimal

import pytest

from decimify import parser


class TestParse:
    @pytest.mark.parametrize(
        ("num", "expected"),
        [
            ("-12", Decimal("-12")),
            ("0", Decimal("0")),
            ("12", Decimal("12")),
            ("12123123213", Decimal("12123123213")),
            ("-12123123213", Decimal("-12123123213")),
        ],
    )
    def test_parse_int_string_should_be_ok(self, num: str, expected: Decimal):
        assert parser.parse(num) == expected

    @pytest.mark.parametrize(
        ("num", "expected"),
        [
            ("-12.2", Decimal("-12.2")),
            ("0.0", Decimal("0.0")),
            ("12.2", Decimal("12.2")),
            ("12123.123213", Decimal("12123.123213")),
            ("-12123.123213", Decimal("-12123.123213")),
        ],
    )
    def test_parse_float_string_should_be_ok(self, num: str, expected: Decimal):
        assert parser.parse(num) == expected

    @pytest.mark.parametrize(
        ("num", "expected"),
        [
            ("-12,2", Decimal("-12.2")),
            ("0,0", Decimal("0.0")),
            ("12,2", Decimal("12.2")),
            ("12123,123213", Decimal("12123.123213")),
            ("-12123,123213", Decimal("-12123.123213")),
        ],
    )
    def test_parse_float_string_with_comma_separators(
        self, num: str, expected: Decimal
    ):
        assert parser.parse(num) == expected

    @pytest.mark.parametrize(
        ("num", "expected"),
        [
            ("12,123.123213", Decimal("12123.123213")),
            ("-12,123.123213", Decimal("-12123.123213")),
            ("12.123,123213", Decimal("12123.123213")),
            ("-12.123,123213", Decimal("-12123.123213")),
        ],
    )
    def test_parse_float_string_with_dot_and_comma_separators(
        self, num: str, expected: Decimal
    ):
        assert parser.parse(num) == expected
