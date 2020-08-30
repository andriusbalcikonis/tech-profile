# Python - notes of things I found interesting (and useful)

## Notable changes in versions

In v3.5:

- Type hints: https://docs.python.org/3/whatsnew/3.5.html#whatsnew-pep-484
- Async awayt: https://docs.python.org/3/whatsnew/3.5.html#whatsnew-pep-492

In 3.6:

- Formatted string literals: https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-pep498

In 3.8:

- Walrus operator: https://docs.python.org/3/whatsnew/3.8.html#assignment-expressions
- Positional args: https://docs.python.org/3/whatsnew/3.8.html#positional-only-parameters

## Garbage collector will cleanup loop-references at some point

Q12 here: https://www.codementor.io/@sheena/essential-python-interview-questions-du107ozr6

## Nice clarification of why python is strongly typed, but dynamically typed

Q3 here: https://www.interviewbit.com/python-interview-questions/

## Nice clear example of decorator

Q10 here: https://www.interviewbit.com/python-interview-questions/

## Nice clear example of generator

Q24 here: https://www.interviewbit.com/python-interview-questions/

## Nice clear example args and kwargs

Q38 here: https://www.interviewbit.com/python-interview-questions/

## Minimal setup.py from setuptools docs

https://setuptools.readthedocs.io/en/latest/setuptools.html#basic-use

## Converter from py2 to py3

https://docs.python.org/2/library/2to3.html

## Popular packages, that may become useful:

- AWS SDK https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
- For advanced datetime usage https://dateutil.readthedocs.io/en/stable/ and https://pypi.org/project/pytz/
- Verifying SSL certs https://pypi.org/project/certifi/
- Yaml parser https://pypi.org/project/PyYAML/
- Guessing charsets https://pypi.org/project/chardet/
- Json advanced parser https://pypi.org/project/jmespath/

(From https://medium.com/better-programming/the-22-most-used-python-packages-in-the-world-7020a904b2e)

## Popular django packages:

- Cors headers https://pypi.org/project/django-cors-headers/
- Django-filter provides a simple way to filter down a queryset based on parameters a user provides. https://django-filter.readthedocs.io/en/master/guide/usage.html
- Redis https://pypi.org/project/django-redis/
- Pytest https://pypi.org/project/pytest-django/
- Storages, like S3 https://pypi.org/project/django-storages/

## Factory class functions pattern

Smth like this:

```
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'

    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])
```

See "Delicious Pizza Factories With @classmethod" in https://realpython.com/instance-class-and-static-methods-demystified/

## Python coroutines is an interesting concept

- Generators produce data for iteration
- Coroutines are consumers of data
- To keep your brain from exploding, you don't mix the two concepts together
- `yield from ...` is best used to "feed" from generator to coroutine
  https://stackoverflow.com/a/26109157

Informative & well-written slides about that: http://dabeaz.com/coroutines/Coroutines.pdf
