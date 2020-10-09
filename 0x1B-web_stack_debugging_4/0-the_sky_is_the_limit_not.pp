# uncomment/add ULIMIT in /etc/default/nginx and reload service
exec {'ulimit':
  command => "/bin/sed -i '/^ULIMIT/s/^/#/' /etc/default/nginx ; /bin/systemctl restart nginx",
  }
