" fbapp.vim - vim configuration for fbapp facebook development
"
" $Author: pierre.lafayette $
" $Date: 2008-11-29 22:09:00 -0500 (Sat, 29 Nov 2008) $
" $Revision: 3 $ 

let host = system('echo $HOSTNAME')
if ( host !~ 'idea' && host  !~ 'xtasy' ) 
    finish
endif 

" scp
" nnoremap <F12> :! scp % vu2031p@refreshpartners.com:demographics/%<CR>

" template for menu files
autocmd BufNewFile menu_*.php 0r $HOME/.vim/templates/refresh/menu_file.php
" template for ajax files
autocmd BufNewFile ajax_*.php 0r $HOME/.vim/templates/refresh/ajax_file.php
" template for action files
autocmd BufNewFile action_*.php 0r $HOME/.vim/templates/refresh/action_file.php 
" template for new html
autocmd BufNewFile *.html,*.css 0r $HOME/.vim/templates/refresh/template.html

nnoremap <C-J> /<+.\{-1,}+><CR>c/+>/e<CR>
inoremap <C-J> <ESC>/<+.\{-1,}+><CR>c/+>/e<CR>

" header for php files
autocmd filetype php  map! hdr; <ESC>ggi<?php<CR><CR>/**<CR><+file+>.php<CR>@author plafayette<CR>@copyright 2009 Refresh Partners<CR>/
                                           
" fbapp 
map! fb; $fbapp->
map! fba; $fbapp->assign(');<ESC>hi
map! fbg; $db = & $fbapp->get_table(DB__ID);<ESC>4hi
map! fbd; $fbapp->display('');<ESC>hhi
map! fbr; $fbapp->redirect($fbapp->get_menu_url(
map! fbu; $fbapp->get_user_id();
map! @pf the application instance
map! @pu the user id
map! scr; <script><CR>{literal}<CR>{/literal}<CR></script><ESC>2ko
map! sty; <style><CR>{literal}<CR>{/literal}<CR></style><ESC>2ko

" db_table
map! db; $db->
map! dbf; $db->set_fields();<ESC>hi
map! dbaf; $db->add_fields();<ESC>hi
map! dbr; $db->set_filter();<ESC>hi
map! dbar; $db->add_filter();<ESC>hi
map! dbl; $db->set_limit();<ESC>hi
map! dbo; $db->set_order();<ESC>hi
map! dbs; $db->select();<ESC>hi
map! dbsf; $db->select_first();<ESC>hi
map! dbd; $db->set_debug();
map! fdb; $db->set_debug_file(SQL_DEBUG_FILE, FILE_ONLY);

" debug
map! pld; printl(logDEBUG, __FUNCTION__, );<ESC>hi
map! plx; printl(logEXCEPTION, __FUNCTION__, '['. $e->getCode() . '] ' . $e->getMessage());<ESC> 
map! pre; echo '<pre>';<CR>echo '</pre>';<ESC>O
map! vbo; if(VERBOSITY > 1)
map! fbo; if(SQL_DEBUG_TO_FILE) 

" html entities
"map! e` &egrave;
"map! E` &Egrave;
"map! e/ &eacute;
"map! E/ &Eacute;
"map! e] &ecirc;
"map! E] &Ecirc;
"map! i] &icirc;
"map! cc, &ccedil;
"map! CC, &Ccedil;
"map! a` &agrave;
"map! A` &Agrave;
"map! a] &acirc;
"map! o] &ocirc;
"map! << &laquo;
"map! >> &raquo;        
