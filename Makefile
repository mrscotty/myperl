#
# Makefile for myperl
#
# TARGETS:
#
#  fetch-perl	Fetches Perl tarball
#
#  myperl		Builds the myperl debian package
#

PERL_SRCBASE	= http://ftp.gwdg.de/pub/languages/perl/CPAN/src/5.0
PERL_TARBALL	= perl-5.18.2.tar.bz2
SRCDIR			= perl-5.18.2
MYPERL_DEBIAN	= debian
MYPERL_NAME		= myperl
MYPERL_VERS     = 5.18.2+1
DEB_PKG			= $(MYPERL_NAME)_$(MYPERL_VERS)_amd64.deb
MYPERL_TARBALL  = $(MYPERL_NAME)_$(MYPERL_VERS).orig.tar.bz2

-include Makefile.local

.PHONY: fetch-perl myperl myperl-clean clean

fetch-perl: $(PERL_TARBALL)

$(PERL_TARBALL):
	wget -O $@ $(PERL_SRCBASE)/$(PERL_TARBALL)

myperl: $(DEB_PKG)

$(MYPERL_TARBALL): $(PERL_TARBALL)
	cp --archive $< $@

$(DEB_PKG): $(MYPERL_TARBALL)
	# unpack Perl tarball
	tar xjf $(PERL_TARBALL)
	# copy over the debian/ stuff
	tar cf -  debian | tar xf - -C $(SRCDIR)
	# update changelog
	cd $(SRCDIR) && debchange --create --package $(MYPERL_NAME) --newversion $(MYPERL_VERS) autobuild
	# build the package
	cd $(SRCDIR) && dpkg-buildpackage -us -uc

clean:
	rm -rf $(SRCDIR) $(DEB_PKG)

realclean: clean
	rm -rf $(DEB_PKG) \
		$(MYPERL_TARBALL) \
		$(MYPERL_NAME)_$(MYPERL_VERS).debian.tar.gz \
	    $(MYPERL_NAME)_$(MYPERL_VERS).dsc
