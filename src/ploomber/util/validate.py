from ploomber.exceptions import ValidationError
from ploomber.io import pretty_print


def keys(valid, passed, required=None, name='spec'):
    passed = set(passed)

    if valid:
        if extra := passed - set(valid):
            raise ValidationError(
                f"Error validating {name}, the following keys aren't valid: {pretty_print.iterable(extra)}. Valid keys are: {pretty_print.iterable(valid)}"
            )

    if required:
        if missing := set(required) - passed:
            raise ValidationError(f"Error validating {name}. Missing "
                                  f"keys: { pretty_print.iterable(missing)}")
