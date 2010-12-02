" php.vim - ftplugin for php files
"
" $Author$
" $Date$
" $Revision$ 

" vim:set fdm=marker sw=4 ts=4:

" php linting - use :make<CR><CR> to check syntax {{{1
set makeprg=php\ -l\ %
set errorformat=%m\ in\ %f\ on\ line\ %l
