# uncomment/add ULIMIT in /etc/default/nginx and reload service
exec {'ulimit':
  command => "sed -i '/^#ULIMIT.*4096/s/^#//' /etc/default/nginx;
              grep -q ^ULIMIT.*4096 /etc/default/nginx ||
              echo 'ULIMIT=\"-n 4096\"' >> /etc/default/nginx &&
              systemctl restart nginx",
  path    => ['/bin', '/usr/bin']
  }
