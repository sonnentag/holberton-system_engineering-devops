# remove restriction causing errors for holberton user
exec {'nolimits':
  command => "sed -i '/holberton/s/^/#/g' /etc/security/limits.conf",
  path    => '/bin'
  }
