服务器远程登录和拷贝
scp -i /Users/Dench/Downloads/PythonTools/AliServerSSHKey.pem root@106.14.127.27:/root/icon01.jpg icon01.jpg
scp -i /Users/Dench/Downloads/PythonTools/AliServerSSHKey.pem icon01.jpg root@106.14.127.27:/root/icon01.jpg
ssh -i /Users/Dench/Downloads/PythonTools/AliServerSSHKey.pem root@106.14.127.27

supervisor 配置和启动
/etc/supervisor/conf.d/ 配置 flask-server.conf
chmod -R  a+x /src
supervisorctl reload

supervisorctl start flask-server
supervisorctl stop flask-server

nginx 配置和启动
/etc/nginx/sites-available/ 配置 flask-server
/etc/nginx/sites-enabled 创建软链接
ln -s /etc/nginx/sites-available/flask-server

/etc/init.d/nginx reload
/etc/init.d/nginx restart

nginx -s reload
nginx -s quit
nginx -s stop
nginx -s reopen
ps -ax | grep nginx
nginx -t -c /etc/nginx/nginx.conf

测试连接和端口
curl http://106.14.127.27/

netstat -ntlp | grep 9000
netstat -tap | grep mysql
