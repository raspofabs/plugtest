#!/bin/bash

# -n for no-cache
# --with to add the other packages
# always use relative or absolute path, otherwise it tries to read from the package repository
uvx -n --with ./amber_add --with ./amber_mult ./amber_core
