---
date: 2022-10-24 16:07:20
templateKey: blog-post
title: Grainger Pre questions
published: False
tags:
  -
---

For both the Senior Data Engineer and Data Engineer.

Todo: For both of these, Take this improper code and change it into easier to
support or maintain?...the code “works” but is hard to understand. Can it be
changed into more understandable code for people who will be working on the
code in the future?

Software craftsmanship and clean code concepts. This shouldn’t take more than
15 minutes (not timed at all but shouldn’t be too intrusive in your life to
complete.

## SQL Question

Acme’s business team is building a report to show only the customers who have
ordered within the last two weeks and the number of orders each of those
customers placed. To support their report they will need the following columns:
Customer ID, Customer First Name, Customer Last Name, and Number of Orders.

● Will the query below solve this problem? If not, what would you recommend to change?

```sql
SELECT
    customer_id,
    first_name,
    last_name,
(
    SELECT COUNT(*) AS number_of_orders
    FROM sales
    WHERE customers.customer_id = sales.customer_id
    AND number_of_orders >= 1
)
FROM
    customers
WHERE
    sales.sale_dt >= current_date() - interval 2 weeks;
```

## Answer

I do not believe this will solve the problem stated. The subquery for the
count does not get filtered for the last two weeks, it will be a count of all
records.

I find the subquery for the `number_of_orders` in the SELECT clause to be more
confusing than necessary. Refactoring this to join an aggregated `num_orders`
subquery joining on customer_id, and counting on one of the records in the
sales table would make thiss easier to follow, and solve the issue in the
`WHERE` statement is not really filtering anything.

```sql
SELECT
    customers.customer_id,
    customers.first_name,
    customers.last_name,
    num_orders.number_of_orders,
FROM
    customers
LEFT JOIN (
    SELECT
        customer_id,
        count(*) as number_of_orders
    FROM
        sales
        sales.sale_dt >= current_date() - interval 2 weeks;
    ) as num_orders
    ON customers.customer_id = num_orders.customer_id
WHERE
    number_of_orders >= 1
```

In the etl roles that I have held, data like this has been ingested into a
python pipeline. If the data is quite large, some initial filtering would be
done in sql, but logic like this would be done in a pandas groupby.

## Python Question

Acme has recently noticed a large volume of potential duplicate customers. Their current
customer_id is based on the customer’s email address. They have noticed in the data many
instances of customers using “.” and “+” in their email addresses. They would like to create a
deduplicated list of customers by removing all periods before the @. They would also like to
remove all characters from the + to the @. They have provided the following test case for you:

● Original Email 1: <tommy.t.tester+throw.away.acct@gmail.com>
● Original Email 2: <tommy.t.tester+shopping@gmail.com>
● Transformed Email: <tommyttester@gmail.com>

Please review the function below and answer the questions.

● Will the function below accomplish this? Can you walk me through what this code is
doing?
● Would you recommend any additions or refactoring? Keep in mind this code will
eventually be merged into main through the team's CI/CD tooling.

## Answer

The code will work as expected as long as an email address contains only one
`@` sign. I am not sure if more than one `@` sign is possible. It creates a
function that creates an empty list of clean emails, iterates over a one
dimensional array that is input, cleans the email, appends it to the list, then
returns a deduplicated list. During the cleaning it splits the string into a
list of strings using `@` as the delimiter. It treats the first item in this
list as the username, and the second item as the domain. It removes all `.`
from the username. It splits the username into a list of strings using `+` as
the delimiter, and gets the first entry to call the new username. It then
creates a cleaned email formatting the username and domain into a string
separated by an `@` sign.

```python
def parse_data(customer_data): # parse_data does not describe the requirement very well, customer_data is "ok", but still not great
    d_o = list() # when I see Instanciate then modify, I generally look for a way to refactor into a list comprehension
    for data in customer_data:
        data_parts = data.split('@')

        # a and b are not very descriptive, I've suggested a few alternatives
        a = data_parts[0] # username or name
        b = data_parts[1] # domain or domain_name
        a = a.replace('.', '')
        a = a.split('+')[0]
        d_o.append('{}@{}'.format(a, b)) # unless your environment needs to support python < 3.6 you should be using f-strings over format strings
    return list(dict.fromkeys(d_o)) # this is an odd way to deduplicate a list, I generally see the use of sets instead of dict keys
```

I have provided a refactoring that I would do. Before merging into CI/CD, I
would reccomend getting full test coverage for these two functions with a
variety of different examples.

```python

from typing import List


class UnsupportedEmailFormat(NameError):
    ...


def _clean_email_address(email: str) -> str:
    """
    Given an email address remove all periods before the @, and remove all
    characters after any + if there is one.

    Args:
        email (str): an email string

    Returns
        a cleaned email

    Examples:

    ● Original Email 1: tommy.t.tester+throw.away.acct@gmail.com
    ● Original Email 2: tommy.t.tester+shopping@gmail.com
    ● Transformed Email: tommyttester@gmail.com

    """
    username, domain, *rest = email.split("@")
    if len(rest) > 0:
        # I am quite sure that a valid email cannot have more than one @ sign
        # in it, for now we will raise an error that we can account for if this
        # ever comes up.
        raise UnsupportedEmailFormat(
            f"{email} has more than one '@', which is unsupported by this project"
        )
    username = username.replace(".", "")
    username = username.split("+")[0]
    return f"{username}@{domain}"


def clean_email_addresses(email_addresses: List[str]) -> List[str]:
    """
    Given an array email address remove all periods before the @, and remove all
    characters after any + if there is one.

    Args:
        email_addresses (str): A list of email addresses

    Returns
        A list of  cleaned email addresses



    Examples:

    ● Original Email 1: tommy.t.tester+throw.away.acct@gmail.com
    ● Original Email 2: tommy.t.tester+shopping@gmail.com
    ● Transformed Email: tommyttester@gmail.com
    """

    return list(set([_clean_email_address(email) for email in email_addresses]))
```
