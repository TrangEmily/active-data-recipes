"""
Get skipped tests on the ActiveData schema. The above command returns the
test suites and their count which were skipped/disabled between specified period.

.. code-block:: bash

    adr skipped_tests
"""
from __future__ import absolute_import, print_function

from ..context import override
from ..query import run_query

RUN_CONTEXTS = [
    override('limit', default=25, help="Maximum number of users in result"),
    override('sort_key', default=1, help="Key to sort on (int, 0-based index)"),
]


def run(config, args):

    result = run_query('skipped_tests', config, args)['data']

    result.sort(key=lambda x: x[0])
    result.insert(0, ['Result test', 'run suite', 'count'])
    return result
