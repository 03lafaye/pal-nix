# external.bashrc
#
# $Author$
# $Date$
# $Revision$  
# vi:set ft=sh fdm=marker sw=4 ts=4:

#-------- Source global definitions --------# {{{1

if [ -f /etc/bashrc ]; then
. /etc/bashrc
fi

export SHELL=/bin/bash
export PATH=".:/usr/sbin/:~/share/bin:$PATH"
export EDITOR="vim"

set -o notify
set -o noclobber
set -o ignoreeof
set -o nounset

if [ ! -n "${TERM}" ]; then
	TERM=cygwin
fi

#-------- Aliases --------#  {{{1

alias h="pd ~"  # go home
alias c="clear" # clean up

function pd() # push directory on to stack
{
	pushd "$1" 1> /dev/null
}
alias bk="popd 1> /dev/null" # pop directory from stack

# The 'ls' family
alias ls="ls -F "
alias la="ls -aF"
alias ll="ls -l"
alias lx="ls -lXB" # sort by extension
alias lc="ls -lcr" # sort by change time
alias lr="ls -lR"  # recursive ls
alias lt="ls -ltr" # sort by date
function lm() # last modification date for a file
{
	ll "$*" | awk '{print $6, $7, $8}'
}

alias background="xv -root -quit -max -rmode 5"
alias brc="vi ~/.bashrc"
alias chmodd="find . -type d -print | xargs chmod 775"
alias chmodf="find . -type f -print | xargs chmod 664"
alias crc="vi ~/.mycshrc"
alias df="df -Th"
alias du="du -h"
alias mkdir="mkdir -p" # prevents accidental clobbers
alias path="echo -e ${PBH//:/\\n}"
alias trix="vi ~/unixtricks"
alias vrc="vi ~/.vimrc"
alias vi='vim'

function gmysql()
{
	/usr/bin/mysql -b -D "$1" -u "$2" -p
}
 
#-------- Colors  --------# {{{1

red='\e[0;31m'
RED='\e[1;31m'
blue='\e[0;34m'
BLUE='\e[1;34m'
cyan='\e[0;36m'
CYAN='\e[1;36m'
purple='\e[0;35m'
PURPLE='\e[1;35m'
green='\e[0;32m'
NC='\e[0m' # no color

#-------- Functions --------# {{{1
function _exit()
{
	cd ~
	echo -e "${RED}Adieu!"
}
trap _exit EXIT

#-------- Shell Prompt --------# {{{1

A=${cyan}
B=${purple}
C=${green}

function fastprompt()
{
	unset PROMPT_COMMAND
	case $TERM in
		*term | rxvt )
			PS1="${A}[$HOSTNAME]$NC \W > \[\033]0;\${TERM} [\u@\h] \w\007\]" ;;
		linux )
			PS1="${A}[$HOSTNAME]$NC \W > " ;;
		* )
			PS1="${C}[$HOSTNAME]$NC \W > " ;;
	esac
}
fastprompt
