#
# Makefile for myperl
#
# TARGETS:
#
#  fetch-perl	Fetches Perl tarball
#
#  debian		Builds the myperl debian package
#

PERL_SRCBASE	= http://ftp.gwdg.de/pub/languages/perl/CPAN/src/5.0
PERL_VERSION	= 5.20.0
PERL_TARBALL	= perl-$(PERL_VERSION).tar.bz2
SRCDIR			= perl-$(PERL_VERSION)
MYPERL_DEBIAN	= debian
MYPERL_NAME		= myperl
MYPERL_VERS     = $(PERL_VERSION)+1
MYPERL			= /opt/myperl/bin/perl
MYPROVE			= /opt/myperl/bin/prove

############################################################
# Debian Variables
############################################################

DEB_PKG			= $(MYPERL_NAME)_$(MYPERL_VERS)_amd64.deb
DEB_MYPERL_TARBALL  = $(MYPERL_NAME)_$(MYPERL_VERS).orig.tar.bz2

############################################################
# SuSE Variables
############################################################

SUSE_PKG		= $(MYPERL_NAME)-$(PERL_VERSION)-1.x86_64.rpm

-include Makefile.local

############################################################
# Generic Targets
############################################################

.PHONY: fetch-perl clean test

fetch-perl: $(PERL_TARBALL)

$(PERL_TARBALL):
	wget -O $@ $(PERL_SRCBASE)/$(PERL_TARBALL)

clean:
	rm -rf $(SRCDIR)

# Note: this currently defaults to debian because that's what we
# do our travis-ci on.
test: debian-test

############################################################
# Debian Targets
############################################################

.PHONY: debian debian-clean debian-install debian-test

debian: $(DEB_PKG)

$(DEB_MYPERL_TARBALL): $(PERL_TARBALL)
	cp --archive $< $@

$(DEB_PKG): $(DEB_MYPERL_TARBALL)
	# unpack Perl tarball
	tar xjf $(PERL_TARBALL)
	# copy over the debian/ stuff
	tar cf -  debian | tar xf - -C $(SRCDIR)
	# update changelog
	cd $(SRCDIR) && debchange --create --package $(MYPERL_NAME) --newversion $(MYPERL_VERS) autobuild
	# build the package
	cd $(SRCDIR) && dpkg-buildpackage -us -uc

debian-clean: clean
	rm -rf $(DEB_PKG) \
		$(DEB_MYPERL_TARBALL) \
		$(MYPERL_NAME)_$(MYPERL_VERS).debian.tar.gz \
	    $(MYPERL_NAME)_$(MYPERL_VERS).dsc \
		perl-$(MYPERL_VERS)

debian-install: $(DEB_PKG)
	sudo dpkg -i $(DEB_PKG)

debian-test:
	$(MYPROVE)

############################################################
# SuSE Targets
############################################################

suse: $(SUSE_PKG)

$(SUSE_PKG): myperl.spec $(HOME)/rpmbuild/SOURCES/$(PERL_TARBALL)
	rpmbuild -bb $<
	mv $(HOME)/rpmbuild/RPMS/x86_64/$(SUSE_PKG) .

$(HOME)/rpmbuild/SOURCES/$(PERL_TARBALL): $(PERL_TARBALL)
	cp -a $< $@

