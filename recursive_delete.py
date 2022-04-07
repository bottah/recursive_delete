# Author: Jason Pedersen
# Date: 4/6/2022

import os
import sys
import glob

'''
The request for an approach to recursively remove all files in a directory, with the *.pyc extension, 
could be accomplished in two lines of code... the rest of the script is an attempt to
demonstrate additional aptitude, albeit possibly just a bit overly pragmatic.
'''

'''
recursively removes all pyc files from the current working directory
'''
def del_pyc_files():
    for path in glob.glob(os.path.join('**', '*.pyc'), recursive=True): # Python 3.5 or great is required for recursive glob
        os.unlink(path)

#####
#####
#####

# GLOBALS
dry_run = True
python_version = float('%s.%s' % (sys.version_info.major, sys.version_info.minor))
# GLOBALS

'''
description:
    recursively search a target directory for a files with a specific extension
params:
    file_ext (required): file extension to be found
    start_dir (optional): starting point of recursion, defaults at the script directory
return:
    list of paths
'''
def get_path_list(file_ext=None, start_dir=None):

    path_list = []

    if file_ext is not None and len(file_ext) > 0:

        file_ext = file_ext if file_ext[0] != '.' else '.'.join(file_ext.split('.')[1:]) # strip period, if included
        start_dir = start_dir if start_dir is not None else '.'

        if python_version < 3.5:
            for root, dirs, files in os.walk(start_dir):
                for file_name in files:
                    path = os.path.join(root, file_name)
                    if '.%s' % (file_ext) in path:
                        path_list.append(path)
        else:
            path_list = glob.glob(os.path.join(start_dir, '**', '*.%s' % (file_ext)), recursive=True)

    return path_list

'''
description:
    delete list of file paths
params:
    path_list (required): list of file paths to be deleted
'''
def del_path_list(path_list):
    for path in path_list:
        if dry_run:
            print('(dry_run)', end=' ')
        else:
            try:
                os.unlink(path)
                print('(deleted)', end=' ')
            except Exception as e:
                print('ERROR: %s' % (e))
        print('path: "%s"' % (path))

'''
description:
    - recursively search a target directory for a files with a specific extension
    - display the results
    - prompt the user if they want to continue with the delete
    - pass the list to a delete helper function
params:
    file_ext (required): file extension to be found... 
    start_dir (optional): starting point of recursion, defaults at the script directory
'''
def delete(file_ext, start_dir=None):
    print('\nrecursive_delete(file_ext="%s", start_dir="%s")' % (file_ext, start_dir))

    path_list = get_path_list(file_ext=file_ext, start_dir=start_dir)

    if len(path_list) > 0:
        print('\nPaths to be deleted (qty=%s):' % (len(path_list)))
        for path in path_list:
            print(path)
        del_confirmed = input('\nContinue? [yes|NO] ')
        if del_confirmed.lower() == 'yes':
            del_path_list(path_list)
        else:
            print('No changes made. Exiting!\n')
    else:
        print('Nothing found with the extension: "%s"\n' % (file_ext))

'''
description:
    call specified method with space delimited parameters...
    if method and at least one parameter (file_ext) are not provided, prompt for input
    then call recursive_delete
'''
if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[0].split(os.sep)[-1] == os.path.basename(__file__): 
        locals()[sys.argv[1]](*sys.argv[2:])
    else: # not enough parameters, or method not specified
        print('')
        print('### '*20)
        print('\nUsage: call delete directly, with space delimited parameters')
        print('EXAMPLE: python recursive_delete.py delete file_ext start_dir')
        print('\n... or you can enter the parameters here (ctrl+c to quit):')
        file_ext = input('file_ext: ')
        start_dir = input('start_dir: [.] ')
        delete(file_ext, start_dir)
