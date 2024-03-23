# Using Puppet, install flask from pip3.

package { 'flask':
  insure   => 'installed',
  provider => 'pip3',
}
