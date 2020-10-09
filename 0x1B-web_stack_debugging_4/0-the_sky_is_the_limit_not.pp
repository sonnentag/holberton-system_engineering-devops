# comment out ULIMIT in /etc/default/nginx and restart service
exec {'ulimit':
  command => "/bin/sed -i '/worker_processes/s/ 4;$/ 1024;/' /etc/nginx/nginx.conf ; /usr/sbin/service restart nginx",
  }
