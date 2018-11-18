docker stop nginx
docker rm nginx
docker run \
--name nginx \
-v /home/roby/alpha/nginx/nginx.conf:/etc/nginx/nginx.conf \
-v /home/roby/alpha/nginx/logs:/logs \
-v /home/roby/alpha/nginx/web:/web \
-v /home/roby/alpha/nginx/certificate:/certificate \
-v /home/roby/alpha:/alpha \
-d -p 80:80 -p 443:443 -p 6688:6688 -p 8080:8080 nginx
