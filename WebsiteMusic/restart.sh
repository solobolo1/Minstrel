sudo setenforce 0
sudo systemctl restart nginx
sudo supervisorctl stop all
sudo supervisorctl start all
sudo supervisorctl reload

