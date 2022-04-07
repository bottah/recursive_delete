The request for an approach to recursively remove all files in a directory, with the *.pyc extension, could be accomplished in two lines of code... the rest of the script is an attempt to demonstrate additional aptitude, albeit possibly just a bit overly pragmatic.

Usage: call delete directly, with space delimited parameters

EXAMPLE: python recursive_delete.py delete pyc

... or if you call recursive_delete.py without parameters, it'll prompt you in an interactive shell-type-thing.

NOTE: To actually delete anything, you'll need to change dry_run to something other than True
