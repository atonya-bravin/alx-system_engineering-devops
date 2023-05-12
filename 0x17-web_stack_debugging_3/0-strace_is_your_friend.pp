# when using strace, we found that the error was that there was a file being
# called with the path: /var/www/html/wp-includes/class-wp-locale.phpp
# This file is however not present. Using, grep -rl class-wp-locale.phpp * 
# we find out that the file is being called in the 
# following file: /var/www/html/wp-includes/wp-settings.php
# on checking whether /var/www/html/wp-includes/class-wp-locale.php exists
# using ls class-wp-locale.php we find out that it exists.
# This script therefore changes class-wp-locale.phpp to class-wp-locale.php 
# in wp-settings.php

$file_pth = '/var/www/html/wp-settings.php'
exec{ 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_pth}",
  path    => ['/bin','/usr/bin']
}
