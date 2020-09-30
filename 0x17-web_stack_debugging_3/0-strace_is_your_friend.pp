# fix typo in settings file
exec { 'locale_file':
  command => '/bin/sed -i "s.phpp.php." /var/www/html/wp-settings.php'
}
