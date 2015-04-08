__author__ = 'Taio'

import ConfigParser

config_file = ConfigParser.RawConfigParser(allow_no_value=True)
# config_file.read(file_path('etc/pytables.conf'))
config_file.read('etc/pytables.conf')

assert config_file.get('DEFAULT', 'host') == '192.168.20.10'
assert config_file.get('DEFAULT', 'exchange') == 'ip_exchange'
assert config_file.get('DEFAULT', 'log_level') == 'logging.DEBUG'