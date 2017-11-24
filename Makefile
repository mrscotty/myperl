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
PERL_VERSION	= 5.26.0
MYPERL_RELEASE	= 1
PERL_TARBALL	= perl-$(PERL_VERSION).tar.bz2
SRCDIR			= perl-$(PERL_VERSION)
MYPERL_DEBIAN	= debian
MYPERL_NAME		= myperl
MYPERL_VERS     = $(PERL_VERSION)
MYPERL			= /opt/myperl/bin/perl
MYPROVE			= /opt/myperl/bin/prove
export PERL_VERSION
export MYPERL_RELEASE

TT_VERSION_SYMBOLS = \
					 --define PERL_VERSION="$(PERL_VERSION)" \
					 --define MYPERL_RELEASE="$(MYPERL_RELEASE)"

ifeq "$(SRCDIR)" "/"
	$(error Let us not go to far with this)
endif

############################################################
# Debian Variables
############################################################

DEB_PKG			= $(MYPERL_NAME)_$(MYPERL_VERS)-$(MYPERL_RELEASE)_amd64.deb
DEB_MYPERL_TARBALL  = $(MYPERL_NAME)_$(MYPERL_VERS).orig.tar.bz2

############################################################
# SuSE Variables
############################################################

SUSE_PKG		= $(HOME)/rpmbuild/RPMS/x86_64/$(MYPERL_NAME)-$(PERL_VERSION)-$(MYPERL_RELEASE).x86_64.rpm

-include Makefile.local

############################################################
# Generic Targets
############################################################

.PHONY: perl-ver-string suse-ver-string myperl-release myperl-deb-release fetch-perl clean test

perl-ver-string:
	@echo "$(PERL_VERSION)"

suse-ver-string debian-ver-string:
	@echo "$(PERL_VERSION)-$(MYPERL_RELEASE)"

myperl-release:
	@echo "$(MYPERL_RELEASE)"

myperl-deb-release:
	@echo "$(MYPERL_RELEASE)"

fetch-perl: $(PERL_TARBALL)

$(PERL_TARBALL):
	wget -O $@ $(PERL_SRCBASE)/$(PERL_TARBALL)

fetch-cpanm: cpanm

cpanm:
	wget -O $@.new --no-check-certificate \
		https://raw.githubusercontent.com/miyagawa/cpanminus/master/cpanm
	chmod 0755 $@.new
	mv $@.new $@

clean:
	rm -rf $(SRCDIR) myperl.spec

# Note: this currently defaults to debian because that's what we
# do our travis-ci on.
test: debian-test

.SUFFIXES: .template

%:: %.template Makefile
	cat $< | tpage $(TT_VERSION_SYMBOLS) $(TT_EXTRA_SYMBOLS) >$@

############################################################
# Debian Targets
#
# For information on Debian packaging, see:
#
# 	https://wiki.debian.org/IntroDebianPackaging
#
############################################################

.PHONY: debian debian-clean debian-install debian-test

debian: $(DEB_PKG)

# This is "Step 1" in the debian packaging intro
$(DEB_MYPERL_TARBALL): $(PERL_TARBALL)
	cp --archive $< $@

$(DEB_PKG): $(DEB_MYPERL_TARBALL) $(shell find debian -type f)
	# delete previous build, if exists
	rm -rf $(SRCDIR)
	# unpack Perl tarball ("Step 2" of the debian packaging intro)
	tar xjf $(DEB_MYPERL_TARBALL)
	# BEGIN "Step 3" of the debian packaging intro...
	tar cf -  debian | tar xf - -C $(SRCDIR)
	# update changelog
	cd $(SRCDIR) && debchange --create --package $(MYPERL_NAME) --newversion $(MYPERL_VERS)-$(MYPERL_RELEASE) autobuild
	# according to docs, this should be '9'
	echo "9" > debian/compat
	# END "Step 3"
	# build the package
	cd $(SRCDIR) && dpkg-buildpackage -us -uc

debian-clean: clean
	rm -rf $(DEB_PKG) \
		$(DEB_MYPERL_TARBALL) \
		$(MYPERL_NAME)_$(MYPERL_VERS)-$(MYPERL_RELEASE).debian.tar.gz \
	    $(MYPERL_NAME)_$(MYPERL_VERS)-$(MYPERL_RELEASE).dsc \
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


############################################################
# Open Build SuSE
############################################################

obs: myperl.spec myperl-buildtools.spec myperl-dbi.spec myperl-fcgi.spec myperl-dbd-mysql.spec myperl-dbd-oracle.spec

myperl-buildtools.spec: package/suse/myperl-buildtools/myperl-buildtools.spec
	cp -a $< $@

package/suse/myperl-buildtools/myperl-buildtools.spec: package/suse/myperl-buildtools/myperl-buildtools.spec.template
	cd package/suse/myperl-buildtools && \
		make STATIC_TARBALLS=1 myperl-buildtools.spec

myperl-dbi.spec: package/suse/myperl-dbi/myperl-dbi.spec
	cp -a $< $@

package/suse/myperl-dbi/myperl-dbi.spec: package/suse/myperl-dbi/myperl-dbi.spec.template
	cd package/suse/myperl-dbi && \
		make STATIC_TARBALLS=1 myperl-dbi.spec

myperl-fcgi.spec: package/suse/myperl-fcgi/myperl-fcgi.spec
	cp -a $< $@

package/suse/myperl-fcgi/myperl-fcgi.spec: package/suse/myperl-fcgi/myperl-fcgi.spec.template
	cd package/suse/myperl-fcgi && \
		make STATIC_TARBALLS=1 myperl-fcgi.spec

myperl-dbd-mysql.spec: package/suse/myperl-dbd-mysql/myperl-dbd-mysql.spec
	cp -a $< $@

package/suse/myperl-dbd-mysql/myperl-dbd-mysql.spec: package/suse/myperl-dbd-mysql/myperl-dbd-mysql.spec.template
	cd package/suse/myperl-dbd-mysql && \
		make STATIC_TARBALLS=1 myperl-dbd-mysql.spec

myperl-dbd-oracle.spec: package/suse/myperl-dbd-oracle/myperl-dbd-oracle.spec
	cp -a $< $@

package/suse/myperl-dbd-oracle/myperl-dbd-oracle.spec: package/suse/myperl-dbd-oracle/myperl-dbd-oracle.spec.template
	cd package/suse/myperl-dbd-oracle && \
		STATIC_TARBALLS=1 make myperl-dbd-oracle.spec


