" .vimrc
" @author Pierre-Antoine LaFayette

" * Initial Configuration * {{{1 "

" Set the location of .vim folder {{{2
set runtimepath=$HOME/pal-nix/.vim,$VIMRUNTIME
" Jump to last cursor position when opening files {{{2
" See |last-position-jump|.
:au BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif

" change directory on open file, buffer switch etc. {{{2
if exists('+autochdir')
  set autochdir
endif

" turn on filetype detection and indentation {{{2
filetype indent plugin on

" set tags file to search in parent directories with tags; {{{2
set tags=tags;

" reload vimrc on update  {{{2
autocmd BufWritePost .vimrc source %

" set folds to look for markers {{{2
:set foldmethod=marker

" automatically save view and reload folds {{{2
"au BufWinLeave * mkview
"au BufWinEnter * silent loadview

" load dictionary files for complete suggestion with Ctrl-n {{{2
set complete+=k
autocmd FileType * exec('set dictionary+=~/vimfiles/dict/' . &filetype)

" Set the shell to load bash {{{2
set shell=bash\ --login

" Templates {{{2
:autocmd BufNewFile *.html 0r $HOME/pal-nix/.vim/templates/skeleton.html

" * User Interface * {{{1 "
" turn on coloring {{{2
if has('syntax')
    syntax on
endif

" gvim color scheme of choice {{{2
if has('gui')
    so $VIMRUNTIME/colors/desert.vim
endif

" turn off annoying bell {{{2
set vb

" set the directory for swp files {{{2
if(isdirectory(expand("$VIMRUNTIME/swp")))
    set dir=$VIMRUNTIME/swp
endif

" have fifty lines of cmdline (etc) history {{{2
set history=50

" have cmdline completion <Tab> (for filenames, help topics, option names) {{{2
" first list the available options and complete the longest common part, then
" have further <Tab>s cycle through the possibilities:
set wildmode=list:longest,full

" use "[RO]" for "[readonly]" to save space in the message line: {{{2
set shortmess+=r

" display current mode and partially typed commands in status line  {{{2
set showmode
set showcmd

" Replace ctags with cscope
set cst

" Text Formatting -- General  {{{2
set autoindent
set backspace=2      "make backspace work normal (indent, eol, start)
set cursorline       "highlight current line
set encoding=utf-8   "set character encoding
set expandtab        "insert spaces instead of tabs
set guioptions-=T    "removes toolbar from gvim
set hl=l:Visual      "use Visual mode's highlighting scheme --much better
set hlsearch         "highlight search terms
set ignorecase       "ignore case in searches --faster this way
set incsearch        "vim will search for text as you type
set laststatus=2     "keep status line showing
set mat=5            "how many tenths of a second to blink matches
set nocompatible     "prevents vim from emulating vi's original bugs
set number           "show line numbers in left margin
set path=$PWD/**     "recursively set the path of the project
set ruler            "ensures each window contains a status line
set shiftround       "indent/outdent to nearest tabstop
set shiftwidth=4     "indent/outdent to by N columns
set showmatch        "causes cursor to jump to bracket match
set smartindent      "makes vim smartly guess indent level
set smartcase        "case insensitive when typing lower case only
set softtabstop=2    "makes vim see multiple space characters as tabstops
set spelllang=en     "set language
set spellsuggest=3   "suggest better spelling
set statusline=[%n]\ %<%.99f\ %h%w%m%r%{exists('*CapsLockStatusline')?CapsLockStatusline():''}%y%=%-16(\ %l,%c-%v\ %)%P
set tabstop=4        "indentation levels every N columns
set virtualedit=all  "allows the cursor to stray beyond defined text
set wildmode=list:longest,full  "autocompletion; default to longest shared prefix
set diffopt+=iwhite  "vimdiff to ignore changes in whitespace

highlight CursorLine guibg=slategray guifg=white ctermbg=blue ctermfg=white

" * Mappings * {{{1 "
" Function keys {{{2
" Don't you always find yourself hitting <F1> instead of <ESC>? {{{3
inoremap <F1> <ESC>
noremap  <F1> <ESC>

" Turn off syntax highlighting {{{3
nnoremap <silent> <F2> :nohlsearch<CR>
inoremap <silent> <F2> <ESC>:nohlsearch<CR>a

" NERD Tree Explorer {{{3
nnoremap <silent> <F3> :NERDTreeToggle<CR>

" Open buffer list {{{3
nnoremap <silent> <F4> :BufExplorerHorizontalSplit<CR>

" Spell check {{{3
nnoremap <silent> <F6> :set spell<CR>

" No spell check {{{3
nnoremap <silent> <F7> :set nospell<CR>

" Refactor curly braces on keyword line {{{3
map <F9> :%s/) \?\n^\s*{/) {/g

" Useful mappings to paste and reformat/reindent {{{2
nnoremap <silent> <ESC>P P'[v']=
nnoremap <silent> <ESC>p P'[v']=

" Remap code completion to Ctrl+Space {{{2
inoremap <Nul> <C-x><C-o>

" Map tab motion to Alt+Left/Right {{{2
map <silent><A-Right> :tabnext<CR>
map <silent><A-Left> :tabprevious<CR>

" Fixing tabs (credit to Damian Conway) {{{2
" Retabbing {{{3
map <silent> TS :set expandtab<CR>:%retab!<CR>
map <silent> TT :set noexpandtab<CR>:%retab!<CR>

" Change the tab spacing to the appropriate number. {{{3
function! NewTabSpacing (newtabsize)
    let was_expanded = &expandtab
    normal TT
    execute "set ts=" . a:newtabsize
    execute "set sw=" . a:newtabsize
    "execute "map F !Gformat -T" . a:newtabsize . " -"
    "execute "map <silent> f !Gformat -T" . a:newtabsize . "<CR>"
    if was_expanded
        normal TS
    endif
endfunction

" Some common tab space sizes. {{{3
map <silent> T@ :call NewTabSpacing(2)<CR>
map <silent> T$ :call NewTabSpacing(4)<CR>

" Format file with autoformat  (credit to Damian Conway) {{{2
" Capitalize to specify options
"nmap          F !Gformat -T4 -
"nmap <silent> f !Gformat -T4<CR>
"vmap          F :!format -T4 -all -
"vmap <silent> f :!format -T4 -all<CR>

" Remove trailing spaces {{{2
nmap <silent> RS :%s/ \+$//g<CR>

" * Scripts * {{{1 "
" Close xml tags with <C-_> {{{2
au Filetype xhtml,html,xml,xsl,erb source $HOME/pal-nix/.vim/scripts/closetag.vim

" Open helptags from index.txt in vertically split window {{{2
" This mapping is still suspect. Needs stabilizing.
au FileType help nnoremap <buffer> <A-]>
    \ :vert belowright split<CR>
    \ :vert resize 75<CR>
    \ :exec("tag ".expand("<cword>"))<CR>

" Modeline {{{1
" vim:set fdm=marker sw=4 ts=4:
