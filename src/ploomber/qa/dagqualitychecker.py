# NOTE: should this be part of each Source?
import warnings

from ploomber.util import requires


class DAGQualityChecker:

    def __call__(self, dag):
        self.empty_docstrings(dag)

    def empty_docstrings(self, dag):
        """Evaluate code quality
        """
        for name, task in dag.items():

            doc = task.source.doc

            if doc is None or doc == '':
                warnings.warn(f'Task "{name}" has no docstring')


@requires(['numpydoc'])
def diagnose(source):
    """Prints some diagnostics
    """
    from numpydoc.docscrape import NumpyDocString

    # [WIP] function to validate docstrings in sources that
    # have placeholders
    found = source.value.variables
    docstring_np = NumpyDocString(source.value.docstring())
    documented = {p[0] for p in docstring_np['Parameters']}

    print(
        f'The following variables were found in the template but are not documented: {found - documented}'
    )

    print(
        f'The following variables are documented but were not found in the template: {documented - found}'
    )

    return documented, found
