" css.vim - ftplugin for css files
"
" $Author$
" $Date$
" $Revision$ 

" vim:set fdm=marker sw=4 ts=4:
 
" CSS fold markers for css blocks (zE to remove folds) {{{1
map cfm; <ESC>:%s/{ *$/{ \/\*{{{\*\//<CR>:%s/^} *$/} \/\*}}}\*\//<CR> 
