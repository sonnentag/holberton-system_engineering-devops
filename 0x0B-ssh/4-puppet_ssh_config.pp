ini_setting { 'ssh config host':
  ensure	      => present,
  path		      => '/etc/ssh/ssh_config',
  section	      => 'Host *',
  section_prefix      => '',
  section_suffix      => '',
  key_value_separator => ' ',
  setting	      => 'PasswordAuthentication',
  value		      => 'no',
  setting	      => 'IdentityFile',
  value		      => '~/.ssh/holberton',
}
