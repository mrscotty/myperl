#!/bin/bash
#
# fetch prereqs for debian/ubuntu build


if [ -e /opt/myperl/bin/perl ]; then
  echo "ERROR: myperl already installed!" >&2
  exit 1
else
  echo "INFO: myperl not installed" >&2
fi

export DEBIAN_FRONTEND=noninteractive

# for rebuilding deb pkgs...
DEBIAN_FRONTEND=noninteractive apt-get install -y make wget bzip2 debhelper devscripts build-essential fakeroot

# for building perl
DEBIAN_FRONTEND=noninteractive apt-get install -y libdb-dev libgdm-dev libbz2-dev 

# for building CPAN modules
DEBIAN_FRONTEND=noninteractive apt-get install -y openssl libssl1.0.0 libssl-dev gettext curl expat libexpat-dev libconfig-std-perl libyaml-perl libtemplate-perl libmysqlclient-dev mysql-server
