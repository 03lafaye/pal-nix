" python.vim
"
" $Author: pierre.lafayette $
" $Date: 2009-02-14 10:30:07 -0500 (Sat, 14 Feb 2009) $
" $Revision: 91 $

" Indent {{{1
set expandtab " enter spaces when tab is pressed
set textwidth=80 " break lines when line length increases
set tabstop=4 " use 4 spaces to represent tab
set softtabstop=4
set shiftwidth=4 " number of spaces to use for auto indent
set autoindent " copy indent from current line when starting a new line
set backspace=indent,eol,start " make backspaces more powerfull

" Jump between code and python class libraries {{{1
if has('python')
python << EOF
import os
import sys
import vim
for p in sys.path:
    if os.path.isdir(p):
        vim.command(r"set path+=%s" % (p.replace(" ", r"\ ")))
EOF
endif

" Generate tags for python libraries {{{1
" $ ctags -R -f ~/.vim/tags/python.ctags /usr/lib/python2.5/

" Use the generated tags {{{1
set tags+=$HOME/.vim/tags/python.ctags

" Code Completion {{{1
" set omnifunc=pythoncomplete#Complete

" Syntax error hilighting {{{1
syn match pythonError "^\s*def\s\+\w\+(.*)\s*$" display
syn match pythonError "^\s*class\s\+\w\+(.*)\s*$" display
syn match pythonError "^\s*for\s.*[^:]$" display
syn match pythonError "^\s*except\s*$" display
syn match pythonError "^\s*finally\s*$" display
syn match pythonError "^\s*try\s*$" display
syn match pythonError "^\s*else\s*$" display
syn match pythonError "^\s*else\s*[^:].*" display
syn match pythonError "^\s*if\s.*[^\:]$" display
syn match pythonError "^\s*except\s.*[^\:]$" display
syn match pythonError "[;]$" display
syn keyword pythonError         do

" Make program for syntax checking {{{1
set makeprg=python\ -c\ \"import\ py_compile,sys;\ sys.stderr=sys.stdout;\ py_compile.compile(r'%')\"
autocmd BufRead *.py set efm=%C\ %.%#,%A\ \ File\ \"%f\"\\,\ line\ %l%.%#,%Z%[%^\ ]%\\@=%m

" Ctrl+h to select range for make program {{{1
if has('python')
python << EOL
import vim
def EvaluateCurrentRange():
    eval(compile('\n'.join(vim.current.range),'','exec'),globals())
EOL
endif

noremap <C-H> :py EvaluateCurrentRange()<CR>

" Max line length for ruby is 80 chars {{{1
match ErrorMsg '\%>80v.\+'

" Modeline {{{1
" vim:set fdm=marker sw=4 ts=4:
