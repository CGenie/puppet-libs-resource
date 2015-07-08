$resource = hiera('{{ resource_name }}')

$ip = $resource['input']['ip']['value']

$rabbitmq_user = $resource['input']['rabbitmq_user']['value']
$rabbitmq_password = $resource['input']['rabbitmq_password']['value']
$rabbitmq_host = $resource['input']['rabbitmq_host']['value']
$rabbitmq_port = $resource['input']['rabbitmq_port']['value']

$keystone_host = $resource['input']['keystone_host']['value']
$keystone_port = $resource['input']['keystone_port']['value']
$keystone_user = $resource['input']['keystone_user']['value']
$keystone_password = $resource['input']['keystone_password']['value']
$keystone_tenant = $resource['input']['keystone_tenant']['value']

class { 'nova::network':
  ensure_package  => 'present'
}

#file { '/etc/nova/nova-exports':
#  owner     => 'root',
#  group     => 'root',
#  content   => template('nova/exports.erb')
#}
