"""Check correctness of *.ini files."""
import fnmatch
import os
import sys

if sys.version_info[0] == 3:
    from configparser import ConfigParser
    from io import StringIO
else:
    import ConfigParser
    from cStringIO import StringIO

DEFAULTS = {
    'files': '*.ini',
}


def check(file_staged_for_commit, options):
    basename = os.path.basename(file_staged_for_commit.path)
    if not fnmatch.fnmatch(basename, options.ini_files):
        return True
    contents = StringIO(file_staged_for_commit.contents)
    parser = ConfigParser.RawConfigParser()
    try:
        parser.readfp(contents, file_staged_for_commit.path)
    except ConfigParser.Error as e:
        print(e)
        return False
    else:
        return True
