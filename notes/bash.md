# Bash and random terminal commands cheatsheet

`sudo !!` - Redo same command as `sudo`

`(leading space) (any command)` - Leading space will not put it into history

`cat file | tee -a log | cat > /dev/null` - Here `tee` intercepts into pipe and logs what was streamed

`sed -i -e "s#OLD_VAL#\${NEW_VAL}#g" file` replacing things in files

`mkdir -p output` makedir only if not exists

Notable or unobvious linux dirs:

- `/bin` - Executbles of all users
- `/dev` - Devices
- `/etc` - Configuration files
- `/opt` - Various software
- `/root` - Homedir of root user
- `/tmp` - Tmp files, will be wiped out after reboot
- `/usr` - Mini file-system, which overrides for user
- `/var` - Mostly log files

What process is listening on which port:

`sudo netstat -tulpn`

Openssl to encryp/decrypt things:

`openssl aes-256-cbc -md md5 -in secrets.yml.crypt -out secrets.yml -d -base64`

`openssl enc -md md5 -aes-256-cbc -in secrets.yml -out secrets.yml.crypt -e -base64`

Network things:

`host somedomain`
