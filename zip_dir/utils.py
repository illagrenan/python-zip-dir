# coding=utf-8

from __future__ import with_statement

from contextlib import closing
from zipfile import ZipFile, ZIP_DEFLATED
import os

ZIP_FILE_MODE = "w"


def create_zip_archive(base_dir_path, archive_name):
    """
    Create *.zip file from given base dir path.
    Ref: http://stackoverflow.com/a/296722/752142

    :type archive_name: str
    :type base_dir_path: str
    :rtype : zipfile.ZipFile
    """
    assert os.path.isdir(base_dir_path)

    with closing(ZipFile(archive_name, ZIP_FILE_MODE, ZIP_DEFLATED)) as target_zip_file:
        for root, dirs, files in os.walk(base_dir_path):
            # NOTE: ignore empty directories
            for one_file in files:
                absolute_file_name = os.path.join(root, one_file)
                zip_file_name = absolute_file_name[len(base_dir_path) + len(os.sep):]
                target_zip_file.write(absolute_file_name, zip_file_name)

    return target_zip_file