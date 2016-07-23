#!/usr/bin/env python3
# coding: utf-8

# Appex script to copy a git file, folder, or repo from the Working Copy app

import appex, os, shutil, zipfile

from_wc = os.path.abspath(os.path.expanduser('from Working Copy'))


def move_file(file_paths):
    assert_msg = 'How did you select multiple files in Working Copy?!?'
    assert len(file_paths) == 1, assert_msg
    local_path = file_paths[0].split('/File Provider Storage/')[-1]
    local_path, file_name = os.path.split(local_path)
    local_path = os.path.join(from_wc, local_path)
    os.makedirs(local_path, exist_ok=True)
    shutil.copy2(file_paths[0], local_path)
    # editor.open_file(os.path.join(local_path, file_name))
    return '{} was copied to {}'.format(file_name, local_path)


def move_folder(file_paths):
    assert_msg = 'How did you select multiple directories in Working Copy?!?'
    assert len(file_paths) == 2, assert_msg
    print(file_paths)
    local_path = file_paths[0].split('/File Provider Storage/')[-1]
    local_path = os.path.join(from_wc, local_path)
    os.makedirs(local_path, exist_ok=True)
    with zipfile.ZipFile(file_paths[-1]) as in_file:
        in_file.extractall(path=local_path)
    fmt = '{} was expanded into {}'
    return fmt.format(os.path.split(file_paths[-1])[-1], local_path)


def main():
    if appex.is_running_extension():
        file_paths = appex.get_file_paths()
        assert file_paths, 'No file paths found!'
        func = move_folder if file_paths[-1].endswith('.zip') else move_file
        print(func(file_paths))
    else:
        print('''
In Working Copy app select a file, directory, or repo to be copied into Pythonista.
Click the Share icon at the upper right corner of the Working Copy screen.
Click Run Pythonista Script.
Click on this script.
Click the run button.
When you return to Pythonista your files should be in the 'from Working Copy' directory.''')

if __name__ == '__main__':
    main()
