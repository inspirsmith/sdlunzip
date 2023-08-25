import zipfile

import pytest
import sdlunzip


def test_bad_password_on_legacy(monkeypatch):
    monkeypatch.setattr(sdlunzip.api, "SDL_PASSWORD", b"BAD PASSWORD")
    zip = zipfile.ZipFile("./tests/data/legacy_log_1.zip")
    with pytest.raises(PermissionError):
        sdlunzip.get(zip)


def test_good_password_on_legacy():
    zip = zipfile.ZipFile("./tests/data/legacy_log_1.zip")
    assert sdlunzip.get(zip)


def test_bad_password_on_openbmc(monkeypatch):
    monkeypatch.setattr(sdlunzip.api, "SDL_PASSWORD", b"BAD PASSWORD")
    zip = zipfile.ZipFile("./tests/data/openbmc_log_1.zip")
    assert sdlunzip.get(zip)


def test_good_password_on_openbmc(monkeypatch):
    zip = zipfile.ZipFile("./tests/data/openbmc_log_1.zip")
    assert sdlunzip.get(zip)


def test_get_bad_zip_type():
    with pytest.raises(TypeError):
        sdlunzip.get("This is not a zip file.") # type: ignore


def test_get_not_a_log():
    zip = zipfile.ZipFile("./tests/data/not_a_log.zip")
    with pytest.raises(KeyError):
        sdlunzip.get(zip)


def test_is_bundled_zip_true():
    zip = zipfile.ZipFile("./tests/data/bundled.zip")
    assert sdlunzip.api._is_bundled_zip(zip)
