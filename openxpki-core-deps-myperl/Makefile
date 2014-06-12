# Makefile for libclass-std-myperl

PERL = /opt/myperl/bin/perl
CPANM = /opt/myperl/bin/cpanm
COREDIR = $(HOME)/git/openxpki/core/server

# Usage: $(call perlcfg,KEY)
define perlcfg
$(shell $(PERL) "-V:$1" | awk -F\' '{print $$2}')
endef

SITELIB		= $(call perlcfg,sitelib)
SITEARCH	= $(call perlcfg,sitearch)
SITELIBEXP	= $(DESTDIR)$(call perlcfg,sitelibexp)
ARCHNAME	= $(call perlcfg,archname)

# The --reinstall flag ensures that the package is built even if cpanm finds
# the module already installed
CPANM_OPTS = --notest --reinstall --verbose

#MYPERL_PREFIX = /opt/myperl

# Environment vars needed for proper Perl module installation
# The PERL5LIB has the lib/perl5 in it to work around a bug in cpanm
export PERL5LIB		= $(DESTDIR)$(SITEARCH):$(DESTDIR)$(SITELIB):$(DESTDIR)/lib/perl5
export PERL_MB_OPT	= "--destdir '$(DESTDIR)' --installdirs site"
#export PERL_MB_OPT	= "--installdirs site"
#export PERL_MM_OPT	= "INSTALLDIRS=site INSTALL_BASE=$(DESTDIR)"
export PERL_MM_OPT	= "INSTALLDIRS=site"

info:
	@echo "*** Makefile for openxpki-core-deps-myperl ***"
	@echo "PERL5LIB     = $(PERL5LIB)"
	@echo "PERL_MB_OPT  = $(PERL_MB_OPT)"
	@echo "PERL_MM_OPT  = $(PERL_MM_OPT)"
	@echo "ARCHNAME     = $(ARCHNAME)"
	@echo "DESTDIR      = $(DESTDIR)"
	@echo "COREDIR      = $(COREDIR)"
	@echo "PERL         = $(PERL)"
	@echo "CPANM        = $(CPANM)"
	@echo "CPANM_OPTS   = $(CPANM_OPTS)"

install: info
	PERL5LIB=$(PERL5LIB) PERL_MB_OPT=$(PERL_MB_OPT) DESTDIR=$(DESTDIR) PERL_MM_OPT=$(PERL_MM_OPT) \
		$(CPANM) $(CPANM_OPTS) --installdeps $(COREDIR)
#		$(CPANM) $(CPANM_OPTS) Class::Std Crypt::OpenSSL::AES
	# Cleanup for missing support in cpanm for DESTDIR with .meta files
	-mv $(DESTDIR)/lib/perl5/$(ARCHNAME)/.meta $(DESTDIR)$(SITEARCH)/
	# try to *safely* remove the unneeded directories
	-rmdir $(DESTDIR)/lib/perl5/$(ARCHNAME) $(DESTDIR)/lib/perl5 $(DESTDIR)/lib

%:
	@echo "** DEBUG ** makefile target '$@' doesn't exist in openxpki-core-deps-myperl Makefile"

# This target writes the package and other debian files to the parent directory '..'
# It will cause the debian helper stuff to run all the above target(s).
package:
	dpkg-buildpackage -us -uc
