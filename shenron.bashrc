# shenron.bashrc
#
# $Author$
# $Date$
# $Revision$    

#-------- Environment Variables --------# {{{1
export PYTHONPATH=$HOME/lib/python2.5/site-packages

#--------- Aliases --------# {{{1

alias doc="pd \"c:/Users/pierre/Documents\""
alias gvim="\"c:/Program Files/vim/vim73/gvim.exe\""
alias htdocs="pd \"c:/Program Files/Apache Software Foundation/Apache2.2/htdocs\"" 
alias myip='c:/windows/system32/ipconfig | grep "IP Address" | awk "{ print \$15 }"'
alias phpsh="/cygdrive/c/Program\ Files/PHP/phpsh/phpsh"  
alias nbeauty="beautify.py -f ' ' -t '_' -L -n "
alias beauty="beautify.py -f ' ' -t '_' -L " 
alias lint="python /cygdrive/c/bin/depot_tools/cpplint.py $1"  

#-------- MP3 utilities --------# {{{1

# creates playlist from album dir {{{2
alias cpl="Tag --oneplaylist *.mp3"

# Command line Winamp {{{2
alias play="clamp /loadplay *.m3u; clear; clamp /title"
alias start="clamp /play; clear; clamp /title"
alias stop="clamp /stop ; clear; clamp /status"
alias pause="clamp /pause; clear; clamp /status"
alias next="clamp /next; clear; clamp /title"
alias prev="clamp /prev; clear; clamp /title"

function track() # usage: track [num] 
{
    clamp /plset "$1" /play; clamp /title
}

# Modeline {{{1
# vi:set ft=sh fdm=marker sw=4 ts=4:
