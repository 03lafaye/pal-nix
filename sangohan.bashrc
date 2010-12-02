# sangohan.bashrc
#
# $Author$
# $Date$
# $Revision$   

#-------- Environment Variables --------# {{{1
export JDK_HOME="/usr/lib/jvm/java-6-openjdk"

# turn on touchpad!
alias touch="sudo modprobe psmouse proto=imps"

#-------- Aliases --------# {{{1"
alias tomstop="sudo /etc/init.d/tomcat6 stop"
alias tomstart="sudo /etc/init.d/tomcat6 start"
alias tomhome="pd /var/lib/tomcat6/"

# project dirs {{{2
alias ph="pd ~/Projects"
alias pTrain="pd ~/Projects/rails/pTrainer"

# Make touchpad work {{{2
alias tpad="sudo modprobe psmouse proto=imps"

# {{{1 Modeline 
# vim:ft=sh:fdm=marker:sw=4:ts=4: 
