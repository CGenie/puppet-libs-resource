$resource = hiera('{{ name }}')
$rabbitmq_user = $resource['input']['rabbitmq_user']['value']
$rabbitmq_password = $resource['input']['rabbitmq_password']['value']
$rabbitmq_host = $resource['input']['rabbitmq_host']['value']
$rabbitmq_port = $resource['input']['rabbitmq_port']['value']

class { 'neutron':
  debug           => true,
  verbose         => true,
  enabled         => true,
  package_ensure  => 'present',
  auth_strategy   => 'noauth',
  rabbit_user     => $rabbitmq_user,
  rabbit_password => $rabbitmq_password,
  rabbit_host     => $rabbitmq_host,
  rabbit_port     => $rabbitmq_port,
  service_plugins => ['metering']
}

class { 'neutron::server':
  enabled          => true,
  package_ensure   => 'present',
  auth_type        => 'noauth'
}

class { 'neutron::agents::dhcp': }
