" general.vim
"
" $Author$
" $Date$
" $Revision$ 
"
 
" Plugin Settings {{{1
" taglist.vim: shows ctags list {{{2
let Tlist_Inc_Winwidth = 1
let Tlist_Exit_OnlyWindow = 1
let Tlist_File_Fold_Auto_Close = 1
let Tlist_Process_File_Always = 1
let Tlist_Enable_Fold_Column = 0
let Tlist_GainFocus_On_ToggleOpen = 1 

" NERD_tree.vim: place directory tree on the right {{{2
let g:NERDTreeWinPos = 'right'

" snippetsEmu {{{2
if exists('loaded_snippet')
	imap <C-B> <Plug>Jumper
endif

" php-doc.vim - global settings {{{2
let g:pdv_cfg_Type = "mixed"
let g:pdv_cfg_Package = ""
let g:pdv_cfg_Version = "$id$"
let g:pdv_cfg_Author = "plafayette"
let g:pdv_cfg_Copyright = "Refresh Partners 2009"
let g:pdv_cfg_License = "" 

" FuzzyFinder Textmate {{{2
let g:fuzzy_ignore = "*.log"
let g:fuzzy_matching_limit = 70

map <leader>t :FuzzyFinderTextMate<CR>
map <leader>b :FuzzyFinderBuffer<CR>


" Autocmds {{{1
" SQL DDL maps {{{2
augroup ddl
	autocmd!
	autocmd filetype sql,mysql map! id; id<TAB><TAB><TAB><TAB>INTEGER NOT NULL AUTO_INCREMENT,
	autocmd filetype sql,mysql map! in; INTEGER NOT NULL,
	autocmd filetype sql,mysql map! da; DATETIME NOT NULL,
	autocmd filetype sql,mysql map! bi; BIGINT() NOT NULL,<ESC>3ba
	autocmd filetype sql,mysql map! ti; TINYINT() NOT NULL,<ESC>3ba
	autocmd filetype sql,mysql map! vc; VARCHAR() NOT NULL,<ESC>3ba
	autocmd filetype sql,mysql map! ch; CHAR() NOT NULL,<ESC>3ba
	autocmd filetype sql,mysql map! nn; NOT NULL,
	autocmd filetype sql,mysql map! ai; AUTO_INCREMENT,
	autocmd filetype sql,mysql map! ct; CREATE TABLE
	autocmd filetype sql,mysql map! pk; PRIMARY KEY (),<ESC>hi
	autocmd filetype sql,mysql map! io; INDEX (),<ESC>hi
	autocmd filetype sql,mysql map! fk; FOREIGN KEY REFERENCES 
augroup END 

" ruby on rails setup {{{2
augroup rails
	autocmd!
	" autoindent with two spaces, always expand tabs
	autocmd FileType ruby,eruby,yaml set ai sw=2 sts=2 et
    " omnicompletion with rubycomplete.vim 
    autocmd FileType ruby,eruby set omnifunc=rubycomplete#Complete
    autocmd FileType ruby,eruby let g:rubycomplete_buffer_loading = 1
    autocmd FileType ruby,eruby let g:rubycomplete_rails = 1
    autocmd FileType ruby,eruby let g:rubycomplete_classes_in_global = 1
augroup END 

" Modeline {{{1
" vim:set fdm=marker sw=4 ts=4:
