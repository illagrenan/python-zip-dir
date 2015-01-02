Python ZIP dir function
==============

A simple function to create zipped folder.

## Usage ##

```
└───some_folder
    │   test_file.txt
    │
    ├───a
    │       aaa_file.txt
    │       aa_file.txt
    │       a_file.txt
    │
    └───b
            b_file.txt
```

```python
>>> from zip_dir.utils import create_zip_archive
>>> create_zip_archive(base_dir_path="some_folder", archive_name="my_archive.zip")
```


```
│   my_archive.zip
│   │   test_file.txt
│   │
│   ├───a
│   │       aaa_file.txt
│   │       aa_file.txt
│   │       a_file.txt
│   │
│   └───b
│           b_file.txt
│
└───some_folder
    │   test_file.txt
    │
    ├───a
    │       aaa_file.txt
    │       aa_file.txt
    │       a_file.txt
    │
    └───b
            b_file.txt
```

## Installation ##

```bash
pip install -e git+https://github.com/illagrenan/python-zip-dir#egg=zip_dir --upgrade
```

## License ##

The MIT License (MIT)

Copyright © 2015 Vašek Dohnal (@illagrenan)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.