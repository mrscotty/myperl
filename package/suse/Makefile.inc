# Written 2016 by Scott Hardin for the OpenXPKI Project
# Copyright (c) 2016 by The OpenXPKI Project
#
# USAGE:
#
# Your Makefile must include at least the following:
#
#   PACKAGE=myperl-<package_name
#   include ../Makefile.inc

# Common definitions for all SuSE package Makefiles
# for myperl subpackages

ifndef PERL_VERSION
$(error PERL_VERSION not defined)
endif
ifndef MYPERL_RELEASE
$(error MYPERL_RELEASE not defined)
endif

# standard directory for RPM builds, to override this use Makefile.local
# or by setting it in your shell environment
RPMBASE?=$(shell rpm --eval '%{_topdir}')
RPMBASE?=/usr/src/packages

ifdef PREFIX
PERL_MAKEPL_ARGS="PREFIX=$(PREFIX)"
endif

PERL := $(shell which perl)

ifndef GIT_AUTHOR_NAME
	GIT_AUTHOR_NAME := $(shell git config --get user.name)
endif
ifndef GIT_AUTHOR_EMAIL
	GIT_AUTHOR_EMAIL := $(shell git config --get user.email)
endif
PACKAGER := $(strip $(GIT_AUTHOR_NAME) <$(GIT_AUTHOR_EMAIL)>)

TT_VERSION_SYMBOLS = --define version="$(PERL_VERSION)" --define PKGREL=$(MYPERL_RELEASE) --define PACKAGER="$(PACKAGER)" --define STATIC_TARBALLS=$(STATIC_TARBALLS)
.SUFFIXES: .template

# For documentation in this implicit rule, see ../../common/Makefile.inc
%:: %.template
	cat $< | tpage $(TT_VERSION_SYMBOLS) $(TT_EXTRA_SYMBOLS) >$@.new
	mv $@.new $@

# May be used to locally to override settings (not checked into git)
-include ../Makefile.local

# Default target
all: clean package

$(PACKAGE).spec: $(PACKAGE).spec.template

package: $(PACKAGE).spec
	PERL_LOCAL_LIB_ROOT= PERL_MB_OPT= PERL_MM_OPT= rpmbuild -ba $(PACKAGE).spec

collect:
	mv $(RPMBASE)/SRPMS/$(PACKAGE)-*.rpm .
	mv $(RPMBASE)/RPMS/*/$(PACKAGE)-*.rpm .

clean:
	rm -f $(PACKAGE)-*.rpm $(PACKAGE).spec




