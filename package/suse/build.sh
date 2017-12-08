#!/bin/bash
#
# package/use/build.sh - Build myperl packages for SLES 11
#
# This script depends on a Vagrant SLES11 image with a few packages
# already installed. It also expects the myperl git repo to be checked
# out in the current directory on host (/vagrant on guest).

# Exit on error
set -e

basedir="$PWD"

if [ -e "$basedir/settings.rc" ]; then
    . $basedir/settings.rc
fi

# Directory where rpmbuild puts the new packages
rpmsdir=~/rpmbuild/RPMS/x86_64

# Directory where we consolidate the new packages
test -d $basedir/rpms || mkdir -p $basedir/rpms


# Clone and update openxpki repo, if needed.
# Note: the 'git pull' uses fast-forward only to abort if there are local
# modifications. 
#test -d ~/git/myperl || git clone $MYPERL_GITURL ~/git/myperl
#(cd ~/git/myperl && git checkout $MYPERL_BRANCH && git pull --ff-only)

export PERL_VERSION=$(make perl-ver-string)
if [ -z "$PERL_VERSION" ]; then
    echo "ERROR - failed to detect perl version" 1>&2
    exit 1
fi

export MYPERL_VERSION=$(make suse-ver-string)
if [ -z "$MYPERL_VERSION" ]; then
    echo "ERROR - failed to detect myperl version" 1>&2
    exit 1
fi

export MYPERL_RELEASE=$(make myperl-release)
if [ -z "$MYPERL_RELEASE" ]; then
    echo "ERROR - failed to detect myperl release" 1>&2
    exit 1
fi


# 
# myperl
#
if ! rpm -q myperl >/dev/null 2>&1; then
    make fetch-perl suse
    sudo rpm -iv --oldpackage --replacepkgs \
        ~/rpmbuild/RPMS/x86_64/myperl-$MYPERL_VERSION.x86_64.rpm
    cp -av \
        $rpmsdir/myperl-$MYPERL_VERSION.x86_64.rpm \
        $basedir/rpms
fi

#
# myperl-buildtools
#
if ! rpm -q myperl-buildtools >/dev/null 2>&1; then
    (cd package/suse/myperl-buildtools && \
    PERL5LIB=$HOME/perl5/lib/perl5 make PERL_VERSION=$PERL_VERSION)
    sudo rpm -iv --oldpackage --replacepkgs \
        ~/rpmbuild/RPMS/x86_64/myperl-buildtools-$MYPERL_VERSION.x86_64.rpm
    cp -av \
        $rpmsdir/myperl-buildtools-$MYPERL_VERSION.x86_64.rpm \
        $basedir/rpms
fi

#
# myperl-dbi
#
if ! rpm -q myperl-dbi >/dev/null 2>&1; then
    (cd package/suse/myperl-dbi && \
        PERL5LIB=$HOME/perl5/lib/perl5/ make)
    test $? == 0 || die "Error building myperl-dbi"
    sudo rpm -iv ~/rpmbuild/RPMS/x86_64/myperl-dbi-$MYPERL_VERSION.x86_64.rpm
    cp -av \
        $rpmsdir/myperl-dbi-$MYPERL_VERSION.x86_64.rpm \
        $basedir/rpms
fi

#
# myperl-fcgi
#
if ! rpm -q myperl-fcgi >/dev/null 2>&1; then
    (cd package/suse/myperl-fcgi && \
        PERL5LIB=$HOME/perl5/lib/perl5/ make)
    test $? == 0 || die "Error building myperl-fcgi"
    sudo rpm -iv ~/rpmbuild/RPMS/x86_64/myperl-fcgi-$MYPERL_VERSION.x86_64.rpm
    cp -av \
        $rpmsdir/myperl-fcgi-$MYPERL_VERSION.x86_64.rpm \
        $basedir/rpms
fi

#
# myperl-dbd-mysql
#
if ! rpm -q myperl-dbd-mysql >/dev/null 2>&1; then
    (cd package/suse/myperl-dbd-mysql && \
        PERL5LIB=$HOME/perl5/lib/perl5/ make)
    test $? == 0 || die "Error building myperl-dbd-mysql"
    sudo rpm -iv ~/rpmbuild/RPMS/x86_64/myperl-dbd-mysql-$MYPERL_VERSION.x86_64.rpm
    cp -av \
        $rpmsdir/myperl-dbd-mysql-$MYPERL_VERSION.x86_64.rpm \
        $basedir/rpms
fi

