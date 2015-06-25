class { 'neutron::server':
  enabled          => false,
  package_ensure   => 'absent',
  auth_type        => 'noauth'
}

class { 'neutron':
  enabled        => false,
  package_ensure => 'absent'
}

