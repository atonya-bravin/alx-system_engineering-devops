# change the ULIMIT of the nginx server
$file_pth = '/etc/default/nginx'
exec{ 'change_limit':
  command => "sed -i 's/15/4096/g' ${file_pth}",
  path    => ['/bin','/usr/bin']
}
exec{ 'restart_nginx':
  command => sudo service nginx restart,
  path    => ['/bin','/usr/bin']
}
