from decimal import Decimal, InvalidOperation

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
        assert parser.decimify(num) == expected

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
        assert parser.decimify(num) == expected

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
        self,
        num: str,
        expected: Decimal,
    ):
        assert parser.decimify(num) == expected

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
        self,
        num: str,
        expected: Decimal,
    ):
        assert parser.decimify(num) == expected

    @pytest.mark.parametrize(
        ("num", "expected"),
        [
            ("12,123,123.213", Decimal("12123123.213")),
            ("-12,123,123.213", Decimal("-12123123.213")),
            ("12.123.123,213", Decimal("12123123.213")),
            ("-12.123.123,213", Decimal("-12123123.213")),
        ],
    )
    def test_parse_float_string_with_multiple_dot_and_comma_separators(
        self,
        num: str,
        expected: Decimal,
    ):
        assert parser.decimify(num) == expected

    @pytest.mark.parametrize(
        ("num", "expected"),
        [
            ("12 123 123.213", Decimal("12123123.213")),
            ("-12 123 123.213", Decimal("-12123123.213")),
            ("12 123 123,213", Decimal("12123123.213")),
            ("-12 123 123,213", Decimal("-12123123.213")),
            ("12 123,123.213", Decimal("12123123.213")),
            ("-12 123,123.213", Decimal("-12123123.213")),
            ("12 123.123,213", Decimal("12123123.213")),
            ("-12 123.123,213", Decimal("-12123123.213")),
        ],
    )
    def test_parse_float_string_with_spaces(self, num: str, expected: Decimal):
        assert parser.decimify(num) == expected

    @pytest.mark.parametrize(
        "num",
        [
            "12,123.123.213",
            "-12,123.123.213",
            "12.123.123.213",
            "-12.123.123.213",
            "12 123.123.213",
            "-12 123.123.213",
        ],
    )
    def test_parse_float_string_with_multiple_floating_point_separators_should_fail(
        self,
        num: str,
    ):
        with pytest.raises(
            InvalidOperation,
            match="Floating point separator:'.' exists multiple times.",
        ):
            parser.decimify(num)

    @pytest.mark.parametrize(
        ("num", "expected"),
        [
            ("4 294 967 295,000", Decimal("4294967295.00")),
            ("4 294 967.295,000", Decimal("4294967295.00")),
            ("4.294.967.295,000", Decimal("4294967295.00")),
            ("4,294,967,295.00", Decimal("4294967295.00")),
        ],
    )
    def test_country_specific_formats(self, num: str, expected: Decimal):
        assert parser.decimify(num) == expected
