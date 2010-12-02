" ruby.vim 
"
" $Author$
" $Date$
" $Revision$ 

" ruby linting - use :make<CR><CR> to check syntax {{{1
set makeprg=erb\ %
set errorformat=%m\ in\ %f\ on\ line\ %l 

" Max line length for ruby is 80 chars {{{1
match ErrorMsg '\%>80v.\+'

" Modeline {{{1
" vim:set fdm=marker sw=4 ts=4:
