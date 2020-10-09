# comment out ULIMIT in /etc/default/nginx and restart service
exec {'ulimit':
  command => "/bin/sed -i '/^ULIMIT/s/^/#/' /etc/default/nginx ; /usr/sbin/service restart nginx",
  }
