#!/bin/sh
find $1 -name '*.py' \
-o -name '*.pl' \
-o -name '*.rb' \
-o -name '*.java' \
-o -iname '*.[CH]' \
-o -name '*.cpp' \
-o -name '*.cc' \
-o -name '*.hpp'  \
-o -name '*.html' \
-o -name '*.js' \
> cscope.files

# -b: just build
# -q: create inverted index
cscope -b -q
