# src/domain/value_objects/oauth/scope_set.py

from mypy.scope import Scope
from dataclasses import dataclass


@dataclass(frozen=True)
class ScopeSet:
    values: frozenset[Scope]

    def contains(self, scope: str):
        return any(s.value == scope for s in self.values)