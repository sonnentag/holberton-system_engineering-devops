# uncomment/add ULIMIT in /etc/default/nginx and reload service
exec {'ulimit':
  command => "sed -i '/^#ULIMIT/s/^#//' /etc/default/nginx &&
              systemctl restart nginx",
  path    => '/bin'
  }
