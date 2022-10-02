import os

import pytest


def requires_mockserver(*args):
    MOCK_SERVER = int(os.environ.get('MOCK_SERVER', 0))
    return pytest.mark.skipif(MOCK_SERVER == 0, reason=f"Mock server is not running")
