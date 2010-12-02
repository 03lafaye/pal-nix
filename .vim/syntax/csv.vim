" csv.vim
"   Author: Pierre LaFayette (plafayette@jonahgroup.com)
"   Date:   Mar 27, 2009
"   Version: 0.0.1
" ---------------------------------------------------------------------
"  Initialization {{{1
"
" Remove any old syntax stuff hanging around
syntax clear

" ---------------------------------------------------------------------

"  Syntax {{{1
"
" Recognizes ',' and '|' as valid delimiters

syn match Col1 "^[^,|]*" nextgroup=Col2
syn match Col2 "[,|][^,|]*"hs=s+1 contained nextgroup=Col3
syn match Col3 "[,|][^,|]*"hs=s+1 contained nextgroup=Col4
syn match Col4 "[,|][^,|]*"hs=s+1 contained nextgroup=Col5
syn match Col5 "[,|][^,|]*"hs=s+1 contained nextgroup=Col6
syn match Col6 "[,|][^,|]*"hs=s+1 contained nextgroup=Col7
syn match Col7 "[,|][^,|]*"hs=s+1 contained nextgroup=Col8
syn match Col8 "[,|][^,|]*"hs=s+1 contained nextgroup=Col9
syn match Col9 "[,|][^,|]*"hs=s+1 contained nextgroup=Col10
syn match Col10 "[,|][^,|]*"hs=s+1 contained nextgroup=Col11
syn match Col11 "[,|][^,|]*"hs=s+1 contained nextgroup=Col12
syn match Col12 "[,|][^,|]*"hs=s+1 contained nextgroup=Col13
syn match Col13 "[,|][^,|]*"hs=s+1 contained nextgroup=Col14
syn match Col14 "[,|][^,|]*"hs=s+1 contained nextgroup=Col15
syn match Col15 "[,|][^,|]*"hs=s+1 contained nextgroup=Col16
syn match Col16 "[,|][^,|]*"hs=s+1 contained nextgroup=Col17
syn match Col17 "[,|][^,|]*"hs=s+1 contained nextgroup=Col18
syn match Col18 "[,|][^,|]*"hs=s+1 contained nextgroup=Col19
syn match Col19 "[,|][^,|]*"hs=s+1 contained nextgroup=Col20
syn match Col20 "[,|][^,|]*"hs=s+1 contained

 
" ---------------------------------------------------------------------
"  Highlighting {{{1

" Color definitions
hi Red ctermfg=red
hi Blue ctermfg=blue 
hi Green ctermfg=green 
hi Magenta ctermfg=magenta 
hi Cyan ctermfg=cyan 
hi White ctermfg=white 
hi Red ctermfg=red 
hi Yellow ctermfg=yellow 
hi Green ctermfg=green 
hi Magenta ctermfg=magenta 
hi LightBlue ctermfg=lightblue
hi LightGreen ctermfg=lightgreen
hi Gray ctermfg=gray
hi Brown  ctermfg=brown

" Col column colors
hi def link Col1 Red
hi def link Col2 Blue
hi def link Col3 Green
hi def link Col4 Magenta
hi def link Col5 Cyan
hi def link Col6 White
hi def link Col7 LightGreen
hi def link Col8 LightBlue
hi def link Col9 Gray
hi def link Col10 Brown
hi def link Col11 Red
hi def link Col12 Blue
hi def link Col13 Green
hi def link Col14 Magenta
hi def link Col15 Cyan
hi def link Col16 White
hi def link Col17 LightGreen
hi def link Col18 LightBlue
hi def link Col19 Gray
hi def link Col20 Brown 

" ---------------------------------------------------------------------

" Modeline {{{1
" vim: ts=4 fdm=marker  

