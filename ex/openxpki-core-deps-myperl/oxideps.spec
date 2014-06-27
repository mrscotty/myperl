#
# spec file for myperl oxi deps 
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#
# icecream 0


Name:           openxpki-core-deps-myperl
Summary:        OpenXPKI Core Dependencies for myperl
License:        Artistic-1.0 or GPL-2.0+
Group:          Development/Languages/Perl
Version:        5.20.0
Release:        1
Vendor:         OpenXPKI Project
Packager:       Scott Hardin <scott@hnsc.de>
Autoreqprov:    off
%define pversion 5.20.0
Url:            http://www.perl.org/
Source:         http://www.cpan.org/src/5.0/perl-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#PreReq:         perl-base = %version
#PreReq:         %fillup_prereq
Requires:       myperl
Requires:       libopenssl0_9_8
Requires:       zlib
BuildRequires:  myperl
BuildRequires:  libopenssl-devel
BuildRequires:  zlib-devel

%define filelist %{pkgname}-%{version}-filelist

%description
OpenXPKI Core dependencies from CPAN using myperl

%prep

%build

%check

%install
PERL=/opt/myperl/bin/perl
CPANM="$PERL $PWD/cpanm"
#CPANM="$PERL -I/git/cpanminus/lib /git/cpanminus/cpanm"
COREDIR=$HOME/git/openxpki/core/server
export DESTDIR=$RPM_BUILD_ROOT

function perlcfg() {
  local key=$1
  local val=`$PERL "-V:$key" | awk -F\' '{print $2}'`
  # fix syntax highlighting with extra apostrophe -> '
  echo "$val"
}
  
SITELIB=$(perlcfg sitelib)
SITEARCH=$(perlcfg sitearch)
SITELIBEXP=${DESTDIR}$(perlcfg sitelibexp)
ARCHNAME=$(perlcfg archname)
SITEMAN1EXP=$(perlcfg siteman1direxp)
SITEMAN3EXP=$(perlcfg siteman3direxp)
SITESCRIPTEXP=$(perlcfg sitescriptexp)

CPANM_OPTS="--notest --verbose --skip-satisfied --skip-installed"

export PERL5LIB=${DESTDIR}${SITEARCH}:${DESTDIR}${SITELIB}:${DESTDIR}/lib/perl5
export PERL_MB_OPT="--destdir ${DESTDIR} --installdirs site"
export PERL_MM_OPT="DESTDIR=${DESTDIR} INSTALLDIRS=site"
    
curl -LO http://xrl.us/cpanm
chmod +x cpanm

PERL5LIB=$PERL5LIB PERL_MB_OPT=$PERL_MB_OPT DESTDIR=$DESTDIR PERL_MM_OPT=$PERL_MM_OPT \
    $CPANM $CPANM_OPTS \
    Config::Std Class::Std

## I used this next one during testing
#PERL5LIB=$PERL5LIB PERL_MB_OPT=$PERL_MB_OPT DESTDIR=$DESTDIR PERL_MM_OPT=$PERL_MM_OPT \
#    $CPANM $CPANM_OPTS \
#    Crypt::SSLeay

(cd $COREDIR && \
    PERL5LIB=$PERL5LIB PERL_MB_OPT=$PERL_MB_OPT DESTDIR=$DESTDIR PERL_MM_OPT=$PERL_MM_OPT \
    $CPANM $CPANM_OPTS \
    --installdeps .)

# Cleanup for missing support in cpanm for DESTDIR with .meta files
mv $DESTDIR/lib/perl5/$ARCHNAME/.meta ${DESTDIR}$SITEARCH/ || echo "WARN: skipping error"

# try to *safely* remove the unneeded directories
rmdir $DESTDIR/lib/perl5/$ARCHNAME $DESTDIR/lib/perl5 $DESTDIR/lib || echo "WARN: skipping error"

# Issue #2 - until I can get Pinto running, just remove the offending files
# Note: since this is a nasty kludge, I'll leave the fail-on-error behavior
# of make.
rm -rf \
    ${DESTDIR}${SITEMAN3EXP}/CGI.3 \
	${DESTDIR}${SITEMAN3EXP}/CGI::Apache.3 \
	${DESTDIR}${SITEMAN3EXP}/CGI::Carp.3 \
	${DESTDIR}${SITEMAN3EXP}/CGI::Cookie.3 \
	${DESTDIR}${SITEMAN3EXP}/CGI::Pretty.3 \
	${DESTDIR}${SITEMAN3EXP}/CGI::Push.3 \
	${DESTDIR}${SITEMAN3EXP}/CGI::Switch.3 \
	${DESTDIR}${SITEMAN3EXP}/CGI::Util.3 \
	${DESTDIR}${SITELIB}/CGI.pm \
	${DESTDIR}${SITELIB}/CGI/Apache.pm \
	${DESTDIR}${SITELIB}/CGI/Carp.pm \
	${DESTDIR}${SITELIB}/CGI/Cookie.pm \
	${DESTDIR}${SITELIB}/CGI/Pretty.pm \
	${DESTDIR}${SITELIB}/CGI/Push.pm \
	${DESTDIR}${SITELIB}/CGI/Switch.pm \
	${DESTDIR}${SITELIB}/CGI/Util.pm \
	${DESTDIR}${SITEMAN3EXP}/Module::Build* \
	${DESTDIR}${SITELIB}/Module/Build.pm \
	${DESTDIR}${SITELIB}/Module/Build \
	${DESTDIR}${ARCHLIB}/auto/Module/Build 
# Issue #2 - let's just trash these for now
rm -rf \
    ${DESTDIR}${SITESCRIPTEXP}/config_data \
	${DESTDIR}${SITEMAN1EXP}/config_data.1 \
	${DESTDIR}${SITEMAN3EXP}/inc::latest.3 \
	${DESTDIR}${SITELIB}/inc

%{__perl} -MFile::Find -le '
    find({ wanted => \&wanted, no_chdir => 1}, "%{buildroot}");
    for my $x (sort @dirs, @files) {
        push @ret, $x unless indirs($x);
        }
    print join "\n", sort @ret;

    sub wanted {
        return if /auto$/;

        local $_ = $File::Find::name;
        my $f = $_; s|^\Q%{buildroot}\E||;
        return unless length;
        return $files[@files] = $_ if (-f $f || -l $f);

        $d = $_;
        /\Q$d\E/ && return for reverse sort @INC;
        $d =~ /\Q$_\E/ && return
            #for qw|/etc %_prefix/man %_prefix/bin %_prefix/share /var |;
            for qw| /etc /opt /usr /srv /var |;

        $dirs[@dirs] = $_;
        }

    sub indirs {
        my $x = shift;
        $x =~ /^\Q$_\E\// && $x ne $_ && return 1 for @dirs;
        }
' > %filelist

[ -z %filelist ] && {
    echo "ERROR: empty %files listing"
    exit -1
    }

%files -f %filelist
%defattr(-,root,root)

%clean
[ "%{buildroot}" != "/" ] && rm -rf "%{buildroot}"


%changelog
* Wed Jun 25 2014 scott@hnsc.de
- initial openxpki-core-deps-myperl package based on SuSE Perl and my own other packaging work
