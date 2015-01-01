# coding=utf-8

from __future__ import with_statement

from contextlib import closing
from zipfile import ZipFile, ZIP_DEFLATED
import os


def zip_dir(base_dir, archive_name):
    """
    Ref: http://stackoverflow.com/a/296722/752142

    :param base_dir:
    :param archive_name:
    """
    assert os.path.isdir(base_dir)

    with closing(ZipFile(archive_name, "w", ZIP_DEFLATED)) as target_zip_file:
        for root, dirs, files in os.walk(base_dir):
            # NOTE: ignore empty directories
            for one_file in files:
                absolute_file_name = os.path.join(root, one_file)
                zip_file_name = absolute_file_name[len(base_dir) + len(os.sep):]
                target_zip_file.write(absolute_file_name, zip_file_name)
