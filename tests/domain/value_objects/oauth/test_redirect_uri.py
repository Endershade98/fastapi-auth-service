# tests/domain/value_objects/oauth/test_redirect_uri.py

import pytest
from src.domain.value_objects.oauth.redirect_uri import RedirectUri


def test_valid_uri():
    uri = RedirectUri("https://app.test/callback")
    assert uri.value == "https://app.test/callback"


def test_invalid_uri():
    with pytest.raises(Exception):
        RedirectUri("not-valid")