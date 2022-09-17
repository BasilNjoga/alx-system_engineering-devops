node default {

file { '/tmp/school' 
	ensure => '/tmp/school'
	source_permissions => '0744'
	owner => 'www-data'
	group => 'www-data'
	content => 'I love Puppet'
	}
}
