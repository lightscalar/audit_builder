"""paths.py
--
Handle path generation for the application.
"""
import audit_builder

import inspect
import os


class GetPath:
    """Get the paths that are important to the project."""

    def base_path(self) -> str:
        """Return the base path of the testify module."""
        return os.path.abspath(inspect.getmodule(audit_builder).__path__[0])

    def path_to_styles(self) -> str:
        """Return the path to the stylesheet."""
        return f"{self.base_path()}/audit_builder/assets/styles/output.css"

    def path_to_images(self) -> str:
        return f"{self.base_path()}/audit_builder/assets/images"


getpath = GetPath()
