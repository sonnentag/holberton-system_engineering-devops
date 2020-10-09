# comment out ULIMIT in /etc/default/nginx and restart service
exec { 'remove ulimit' :
  command  => "/bin/sed -i '/^ULIMIT/s/^/#/' /etc/nginx/nginx.conf ; /usr/sbin/service restart nginx",
  provider => 'shell',
  }
