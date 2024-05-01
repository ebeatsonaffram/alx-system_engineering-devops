import fabric
from fabric import run, env, cd, local, settings, sudo

run ("mkdir /tmp.trunk/")

run("ubuntu")

result = run("ls -l /var/www")

result.failed