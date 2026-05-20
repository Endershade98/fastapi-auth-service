# src/domain/value_objects/oauth/scope_set.py

from dataclasses import dataclass

from src.domain.value_objects.oauth.scope import Scope


@dataclass(frozen=True)
class ScopeSet:
    values: frozenset[Scope]

    def contains(self, scope: str) -> bool:
        return any(
            s.value == scope
            for s in self.values
        )