srpm:
	dnf -y install rpmdevtools fedpkg
	spectool -g higan.spec
	fedpkg --release=f28 srpm
	cp *.src.rpm $(outdir)
