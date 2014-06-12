#
# Makefile for myperl
#
# TARGETS:
#
#  myperl		Builds the myperl debian package
#

PERL_TARBALL	= perl-5.18.2.tar.bz2
SRCDIR			= perl-5.18.2
MYPERL_DEBIAN	= myperl-debian
MYPERL_NAME		= myperl_5.18.2+1
DEB_PKG			= $(MYPERL_NAME)-1_amd64.deb

.PHONY: myperl

myperl: $(DEB_PKG)

$(DEB_PKG):
	# unpack Perl tarball
	tar xjf $(PERL_TARBALL)
	# copy over the debian/ stuff
	tar cf - -C $(MYPERL_DEBIAN) . | tar xf - -C $(SRCDIR)
	# build the package
	cd $(SRCDIR) && dpkg-buildpackage -us -uc


