from src.base import SourceLocation, Target

SourceLocation(
	name = 'sby',
	vcs = 'git',
	location = 'https://github.com/YosysHQ/SymbiYosys',
	revision = 'origin/master'
)

Target(
	name = 'sby',
	sources = [ 'sby' ],
	resources = [ 'python3' ],
	license_file = 'sby/COPYING',
)

SourceLocation(
	name = 'sby-gui',
	vcs = 'git',
	location = 'https://github.com/YosysHQ/sby-gui',
	revision = 'origin/master'
)

Target(
	name = 'sby-gui',
	sources = [ 'sby-gui' ],
	license_file = 'sby-gui/COPYING',
)
