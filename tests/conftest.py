import os
import pytest

import webhook

@pytest.fixture
def app():
    app = webhook.create_app()
    return app
