# php-errata
Check function documentation for assistance on code reviews

No error checking, no filtering of duplicates, needs better warning checks, etc.

parse_docs.py: parse downloaded copy of php function documentation. These have been provided in the .txt files

code_check.py: check over a code base for the discovered/interesting functions. Code base must start in a SOURCE/ directory

Output will be written to files in the output/ directory
