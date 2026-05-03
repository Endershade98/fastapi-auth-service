# tests/domain/value_objects/test_timestamp.py

import pytest
from datetime import datetime, timezone

from src.domain.value_objects.shared.timestamp import Timestamp


def test_now():
    ts = Timestamp.now()
    assert ts.value is not None


def test_compare():
    a = Timestamp(datetime(2024,1,1,tzinfo=timezone.utc))
    b = Timestamp(datetime(2025,1,1,tzinfo=timezone.utc))

    assert a.is_before(b)
    assert b.is_after(a)


def test_naive_datetime_invalid():
    with pytest.raises(Exception):
        Timestamp(datetime.now())