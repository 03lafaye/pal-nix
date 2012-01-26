" quic.vim - vim configuration for QUIC Webtech development
" @author pierre.lafayette

let host = system('echo $HOSTNAME')
if ( host !~ 'Dende' ) 
    finish
endif  

" template for new .cpp, .h, .h
autocmd BufNewFile *.h,*.c,*.cpp 0r $HOME/.vim/templates/quic/copyright.tpl.h
