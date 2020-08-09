# Django cheatsheet / notes

## Tip:

`.all()` will reevaluate (refetch)
Set primary key to None to copy model instance https://docs.djangoproject.com/en/3.0/topics/db/queries/#copying-model-instances

## Tip:

`.only()` is very similar to `.values()`, but has some differences:

- `.only()` returns model instances, just select skips some fields
- `.values` returns smth like "list of dicts"...
  https://stackoverflow.com/questions/11974691/difference-between-values-and-only
