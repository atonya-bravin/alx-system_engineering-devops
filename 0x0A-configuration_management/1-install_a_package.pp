# Install a package using Puppet

exec { 'install pip':
  command => '/usr/bin/apt-get install -y pip'
}

exec { 'install flask':
  command => '/usr/bin/pip install flask -v 2.1.0'
}

package { 'pip':
  ensure => 'installed',
  before => Exec['install pip']
}

package { 'flask':
  ensure  => 'installed',
  before  => Exec['install flask'],
  require => Package['pip']
}
