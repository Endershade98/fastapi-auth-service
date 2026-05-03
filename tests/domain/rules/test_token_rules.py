# tests/domain/rules/test_token_rules.py

import pytest

from src.domain.rules.token_rules import TokenRules


def test_refresh_token_not_used_allowed():
    TokenRules.ensure_one_time_use(False)


def test_refresh_token_already_used_blocked():
    with pytest.raises(Exception):
        TokenRules.ensure_one_time_use(True)