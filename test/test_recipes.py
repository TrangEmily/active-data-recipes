from __future__ import absolute_import, print_function

import json
import os

from pytest import xfail

from adr.cli import run_recipe
from adr.recipe import is_fail
from adr.util.config import Configuration

here = os.path.abspath(os.path.dirname(__file__))


def test_recipe(patch_active_data, recipe_test, validate):
    try:
        patch_active_data(recipe_test)

        config = Configuration()
        config.fmt = "json"
        result = json.loads(run_recipe(recipe_test['recipe'], recipe_test['args'], config))

        validate(recipe_test, result)
    except Exception as e:
        if is_fail(recipe_test['recipe']):
            xfail(str(e))
        else:
            raise e
