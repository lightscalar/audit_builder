"""paths.py
--
Handle path generation for the application.
"""
import audit_builder

import inspect
import os


class GetPath:
    """Get the paths that are important to the project."""

    @property
    def root(self) -> str:
        """Return the root path of the current library."""
        return os.path.abspath(inspect.getmodule(audit_builder).__path__[0])

    @property
    def styles(self) -> str:
        """Return the path to the CSS stylesheet."""
        return f"{self.root}/assets/styles/output.css"

    @property
    def images(self) -> str:
        return f"{self.root}/assets/images"

    @property
    def reports(self) -> str:
        return f"{self.root}/audit_builder/audit_reports"


# Make an instance for convenience...
getpath = GetPath()
