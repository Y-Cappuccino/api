#   -*- coding: utf-8 -*-


from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.distutils")


name = "ycappuccino_api"
default_task = "publish"
version = "0.1.0"


@init
def set_properties(project):
    project.set_property("core", False)  # default is True
    project.depends_on_requirements("requirements.txt")
