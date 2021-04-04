# Make some change
file_line { 'Turn of passwd':
	  ensure => 'present',
	  path 	 => '/etc/ssh/ssh_config',
	  line	 => '	PasswordAuthentication no'
}
file_line { 'Declare identity file':
	  ensure => 'present',
	  path	 => '/etc/ssh/ssh_config',
	  line	 => '	IdentifyFile ~/.ssh/holberton'
}
