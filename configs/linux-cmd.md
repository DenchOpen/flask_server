
scp -i /Users/Dench/Downloads/PythonTools/AliServerSSHKey.pem root@106.14.127.27:/root/source/awesome/www/001.jpg 001.jpg

scp -i /Users/Dench/Downloads/PythonTools/AliServerSSHKey.pem 001.jpg root@106.14.127.27:/root/source/awesome/www/001.jpg

ssh -i /Users/Dench/Downloads/PythonTools/AliServerSSHKey.pem root@106.14.127.27

ssh -i /Users/dench/Downloads/AliServerSSHKey.pem root@106.14.127.27

scp -i /Users/dench/Downloads/AliServerSSHKey.pem flaskserver.zip root@106.14.127.27:/usr/flaskserver.zip


supervisorctl stop awesome
supervisorctl start awesome
/etc/init.d/nginx reload

/etc/nginx/sites-available/
curl http://106.14.127.27/

netstat -ntlp | grep 9000
netstat -tap | grep mysql


nginx -s reload
nginx -s quit
nginx -s stop
nginx -s reopen
ps -ax | grep nginx
nginx -t -c /etc/nginx/nginx.conf

/etc/init.d/nginx reload
/etc/init.d/nginx restart
python3 /root/source/awesome/www/app.py
