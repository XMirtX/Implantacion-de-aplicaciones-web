from fabric.api import env, dc, local, run

# nombre de la maquina de producción
env.hosts = ["cloud"]
# env.user
# env.password


def deploy():
	local("git push")
	with cd("~/myweb_db"):
	run("git pull")
	run("supervisorctl restart myweb")
