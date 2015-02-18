#
# spec file for package perl
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


Name:           myperl
Summary:        Local installation of the Perl interpreter
License:        Artistic-1.0 or GPL-2.0+
Group:          Development/Languages/Perl
%define pversion 5.20.1
Version:        %{pversion}
Release:        1
Vendor:         OpenXPKI Project
Packager:       Scott Hardin <scott@hnsc.de>
Autoreqprov:    off
Url:            http://www.perl.org/
Source:         http://www.cpan.org/src/5.0/perl-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#PreReq:         perl-base = %version
#PreReq:         %fillup_prereq
#BuildRequires:  db-devel
#BuildRequires:  gdbm-devel
#BuildRequires:  libbz2-devel
#BuildRequires:  ncurses-devel
#BuildRequires:  zlib-devel
#Requires:       gzip	# needed in SuSEconfig.perl
Suggests:       perl-doc = %version
#
%if "%version" != "%pversion"
Provides:       myperl = %pversion-%release
%endif
Provides:       myperl-500
Provides:       myperl-macros
Provides:       myperl(:MODULE_COMPAT_%pversion)
Obsoletes:      myperl-macros
Provides:       myperl-Filter-Simple
Obsoletes:      myperl-Filter-Simple
Provides:       myperl-I18N-LangTags
Obsoletes:      myperl-I18N-LangTags
Provides:       myperl-MIME-Base64
Obsoletes:      myperl-MIME-Base64
Provides:       myperl-Storable
Obsoletes:      myperl-Storable
Provides:       myperl-Test-Simple = 0.98-%{release}
Obsoletes:      myperl-Test-Simple < 0.98
Provides:       myperl-Text-Balanced
Obsoletes:      myperl-Text-Balanced
Provides:       myperl-Time-HiRes
Obsoletes:      myperl-Time-HiRes
Provides:       myperl-libnet
Obsoletes:      myperl-libnet
Provides:       myperl-Compress-Raw-Zlib
Obsoletes:      myperl-Compress-Raw-Zlib
Provides:       myperl-Compress-Zlib
Obsoletes:      myperl-Compress-Zlib
Provides:       myperl-IO-Compress-Base
Obsoletes:      myperl-IO-Compress-Base
Provides:       myperl-IO-Compress-Zlib
Obsoletes:      myperl-IO-Compress-Zlib
Provides:       myperl-IO-Zlib
Obsoletes:      myperl-IO-Zlib
Provides:       myperl-Archive-Tar
Obsoletes:      myperl-Archive-Tar
Provides:       myperl-Module-Build = 0.3901
Provides:       myperl(Module::Build) = 0.3901
Obsoletes:      myperl-Module-Build < 0.3901
Provides:       myperl-Module-Pluggable = 4.0
Obsoletes:      myperl-Module-Pluggable < 4.0
Provides:       myperl-Locale-Maketext-Simple = 0.21
Obsoletes:      myperl-Locale-Maketext-Simple < 0.21
Provides:       myperl-Pod-Escapes = 1.04
Obsoletes:      myperl-Pod-Escapes < 1.04
Provides:       myperl-Pod-Simple = 3.2
Obsoletes:      myperl-Pod-Simple < 3.2
Provides:       myperl-ExtUtils-ParseXS
Obsoletes:      myperl-ExtUtils-ParseXS
Provides:       myperl-version
Obsoletes:      myperl-version
Provides:       myperl-Digest
Provides:       myperl-Digest-MD5
%define filelist %{pkgname}-%{version}-filelist

%description
myperl - Local Version of Practical Extraction and Report Language

Perl is optimized for scanning arbitrary text files, extracting
information from those text files, and printing reports based on that
information.  It is also good for many system management tasks. Perl is
intended to be practical (easy to use, efficient, and complete) rather
than beautiful (tiny, elegant, and minimal).

Some of the modules available on CPAN can be found in the "myperl"
series.

The "myperl" version is just a separate Perl installation parallel to
the system Perl that comes with the distribution.

%prep
%setup -q -n perl-%{pversion}
#cp -p %{S:3} .
#%patch0
#%patch1
#%patch2
#%patch3
#%patch4
#%patch5
#%patch6
#%patch7
#%patch8
#%patch9
#%patch10

%build
#cp -a lib savelib
#export SUSE_ASNEEDED=0
#export BZIP2_LIB=%{_libdir}
#export BZIP2_INCLUDE=%{_includedir}
#export BUILD_BZIP2=0
#options="-Doptimize='$RPM_OPT_FLAGS -Wall -pipe'"
#%ifarch alpha
## -mieee needed for bad alpha gcc optimization
#options="-Doptimize='$RPM_OPT_FLAGS -Wall -pipe -mieee'"
#%endif
#%ifarch ppc ppc64
#options="$options -Duse64bitint"
#%endif
## always use glibc's setenv
#options="$options -Accflags='-DPERL_USE_SAFE_PUTENV'"
#options="$options -Dotherlibdirs=/usr/lib/perl5/site_perl"
#chmod 755 ./configure.gnu
#./configure.gnu --prefix=/usr -Dvendorprefix=/usr -Dinstallusrbinperl -Dusethreads -Di_db -Di_dbm -Di_ndbm -Di_gdbm -Dd_dbm_open -Duseshrplib=\'true\' $options
#make %{?_smp_mflags}
#cp -p libperl.so savelibperl.so
#cp -p lib/Config.pm saveConfig.pm
#cp -p lib/Config_heavy.pl saveConfig_heavy.pl
#make clean > /dev/null
#make clobber
#rm -rf lib
#mv savelib lib
#./configure.gnu --prefix=/usr -Dvendorprefix=/usr -Dinstallusrbinperl -Dusethreads -Di_db -Di_dbm -Di_ndbm -Di_gdbm -Dd_dbm_open $options
#make %{?_smp_mflags}

# Note: setting vendorprefix=/opt/myperl actually causes it to use the
# directories /opt/myperl/lib/vendor_perl/5.20.0 and
# /opt/myperl/lib/vendor_perl/5.20.0/x86_64-linux
./Configure -des \
    -Dprefix=/opt/myperl \
    -Dvendorprefix=/opt/myperl \
    -Duseithreads \
    -Duseshrplib

%check
%ifnarch %arm
export SUSE_ASNEEDED=0
#make test
%endif

%install
MYPERL="./miniperl -Ilib"
make install DESTDIR=$RPM_BUILD_ROOT

#if false; then # disable this whole block for now
# Fetch cpanm
curl -LO http://xrl.us/cpanm
chmod +x cpanm

VENDORLIB=`$MYPERL "-V:vendorlib" | awk -F\' '{print $2}'`        # 'syntax
VENDORARCH=`$MYPERL "-V:vendorarch" | awk -F\' '{print $2}'`      # 'syntax
VENDORLIBEXP=`$MYPERL "-V:vendorlibexp" | awk -F\' '{print $2}'`  # 'syntax
ARCHNAME=`$MYPERL "-V:archname" | awk -F\' '{print $2}'`          # 'syntax
ARCHLIB=`$MYPERL "-V:archlib" | awk -F\' '{print $2}'`            # 'syntax
PRIVLIB=`$MYPERL "-V:privlib" | awk -F\' '{print $2}'`            # 'syntax
CPANM_OPTS="--notest --verbose --skip-satisfied --skip-installed"

echo "===== DEBUG"
echo "VENDORLIB=$VENDORLIB"
echo "VENDORARCH=$VENDORARCH"
echo "VENDORLIBEXP=$VENDORLIBEXP"
echo "ARCHNAME=$ARCHNAME"
echo "ARCHLIB=$ARCHLIB"
echo "PRIVLIB=$PRIVLIB"
echo "===== DEBUG"

# Env vars needed for proper Perl module installation
export PERL5LIB="$RPM_BUILD_ROOT/$VENDORARCH:$RPM_BUILD_ROOT/$VENDORLIB"
export PERL_MB_OPT="--destdir '$RPM_BUILD_ROOT' --installdirs vendor"
export PERL_MM_OPT="DESTDIR=$RPM_BUILD_ROOT INSTALLDIRS=vendor"

# Install some CPAN dependencies to avoid conflicts
# (e.g. between oxi and mysql)
#DESTDIR=$RPM_BUILD_ROOT $MYPERL cpanm $CPANM_OPTS Test::NoWarnings Test::Tester Test::Deep
#DESTDIR=$RPM_BUILD_ROOT $MYPERL cpanm $CPANM_OPTS CPAN::Meta

# NOTE: ExtUtils::MakeMaker that comes with Perl 5.20.1 seems to
# be outdated, so let's force an update here.
DESTDIR=$RPM_BUILD_ROOT $MYPERL cpanm $CPANM_OPTS ExtUtils::MakeMaker
#fi

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


#cp -a $RPM_BUILD_ROOT/usr/lib/perl5/site_perl $RPM_BUILD_ROOT/usr/lib/perl5/vendor_perl
#cpa=`echo $RPM_BUILD_ROOT/usr/lib/perl5/*/*/CORE | sed -e 's@/CORE$@@'`
#cp=`echo "$cpa" | sed -e 's@/[^/]*$@@'`
#vpa=`echo $cpa | sed -e 's@/perl5/@/perl5/vendor_perl/@'`
#vp=`echo "$vpa" | sed -e 's@/[^/]*$@@'`
#install -d $vp/auto
#install -d $vpa/auto
#install -m 555 savelibperl.so $cpa/CORE/libperl.so
#install -m 444 saveConfig.pm $cpa/Config.pm
#install -m 444 saveConfig_heavy.pl $cpa/Config_heavy.pl
##install -d $RPM_BUILD_ROOT/var/adm/SuSEconfig/bin
##install -d $RPM_BUILD_ROOT/sbin/conf.d
##install -d $RPM_BUILD_ROOT/var/adm/fillup-templates
##install -m 755 SuSE/perllocal.SuSE $RPM_BUILD_ROOT/usr/lib/perl5
##install -m 755 SuSE/SuSEconfig.perl $RPM_BUILD_ROOT/sbin/conf.d
##install -m 755 SuSE/sysconfig.suseconfig-perl $RPM_BUILD_ROOT/var/adm/fillup-templates
## install macros.perl file
#install -D -m 644 %{S:2} $RPM_BUILD_ROOT%{_sysconfdir}/rpm/macros.perl
#pushd /usr/include
#( rpm -ql glibc-devel | fgrep '.h' 
#  find /usr/include/asm/ -name \*.h
#  find /usr/include/asm-generic -name \*.h
#  find /usr/include/linux -name \*.h
#) | while read f; do
#  $RPM_BUILD_ROOT/usr/bin/perl -I$cp -I$cpa $RPM_BUILD_ROOT/usr/bin/h2ph -d $vpa ${f/\/usr\/include\//} || : 
#done
#popd
#d="`gcc -print-file-name=include`"
#test -f "$d/stdarg.h" && (cd $d ; $RPM_BUILD_ROOT/usr/bin/perl -I$cp -I$cpa $RPM_BUILD_ROOT/usr/bin/h2ph -d $vpa stdarg.h stddef.h float.h)
## remove broken pm - we don't have the module
#rm $RPM_BUILD_ROOT/usr/lib/perl5/*/Pod/Perldoc/ToTk.pm
## we don't need this in here
#rm $RPM_BUILD_ROOT/usr/lib/perl5/*/*/CORE/libperl.a
##touch $RPM_BUILD_ROOT/usr/share/man/man3/perllocal.3pm
##touch $cpa/perllocal.pod
## test CVE-2007-5116
#$RPM_BUILD_ROOT/usr/bin/perl -e '$r=chr(128)."\\x{100}";/$r/'
## test perl-regexp-refoverflow.diff
#$RPM_BUILD_ROOT/usr/bin/perl -e '/\6666666666/'
#%if 0
## remove unrelated target/os manpages
#rm $RPM_BUILD_ROOT/usr/share/man/man1/perlaix.1*
#rm $RPM_BUILD_ROOT/usr/share/man/man1/perlamiga.1*
#rm $RPM_BUILD_ROOT/usr/share/man/man1/perlapollo.1*
#rm $RPM_BUILD_ROOT/usr/share/man/man1/perlbeos.1*
#rm $RPM_BUILD_ROOT/usr/share/man/man1/perlbs2000.1*
#rm $RPM_BUILD_ROOT/usr/share/man/man1/perlcygwin.1*
#rm $RPM_BUILD_ROOT/usr/share/man/man1/perldgux.1*
#rm $RPM_BUILD_ROOT/usr/share/man/man1/perldos.1*
#rm $RPM_BUILD_ROOT/usr/share/man/man1/perlepoc.1*
#rm $RPM_BUILD_ROOT/usr/share/man/man1/perlfreebsd.1*
#rm $RPM_BUILD_ROOT/usr/share/man/man1/perlhpux.1*
#rm $RPM_BUILD_ROOT/usr/share/man/man1/perlhurd.1*
#rm $RPM_BUILD_ROOT/usr/share/man/man1/perlirix.1*
#rm $RPM_BUILD_ROOT/usr/share/man/man1/perlmachten.1*
#rm $RPM_BUILD_ROOT/usr/share/man/man1/perlmacos.1*
#rm $RPM_BUILD_ROOT/usr/share/man/man1/perlmacosx.1*
#rm $RPM_BUILD_ROOT/usr/share/man/man1/perlmint.1*
#rm $RPM_BUILD_ROOT/usr/share/man/man1/perlnetware.1*
#rm $RPM_BUILD_ROOT/usr/share/man/man1/perlopenbsd.1*
#rm $RPM_BUILD_ROOT/usr/share/man/man1/perlos2.1*
#rm $RPM_BUILD_ROOT/usr/share/man/man1/perlos390.1*
#rm $RPM_BUILD_ROOT/usr/share/man/man1/perlos400.1*
#rm $RPM_BUILD_ROOT/usr/share/man/man1/perlplan9.1*
#rm $RPM_BUILD_ROOT/usr/share/man/man1/perlqnx.1*
#rm $RPM_BUILD_ROOT/usr/share/man/man1/perlsolaris.1*
#rm $RPM_BUILD_ROOT/usr/share/man/man1/perltru64.1*
#rm $RPM_BUILD_ROOT/usr/share/man/man1/perluts.1*
#rm $RPM_BUILD_ROOT/usr/share/man/man1/perlvmesa.1*
#rm $RPM_BUILD_ROOT/usr/share/man/man1/perlvms.1*
#rm $RPM_BUILD_ROOT/usr/share/man/man1/perlvos.1*
#rm $RPM_BUILD_ROOT/usr/share/man/man1/perlwin32.1*
#%endif
#cat << EOF > perl-base-filelist
#/usr/lib/perl5/%pversion/B/Deparse.pm
#/usr/lib/perl5/%pversion/Carp.pm
#/usr/lib/perl5/%pversion/Carp/
#/usr/lib/perl5/%pversion/Class/
#/usr/lib/perl5/%pversion/Config/
#/usr/lib/perl5/%pversion/Digest.pm
#/usr/lib/perl5/%pversion/Digest/
#/usr/lib/perl5/%pversion/Exporter.pm
#/usr/lib/perl5/%pversion/Exporter/
#/usr/lib/perl5/%pversion/File/
#/usr/lib/perl5/%pversion/Getopt/
#/usr/lib/perl5/%pversion/IPC/
#/usr/lib/perl5/%pversion/Text/
#/usr/lib/perl5/%pversion/Tie/Hash.pm
#/usr/lib/perl5/%pversion/XSLoader.pm
#/usr/lib/perl5/%pversion/warnings.pm
#/usr/lib/perl5/%pversion/warnings/
#/usr/lib/perl5/%pversion/AutoLoader.pm
#/usr/lib/perl5/%pversion/FileHandle.pm
#/usr/lib/perl5/%pversion/SelectSaver.pm
#/usr/lib/perl5/%pversion/Symbol.pm
#/usr/lib/perl5/%pversion/base.pm
#/usr/lib/perl5/%pversion/bytes.pm
#/usr/lib/perl5/%pversion/bytes_heavy.pl
#/usr/lib/perl5/%pversion/constant.pm
#/usr/lib/perl5/%pversion/fields.pm
#/usr/lib/perl5/%pversion/feature.pm
#/usr/lib/perl5/%pversion/integer.pm
#/usr/lib/perl5/%pversion/locale.pm
#/usr/lib/perl5/%pversion/overload.pm
#/usr/lib/perl5/%pversion/overloading.pm
#/usr/lib/perl5/%pversion/strict.pm
#/usr/lib/perl5/%pversion/unicore/Heavy.pl
#/usr/lib/perl5/%pversion/utf8.pm
#/usr/lib/perl5/%pversion/utf8_heavy.pl
#/usr/lib/perl5/%pversion/vars.pm
#/usr/lib/perl5/%pversion/version.pm
#/usr/lib/perl5/%pversion/*-linux-thread-multi*/Data/
#/usr/lib/perl5/%pversion/*-linux-thread-multi*/Digest/
#/usr/lib/perl5/%pversion/*-linux-thread-multi*/File/
#/usr/lib/perl5/%pversion/*-linux-thread-multi*/List/
#/usr/lib/perl5/%pversion/*-linux-thread-multi*/Scalar/
#/usr/lib/perl5/%pversion/*-linux-thread-multi*/IO.pm
#/usr/lib/perl5/%pversion/*-linux-thread-multi*/IO/Dir.pm
#/usr/lib/perl5/%pversion/*-linux-thread-multi*/IO/File.pm
#/usr/lib/perl5/%pversion/*-linux-thread-multi*/IO/Handle.pm
#/usr/lib/perl5/%pversion/*-linux-thread-multi*/IO/Pipe.pm
#/usr/lib/perl5/%pversion/*-linux-thread-multi*/IO/Poll.pm
#/usr/lib/perl5/%pversion/*-linux-thread-multi*/IO/Seekable.pm
#/usr/lib/perl5/%pversion/*-linux-thread-multi*/IO/Select.pm
#/usr/lib/perl5/%pversion/*-linux-thread-multi*/IO/Socket.pm
#/usr/lib/perl5/%pversion/*-linux-thread-multi*/IO/Socket/
#/usr/lib/perl5/%pversion/*-linux-thread-multi*/B.pm
#/usr/lib/perl5/%pversion/*-linux-thread-multi*/Config.pm
#/usr/lib/perl5/%pversion/*-linux-thread-multi*/Config_heavy.pl
#/usr/lib/perl5/%pversion/*-linux-thread-multi*/Cwd.pm
#/usr/lib/perl5/%pversion/*-linux-thread-multi*/DynaLoader.pm
#/usr/lib/perl5/%pversion/*-linux-thread-multi*/Errno.pm
#/usr/lib/perl5/%pversion/*-linux-thread-multi*/Fcntl.pm
#/usr/lib/perl5/%pversion/*-linux-thread-multi*/POSIX.pm
#/usr/lib/perl5/%pversion/*-linux-thread-multi*/Socket.pm
#/usr/lib/perl5/%pversion/*-linux-thread-multi*/attributes.pm
#/usr/lib/perl5/%pversion/*-linux-thread-multi*/auto/Data/
#/usr/lib/perl5/%pversion/*-linux-thread-multi*/auto/Digest/
#/usr/lib/perl5/%pversion/*-linux-thread-multi*/auto/Fcntl/
#/usr/lib/perl5/%pversion/*-linux-thread-multi*/auto/File/
#/usr/lib/perl5/%pversion/*-linux-thread-multi*/auto/IO/
#/usr/lib/perl5/%pversion/*-linux-thread-multi*/auto/List/
#/usr/lib/perl5/%pversion/*-linux-thread-multi*/auto/Cwd/
#/usr/lib/perl5/%pversion/*-linux-thread-multi*/auto/Socket/
#/usr/lib/perl5/%pversion/*-linux-thread-multi*/auto/POSIX/POSIX.bs
#/usr/lib/perl5/%pversion/*-linux-thread-multi*/auto/POSIX/POSIX.so
#/usr/lib/perl5/%pversion/*-linux-thread-multi*/lib.pm
#/usr/lib/perl5/%pversion/*-linux-thread-multi*/re.pm
#EOF
#{
#  sed -e 's/^/%%exclude /' perl-base-filelist
#  (cd $RPM_BUILD_ROOT
#   for i in usr/lib/perl5/*/pod/*; do
#     case $i in */perldiag.pod) ;;
#     *) echo "%%exclude /$i" ;;
#     esac
#   done)
#} > perl-base-excludes
##%%post
#%%{fillup_only -an suseconfig}

#%files base -f perl-base-filelist
#%defattr(-,root,root)
#%dir /usr/lib/perl5
#%dir /usr/lib/perl5/%pversion
#%dir /usr/lib/perl5/%pversion/B
#%dir /usr/lib/perl5/%pversion/*-linux-thread-multi*
#%dir /usr/lib/perl5/%pversion/*-linux-thread-multi*/auto
#%dir /usr/lib/perl5/%pversion/*-linux-thread-multi*/auto/POSIX
#/usr/bin/perl
#/usr/bin/perl%pversion
#%doc /usr/share/man/man1/perl.1.gz
#
#%files -f perl-base-excludes 
#%defattr(-,root,root)
#%exclude /usr/bin/perl
#%exclude /usr/bin/perl%pversion
#/usr/bin/*
#/usr/lib/perl5/*
#%config %{_sysconfdir}/rpm/macros.perl
##/sbin/conf.d/SuSEconfig.perl
##/var/adm/fillup-templates/sysconfig.suseconfig-perl
##%ghost /usr/lib/perl*/*/*/perllocal.pod
##%ghost %doc /usr/share/man/man3/perllocal.3pm.gz
#
#%files doc
#%defattr(-,root,root)
#%doc README.macros
#%exclude /usr/share/man/man1/perl.1.gz
#%exclude /usr/lib/perl5/*/pod/perldiag.pod
#%doc /usr/share/man/man1/*
#%doc /usr/share/man/man3/*
#%doc /usr/lib/perl5/*/pod

%files
%defattr(-,root,root)
/opt/myperl

%clean
[ "%{buildroot}" != "/" ] && rm -rf "%{buildroot}"


%changelog
* Wed Jun 25 2014 scott@hnsc.de
- initial myperl package based on SuSE Perl and my own other packaging work
