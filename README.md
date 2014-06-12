# OVERVIEW

This is a parallel installation of Perl that is used independently of
the system Perl supplied by the distribution you are using.

# REFERENCES

Information for preparing this was taken from the following sources:

*    http://forums.debian.net/viewtopic.php?t=38976

*    http://www.debian.org/doc/manuals/maint-guide/first.en.html

## Prereqs

    sudo aptitude install -y quilt

# NOTES (Following the maint-guide doc from debian)

## First Steps (initial non-native debian package)

    . /git/myperl/deb.rc
    cd ~/git/myperl
    tar xjf perl-5.18.2.tar.bz
    cd perl-5.18.2
    dh_make -f ../perl-5.18.2.tar.bz2 --single --packagename myperl_5.18.2+1 --copyright artistic --yes

### Output from dh\_make:

    Maintainer name  : Scott Hardin
    Email-Address    : scott@hnsc.de
    Date             : Thu, 12 Jun 2014 19:19:44 +0000
    Package Name     : myperl
    Version          : 5.18.2+1
    License          : artistic
    Type of Package  : Single
    Currently there is no top level Makefile. This may require additional tuning.
    Done. Please edit the files in the debian/ subdirectory now. You should also
    check that the myperl Makefiles install into $DESTDIR and not in / .

### Patching up debian/ files

Manually clean up the following files:

debian/control: Set 'Description:' to 'Local Perl installation independent of system Perl'

    cp /git/myperl/control debian/

debian/rules: use our hacked version

    cp /git/myperl/rules debian/

Remove all example files:

    rm debian/*.ex

### TODO:

* fix debian/copyright

## Modifying the Source

### Quilt

**NOTE:** I didn't actually need quilt since I didn't end up adding 'configure'.

    cp /git/myperl/quiltrc-dpkg.rc ~/.quiltrc-dpkg
    . /git/myperl/deb.rc

Note: to use quilt:

    mkdir debian/patches
    dquilt new <patch description>.patch
    dquilt add <name of file(s) to patch>

Create 'configuration' file with the following content:


    dquilt refresh
    dquilt header -e 
    ... describe patch

### Adding 'configuration' script

    mkdir debian/patches
    dquilt new add-auto-config-wrapper.patch
    dquilt add configure
    cp /git/myperl/configure .
    dquilt refresh
    dquilt header -e
    ... describe patch

## Building the Package

    rm -rf UU
    time dpkg-buildpackage -us -uc 2>&1 | tee ../build.out

Note: this fails with an error that the package seems to be incomplete. The dh\_clean is cleaning up
a file used by the tests.

Fix debian/rules to have it's own dh\_clean.


# BUILDING SUPPLEMENTAL PACKAGES

First, install the myperl package. Then, if not already with myperl, install cpanm

    curl -L http://cpanmin.us | /opt/myperl/bin/perl - --sudo App::cpanminus

## Example Class::Std

Class::Std is installed as a native debian package. The package name is libclass-std-myperl.

    mkdir libclass-std-myperl-1.0
    cd libclass-std-myperl-1.0
    dh_make --native --single --packagename libclass-std-myperl --copyright artistic --yes


    PERL5LIB=$HOME/tmp-build/opt/myperl/lib/5.18.2/x86_64-linux:$HOME/tmp-build/opt/myperl/lib/5.18.2 \
        PERL_MB_OPT="--destdir '$HOME/tmp-build' --installdirs site --installarchlib '/opt/myperl/lib/$arch'" \
        PERL_MM_OPT="INSTALLDIRS=site DESTDIR=$HOME/tmp-build INSTALLARCHLIB=/opt/myperl/lib/5.18.2" \
        /opt/myperl/bin/cpanm Class::Std

TODO: fix path in .packlist files

### Cleaning debian/

    rm -f debian/*.ex debian/*.EX debian/*.log

# TROUBLESHOOTING

If you get an error that files aren't found, look for the line '<CPAN::Module> is up to date.'
This happens when the CPAN module is already installed:cal foreground()

