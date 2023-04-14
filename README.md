# decimify

Parse numbers to Decimal

#### Some examples of large number presentations in all around the world:

| Locale                        | Large Number      |
| ----------------------------- | ----------------- |
| Canadian (English and French) | 4 294 967 295,000 |
| Danish                        | 4 294 967 295,000 |
| Finnish                       | 4 294 967 295,000 |
| French                        | 4 294 967 295,000 |
| German                        | 4 294 967.295,000 |
| Italian                       | 4.294.967.295,000 |
| Norwegian                     | 4.294.967.295,000 |
| Spanish                       | 4.294.967.295,000 |
| Swedish                       | 4 294 967 295,000 |
| GB-English                    | 4,294,967,295.00  |
| US-English                    | 4,294,967,295.00  |
| Thai                          | 4,294,967,295.00  |

Data taken [from](https://docs.oracle.com/cd/E19455-01/806-0169/overview-9/index.html)

## Usage

```python
from decimify import decimify

my_decimal = decimify('23 234.678,00')
my_decimal
# Decimal('23234678.00')
```
