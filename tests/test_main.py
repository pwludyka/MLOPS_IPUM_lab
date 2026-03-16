from settings import Settings
from main import export_envs


def test_settings_load():
    export_envs("test")
    settings = Settings()
    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "fake_app"
    assert settings.API == "secret_test"
