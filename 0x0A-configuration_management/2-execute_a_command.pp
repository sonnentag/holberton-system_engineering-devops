# kill a process named killmenow

exec { 'pkill':
    path    => '/usr/bin:/usr/sbin:/bin',
    command => 'pkill -f killmenow'
}
