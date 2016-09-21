# OVERVIEW

'myperl' is a Perl installation that is independent of the system Perl
supplied by the distribution you are using.

For many cases, the system Perl that comes with your distribution is
completely sufficient. But if your application has a plethora of CPAN
dependencies or requires module versions not supplied by the distribution,
'myperl' can be a way of having debian packages of your own Perl and 
CPAN dependencies.

# VERSION NUMBERS

## Definitions

### Perl Version

This is the version string of the underlying Perl version. As of this
writing, the current version was 5.20.0.

### Myperl Release Number

This is a single integer used to distinguish between Myperl  that is unique
for each underlying Perl version.

This number starts at '1' and is incremented each time a new package for
the given Perl version is generated. When the Perl version changes, it
starts again at '1'.

Since myperl is mainly about installable packages, this myperl version number
can be used for the release number in RPM files.

### Myperl Version

This is the full version string used in the package name and for the 
version number of the installable packages. It consists of the Perl version
followed by the myperl release number, in the format:

    PERL_VERSION.MYPERL_RELEASE_NUMBER

# BUILDING MYPERL

For those familiar with debian packaging, you'll notice  that this package
is a non-native debian package. It uses the original Perl tarball (which
gets renamed to 'myperl\_\*.orig.tar.bz2) and adds a debian/ directory.

To build the debian myperl package:

    # fetch Perl tarball, if needed
    make fetch-perl

    # build debian package
    make debian

As an example, here are the further steps for building OpenXPKI,
including the CPAN dependencies:

    # install the freshly-built myperl package
    make debian-install

    # install prereqs for mysql and openxpki
    sudo aptitude install -y libmysqlclient-dev apache2

    # build and install mysql package
    (cd ex/libdbd-mysql-myperl && make package)
    sudo dpkg -i ex/libdbd-mysql-myperl*.deb

    # build and install oxi dependencies
    git clone /git/openxpki ~/git/openxpki
    (cd ex/openxpki-core-deps-myperl && make package)
    sudo dpkg -i ex/openxpki-core-deps-myperl*.deb

    # build and install oxi
    (cd ~/git/openxpki/package/debian && make core)
    sudo dpkg -i ~/git/openxpki/package/debian/core/libopenxpki-perl*.deb




    
    


## First Steps (initial non-native debian package)

To see how the initial contents of the debian/ were created, see the script
'bootstrap.mk'.

# BUILDING SUPPLEMENTAL PACKAGES

Installing supplemental packages (i.e.: all the CPAN prerequisites needed
by your application) is done quite differently from the debian Perl. Debian
uses dh-perl to package each CPAN module individually, which works well for
the system Perl--unless your application needs 130 CPAN prereqs.

When packaging the dependencies for your application, it is much easier 
to put them all in a single debian package. And if your application
specifies its dependencies correctly, the packaging script is as simple
as calling 'cpanm --installdeps PATH\_TO\_YOUR\_APP\_SRC'.

For these packages, the native debian package seems to work well. 

The ex/ directory contains a couple of examples, simple and complex.
To build libdbd-mysql, for example, run the following:

    cd ex/libdbd-mysql-myperl && make package

# openSUSE:Build

For building on openSUSE:build, follow the instructions in the tutorial:

    https://en.opensuse.org/openSUSE:Build_Service_Tutorial

In the Source Files list, add the http(s) links to the cpanm script
and perl tarball. Upload myperl.spec (you need to run "make myperl.spec"
to generate this from the template) and perl-rpmlintrc.

## myperl

    make myperl.spec

## myperl-buildtools

Create the myperl-buildtools.spec:

    make myperl-buildtools.spec

Add the following sources to the OBS package:

    https://cpan.metacpan.org/authors/id/L/LE/LEONT/Module-Build-0.4218.tar.gz
    https://cpan.metacpan.org/authors/id/C/CH/CHORNY/Class-Std-0.013.tar.gz
    https://cpan.metacpan.org/authors/id/B/BR/BRICKER/Config-Std-0.901.tar.gz
    https://cpan.metacpan.org/authors/id/A/AD/ADAMK/Test-NoWarnings-1.04.tar.gz
    https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Test-Simple-1.302031.tar.gz
    https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Test-Deep-1.120.tar.gz

## myperl-dbi

Create the myperl-dbi.spec:

    make myperl-dbi.spec

Add the spec file and the following sources to the OBS package:

    https://cpan.metacpan.org/authors/id/T/TI/TIMB/DBI-1.636.tar.gz

## myperl-fcgi

Create the myperl-fcgi.spec:

    make myperl-fcgi.spec

Add the spec file and the following sources to the OBS package:

    https://cpan.metacpan.org/authors/id/E/ET/ETHER/FCGI-0.78.tar.gz


# ADDITIONAL INFO

## TROUBLESHOOTING

If you get an error that files aren't found, look for the line '<CPAN::Module> is up to date.'
This happens when the CPAN module is already installed.

## Alternatives

### Manual Download and Installation of Perl Tarball

Sure, this may be an easy option in an ad-hoc development environment, but if 
your application is deployed using Debian packages, you need an easy method
for building those packages. That's exactly what 'myperl' is.

### Perlbrew

Perlbrew does automate the task of downloading and installing the Perl,
tarball, but the foo it adds to cater to developers adds some overhead
that makes it less suitable for deployment in production environments.

Also, perlbrew depends on a compiler, which is often frowned on in production
environments for security reasons.

### Carton

Carton looks very promising because it can be easily used to create Perl
and dependency packages for distribution in develoment, test and production
environments. I really wanted to use this one. According to the Carton
website, however, it doesn't work in environments using embedded Perl
(e.g. mod\_perl). Bummer.

# REFERENCES

Information for preparing this was taken from the following sources:

*    http://forums.debian.net/viewtopic.php?t=38976

*    http://www.debian.org/doc/manuals/maint-guide/first.en.html




