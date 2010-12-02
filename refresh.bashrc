# refresh.bashrc
#
# $Author$
# $Date$
# $Revision$   
# vi:set ft=sh fdm=marker sw=4 ts=4:

#-------- Refresh Project Servers --------#  {{{1

alias rapps='pd /var/www/virtual/refreshpartners.com/apps/htdocs/'
alias eastern='ssh root@10.10.12.100'
alias smysql='net stop mysql'
alias shttpd='kill -TERM `cat /var/run/httpd.pid`' # stop httpd service
alias refresh='ssh vu2031p@apps.refreshpartners.com' # refresh server
alias nrefresh='ssh pierre@66.46.177.186' # new refresh server
alias rogers='ssh defirogers@207.107.237.118'      # le defi compte sur tes amis
alias flipcup='ssh 99b642c2@99b642c2.fb.joyent.us' # flip cup on joyent
alias demojoy='ssh 9b4600a6@8.17.172.56' # refresh analytics on joyent 
alias grgjoy='ssh 992402e2@992402e2.fb.joyent.us' # get real gifts on joyent
alias beelya='ssh mfaggian@67.192.124.88' # beelya server
alias zoojoy='ssh fjq6yraa@fjq6yraa.joyent.us' # zoocasa server
alias babyjoy='ssh cpbadmin_dev@gnnucfaa.joyent.us' # babymaker server
alias facialjoy='ssh refresh@72.2.118.52' # facial grab server
alias nrefresh='ssh pierre@apps3.refreshpartners.com' # new refresh server

#-------- Refresh Projects Directories --------#  {{{1

alias 83things="83ways"
alias 83ways="pd ~/83things"
alias beta="pd ~/beelya_beta"
alias brand="pd ~/brand5"
alias demographics="pd ~/demographics"
alias ford="pd ~/forddsl"
alias friends="pd ~/friendsgive/web"
alias phpsh="~/phpsh/phpsh"
alias slang="pd ~/slangbook"
alias socialads="pd ~/socialdoughads"
alias social="pd ~/socialdough"
alias tes_amis="pd ~/tes_amis"
alias wyr="pd ~/whodyourather"
alias zoo="pd ~/zoocasa"
alias burger="pd ~/pollarizer"
alias baby="pd ~/babymaker"
alias delib="pd ~/fb_deliberator"
alias smart="pd ~/smarties_colour"
 
