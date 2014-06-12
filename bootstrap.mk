#!/usr/bin/make -f
#
# I used this makefile to 'bootstrap' the initial contents
# of the debian/ directory and used it for initial tests.
#
# I left it here to document the process for the next time I
# am forced to do something strange like this.

GITDIR = /git/myperl
PERL_TARBALL = perl-5.18.2.tar.bz2
SRCDIR=perl-5.18.2
MYPERL_NAME=myperl_5.18.2+1

doit: prep-state build-state

prep: prep-state
prep-state:
	tar xjf $(PERL_TARBALL)
	cd $(SRCDIR) && dh_make -f ../$(PERL_TARBALL) --single \
		--packagename $(MYPERL_NAME) --copyright artistic --yes
	cp $(GITDIR)/control $(SRCDIR)/debian/
	cp $(GITDIR)/rules $(SRCDIR)/debian/
	rm $(SRCDIR)/debian/*.ex $(SRCDIR)/debian/*.EX
	touch $@

build: build-state
build-state:
	cd $(SRCDIR) && dpkg-buildpackage -us -uc
	touch $@

clean:
	rm -rf myperl_* $(SRCDIR) *-state

inst: build-state
	sudo dpkg -i $(MYPERL_NAME)-1_amd64.deb


