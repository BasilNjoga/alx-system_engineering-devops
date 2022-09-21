#this manifest creates a file in tmp

node default {

file { '/tmp/school':
  ensure             => present
  source_permissions => '0744'
  owner              => 'www-data'
  group              => 'www-data'
  content            => 'I love Puppet'
  }
}
