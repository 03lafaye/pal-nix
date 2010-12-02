# sangoten.bashrc
#
# $Author$
# $Date$
# $Revision$   

# Environment Variables {{{1
export ANT_HOME="/usr/share/ant"
export ANT_OPTS="-Xmx192M"
export PATH="$PATH:$ANT_HOME/bin"
export JAVA_HOME="C:/IBM/WebSphere/AppServer/java"
export JAVA_TRUNK="C:/JavaTrunk/source/Java/"
export BC="C:/BC"

# Aliases {{{1 

# My Documents {{{2
alias docs="pd \"C:/Documents and Settings/plafayette/My Documents\""
 
# htdocs {{{2
alias htdocs="pd \"C:/Program Files/Apache Software Foundation/Apache2.2/htdocs\""

# Java BeanShell {{{2
alias bsh="pd ~/; java -jar scripts/bsh-core-2.0b4.jar" 

# Jonah Group CVS {{{2
alias cvsroot="pd \"C:/Documents and Settings/plafayette/My Documents/cvs.jonahgroup.com\""

# BC SVN Java trunk {{{2
alias javatrunk="pd $JAVA_TRUNK"

# Script corner {{{2
alias scorner="pd /cygdrive/c/BC/source/utility/"
alias python="/cygdrive/c/BC/thirdParty/Python25/python.exe"

# David Chang's SuperDeployX {{{3
alias superdeploy="python \"c:\BC\source\utility\superDeployX.py\" -p --ide=idea --webAppOnly default \"C:\JavaTrunk\source\Java\""

# Oracle Admin folder {{{2
alias oradmin="pd /cygdrive/c/oracle/product/10.2.0/client_2/NETWORK/ADMIN"

# WebSphere logs {{{2
alias weblog="pd /cygdrive/c/IBM/WebSphere/AppServer/profiles/default/logs/server1"
 
# WAS Server {{{2
alias was="ssh was@jonah-dev06"

# NPS virgination scripts {{{2
alias virgin="pd /cygdrive/c/BC/source/schema/NpsUtilityScripts"

# @param $1 DB SID
function virginate()
{
    virgin # move to script directory
    logfile="logs/${1}_virgination_$(date +%Y-%m-%d_%H-%-M-%S).log"
    exit | sqlplus "dev1/bc@${1}" @prepare_initial_nps_run.sql > $logfile
    cat $logfile
}

# Modeline {{{1 
# vim:ft=sh:fdm=marker:sw=4:ts=4:
