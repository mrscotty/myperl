# OVERVIEW

'myperl' is a Perl installation that is independent of the system Perl
supplied by the distribution you are using.

For many cases, the system Perl that comes with your distribution is
completely sufficient. But if your application has a plethora of CPAN
dependencies or requires module versions not supplied by the distribution,
'myperl' can be a way of having debian packages of your own Perl and 
CPAN dependencies.

# BUILDING MYPERL

For those familiar with debian packaging, you'll notice  that this package
is a non-native debian package. It uses the original Perl tarball (which
gets renamed to 'myperl\_\*.orig.tar.bz2) and adds a debian/ directory.

To build the debian myperl package:

    # fetch Perl tarball, if needed
    make fetch-perl

    # build debian package
    make myperl

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




