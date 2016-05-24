import os

def _np(p):
    return os.path.normpath(p)

ROOT = _np(os.path.join(os.path.dirname(__file__), '..'))
STATIC_DIR = _np(os.path.join(ROOT, 'showdocs', 'static'))

STAGING_DIR = _np(os.path.join(ROOT, 'staging'))
EXTERNAL_DIR = _np(os.path.join(ROOT, 'external'))

TEST = True
LOG = False

def update(d):
    globals().update(d)

    from showdocs import setuplogging
    setuplogging()
