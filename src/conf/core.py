import threading
import importlib
import inspect
import sys
from typing import Final

class _SingletonMeta(type):
    """This is a thread-safe implementation of the Singleton"""

    _lock: threading.Lock = threading.Lock()

    def __init__(self, *args, **kwargs):
        super(_SingletonMeta, self).__init__(*args, **kwargs)
        self._instance = None
    
    def __call__(self, *args, **kwargs):
        with self._lock:
            if self._instance is None:
                self._instance = super(_SingletonMeta, self).__call__(*args, **kwargs)
        return self._instance


class _Settings(metaclass=_SingletonMeta):
    def __init__(self):
        self._dict = {}
        self._setup()

    def _setup(self):
        self._settings_module = self._get_settings_from_cmd_line()
        if not self._settings_module:
            self._settings_module = "conf.settings"
        self._load_settings_module()

    def _get_settings_from_cmd_line(self):
        for argument in sys.argv:
            if argument.startswith("--settings"):
                try:
                    return argument.split("=")[1]
                except IndexError:
                    return None

    def _load_settings_module(self):
        module = importlib.import_module(self._settings_module)
        self._dict = {
            setting: getattr(module, setting) 
            for setting in dir(module)
            if setting.isupper() and not (
                setting.startswith("_") or setting.startswith("__")
            )
        }

    def __getattr__(self, attr):
        try:
            return self._dict[attr]
        except KeyError as e:
            raise AttributeError(f"You did not set {attr} setting") from e

    def as_dict(self):
        return self._dict.copy()


settings = _Settings()