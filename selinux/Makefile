all: build install clean relabel

build:
	make -f /usr/share/selinux/devel/Makefile persistent-evdev.pp

install:
	semodule -i persistent-evdev.pp

relabel:
	restorecon -F -r -v /opt/persistent-evdev /var/cache/persistent-evdev

clean:
	rm -Rf persistent-evdev.pp tmp/
