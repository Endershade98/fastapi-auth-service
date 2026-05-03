# tests/domain/value_objects/security/test_password_hash.py

from src.domain.value_objects.security.password_hash import PasswordHash


class FakeHasher:
    def verify(self, plain, hashed):
        return plain == "secret" and hashed == "HASH"


def test_password_verify_true():
    vo = PasswordHash("HASH")
    assert vo.verify("secret", FakeHasher())


def test_password_verify_false():
    vo = PasswordHash("HASH")
    assert not vo.verify("wrong", FakeHasher())