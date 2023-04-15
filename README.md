# decimify

[![CI](https://github.com/zahidkizmaz/decimify/workflows/CI/badge.svg?event=push)](https://github.com/zahidkizmaz/decimify/actions?query=event%3Apush+branch%3Amain+workflow%3ACI)
[![Pypi](https://img.shields.io/pypi/v/decimify.svg)](https://pypi.python.org/pypi/decimify)
[![Versions](https://img.shields.io/pypi/pyversions/decimify.svg)](https://github.com/zahidkizmaz/decimify)
[![Codecov](https://codecov.io/gh/zahidkizmaz/decimify/branch/main/graph/badge.svg?token=2O3A7Z5NKV)](https://codecov.io/gh/zahidkizmaz/decimify)
[![License](https://img.shields.io/github/license/zahidkizmaz/decimify.svg)](https://github.com/zahidkizmaz/decimify/blob/main/LICENSE)

Parse numbers with different formatting to builtin python Decimal.

> A decimal separator is a symbol used to separate the integer part from the fractional part of a number written in decimal form (e.g. "." in 12.45). Different countries officially designate different symbols for use as the separator. The choice of symbol also affects the choice of symbol for the thousands separator used in digit grouping.

#### Some examples of large number presentations in all around the world:

| Large Number | Locale                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1,234,567.89 | Australia, Cambodia, Canada (English-speaking; unofficial), China, Cyprus (currency numbers), Hong Kong, Iran, Ireland, Israel, Japan, Korea, Macau (in Chinese and English text), Malaysia, Malta, Mexico, Namibia, New Zealand, Pakistan, Peru (currency numbers), Philippines, Singapore, South Africa (English-speaking; unofficial), Taiwan, Thailand, United Kingdom and other Commonwealth states except Mozambique, United States.                                                            |
| 1234567.89   | SI style (English version), Canada (English-speaking; official), China, Estonia (currency numbers), Hong Kong (in education), Mexico, Namibia, South Africa (English-speaking; unofficial), Sri Lanka, Switzerland (in federal texts for currency numbers only), United Kingdom (in education), United States (in education).                                                                                                                                                                         |
| 1234567,89   | SI style (French version), Albania, Belgium (French), Brazil, Bulgaria, Canada (French-speaking), Costa Rica, Croatia, Czech Republic, Estonia, Finland, France, Hungary, Italy (in education), Latin America, Latin Europe, Latvia, Lithuania, Macau (in Portuguese text), Mozambique, Norway, Peru, Poland, Portugal, Russia, Serbia (informal), Slovakia, South Africa (officiale RAE and CSIC), Sweden, Switzerland (in federal texts, except currency numbers), Ukraine, Vietnam (in education). |
| 1.234.567,89 | Austria, Belgium (Dutch), Bosnia and Herzegovina, Brazil (informal and in technology), Chile, Colombia, Croatia (in bookkeeping and technology), Denmark, Germany, Greece, Indonesia, Italy, Latin America (informal), Netherlands, Romania, Slovenia, Serbia, Spain (used until 2010, inadvisable use according to the RAE and CSIC), Turkey, Uruguay, Vietnam.                                                                                                                                      |
| 1,234,567·89 | Malaysia, Philippines (uncommon today), Singapore, United Kingdom (older, typically handwritten; in education)                                                                                                                                                                                                                                                                                                                                                                                        |
| 12,34,567.89 | Bangladesh, India, Nepal, Pakistan (see Indian numbering system).                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 1234567.89   | Bangladesh, India, Nepal, Pakistan (see Indian numbering system).                                                                                                                                                                                                                                                                                                                                                                                                                                     |

[Reference](https://en.wikipedia.org/wiki/Decimal_separator)

**decimify** aims to solve this problem by automatically converting many common formats into python `Decimal`.

Without having any external dependencies. It uses builtin python functions to convert string representation of numbers to Decimal.

## Installation

```shell
pip install -U decimify
```

## Usage

```python
from decimify import decimify

my_decimal = decimify('23 234.678,00')
my_decimal
# Decimal('23234678.00')
```
