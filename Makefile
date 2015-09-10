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
PERL_VERSION	= 5.22.0
MYPERL_RELEASE	= 1
PERL_TARBALL	= perl-$(PERL_VERSION).tar.bz2
SRCDIR			= perl-$(PERL_VERSION)
MYPERL_DEBIAN	= debian
MYPERL_NAME		= myperl
MYPERL_VERS     = $(PERL_VERSION).$(MYPERL_RELEASE)
MYPERL			= /opt/myperl/bin/perl
MYPROVE			= /opt/myperl/bin/prove

TT_VERSION_SYMBOLS = \
					 --define PERL_VERSION="$(PERL_VERSION)" \
					 --define MYPERL_RELEASE="$(MYPERL_RELEASE)"

############################################################
# Debian Variables
############################################################

DEB_PKG			= $(MYPERL_NAME)_$(MYPERL_VERS)_amd64.deb
DEB_MYPERL_TARBALL  = $(MYPERL_NAME)_$(MYPERL_VERS).orig.tar.bz2

############################################################
# SuSE Variables
############################################################

SUSE_PKG		= $(HOME)/rpmbuild/RPMS/x86_64/$(MYPERL_NAME)-$(PERL_VERSION)-$(MYPERL_RELEASE).x86_64.rpm

-include Makefile.local

############################################################
# Generic Targets
############################################################

.PHONY: suse-ver-string fetch-perl clean test

suse-ver-string:
	@echo "$(PERL_VERSION)-$(MYPERL_RELEASE)"

fetch-perl: $(PERL_TARBALL)

$(PERL_TARBALL):
	wget -O $@ $(PERL_SRCBASE)/$(PERL_TARBALL)

fetch-cpanm: cpanm

cpanm:
	wget -O $@ \
		https://raw.githubusercontent.com/miyagawa/cpanminus/master/cpanm
	chmod 0755 $@

clean:
	rm -rf $(SRCDIR)

# Note: this currently defaults to debian because that's what we
# do our travis-ci on.
test: debian-test

.SUFFIXES: .template

%:: %.template
	cat $< | tpage $(TT_VERSION_SYMBOLS) $(TT_EXTRA_SYMBOLS) >$@

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
	$(SUDO) dpkg -i $(DEB_PKG)

debian-test:
	$(MYPROVE)

############################################################
# SuSE Targets
############################################################

suse: $(SUSE_PKG)

$(SUSE_PKG): myperl.spec \
		$(HOME)/rpmbuild/SOURCES/$(PERL_TARBALL) \
		$(HOME)/rpmbuild/SOURCES/cpanm
	rpmbuild -bb $<

$(HOME)/rpmbuild/SOURCES/$(PERL_TARBALL): $(PERL_TARBALL)
	cp -a $< $@

$(HOME)/rpmbuild/SOURCES/cpanm: cpanm
	cp -a $< $@

suse-install: $(SUSE_PKG)
	$(SUDO) rpm -ivh $(SUSE_PKG)

suse-clean:
	rm -rf $(SUSE_PKG)
