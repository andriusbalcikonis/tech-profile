# Django cheatsheet / notes

## Tip:

`.all()` will reevaluate (refetch)
Set primary key to None to copy model instance https://docs.djangoproject.com/en/3.0/topics/db/queries/#copying-model-instances

## Tip:

`.only()` is very similar to `.values()`, but has some differences:

- `.only()` returns model instances, just select skips some fields
- `.values` returns smth like "list of dicts"...
  https://stackoverflow.com/questions/11974691/difference-between-values-and-only

## Tip

Weird thing - `.all()` will not cause queryset to be evaluated.

See:

- https://docs.djangoproject.com/en/3.1/ref/models/querysets/#all
- https://docs.djangoproject.com/en/3.1/ref/models/querysets/#when-querysets-are-evaluated

# Tip

If you need smth to be ordered randomly, use `.order_by('?')`

https://books.agiliq.com/projects/django-orm-cookbook/en/latest/random.html
