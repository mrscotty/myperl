# Makefile for libclass-std-myperl

PERL = /opt/myperl/bin/perl
CPANM = /opt/myperl/bin/cpanm

# Usage: $(call perlcfg,KEY)
define perlcfg
$(shell $(PERL) "-V:$1" | awk -F\' '{print $$2}')
endef

SITELIB		= $(call perlcfg,sitelib)
SITEARCH	= $(call perlcfg,sitearch)
SITELIBEXP	= $(DESTDIR)$(call perlcfg,sitelibexp)
ARCHNAME	= $(call perlcfg,archname)

#MYPERL_PREFIX = /opt/myperl

# Environment vars needed for proper Perl module installation
export PERL5LIB		= $(DESTDIR)$(SITEARCH):$(DESTDIR)$(SITELIB)
export PERL_MB_OPT	= "--destdir '$(DESTDIR)' --installdirs site"
export PERL_MM_OPT	= "INSTALLDIRS=site INSTALL_BASE=$(DESTDIR)"
#export PERL_MB_OPT = "--destdir '$(DESTDIR)' --installdirs site --installarchlib '$(SITEARCH)'"
#export PERL_MM_OPT = "INSTALLDIRS=site DESTDIR=$(DESTDIR) INSTALLARCHLIB=$(SITEARCH)"

info:
	@echo "PERL5LIB     = $(PERL5LIB)"
	@echo "PERL_MB_OPT  = $(PERL_MB_OPT)"
	@echo "PERL_MM_OPT  = $(PERL_MM_OPT)"

# The --reinstall flag ensures that the package is built even if cpanm finds
# the module already installed
install:
	PERL5LIB=$(PERL5LIB) PERL_MB_OPT=$(PERL_MB_OPT) PERL_MM_OPT=$(PERL_MM_OPT) DESTDIR=$(DESTDIR) \
			 $(CPANM) --reinstall --verbose Class::Std
	# Cleanup for missing support in cpanm for DESTDIR with .meta files
	mv $(DESTDIR)/lib/perl5/$(ARCHNAME)/.meta $(DESTDIR)$(SITEARCH)/
	# try to *safely* remove the unneeded directories
	rmdir $(DESTDIR)/lib/perl5/$(ARCHNAME) $(DESTDIR)/lib/perl5 $(DESTDIR)/lib

%:
	@echo "** DEBUG ** makefile target '$@' doesn't exist in libclass-std-myperl Makefile"

# This target writes the package and other debian files to the parent directory '..'
# It will cause the debian helper stuff to run all the above target(s).
package:
	dpkg-buildpackage -us -uc
