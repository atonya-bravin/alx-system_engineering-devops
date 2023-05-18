# change the ULIMIT of the nginx server
$file_path = '/etc/default/nginx'
exec { 'change_limit':
  command => "/bin/sed -i ${file_path} -e 's/15/4096/'"
}

exec { 'restart nginx':
  command => '/usr/sbin/service nginx restart',
  require => Exec['change_limit']
}
