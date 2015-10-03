#!/usr/bin/env perl
#

use strict;
use warnings;

use Test::More;


############################################################
# Check that specific files exist (and are not empty)
############################################################
#ok(-s '/opt/myperl/bin/cpanm', "cpanm exists");
is(`dpkg -S /opt/myperl/bin/perl`, "myperl: /opt/myperl/bin/perl\n",
    "myperl is installed");

############################################################
# Check that each package was installed
############################################################

if ( 0 ) {
my $fh;

open( $fh, 'find /opt/myperl|' ) or die "Error running find: $!";

my $dirlist = [];
while (<$fh>) {
    chomp;
    next if m{^(/\.|/opt|/opt/myperl)$};
    push @{ $dirlist }, $_;
}
close $fh or die "Error closing find filehandle: $!";
$dirlist = [ sort @{ $dirlist } ];

my $pkgfilelisthash = {};
foreach my $pkg (qw( myperl myperl-dbd-mysql myperl-openxpki-core-deps myperl-openxpki-core)) {
    open( $fh, "dpkg -L $pkg|" ) or die "Error running 'dpkg -L $pkg': $!";
    while (<$fh>) {
        chomp;
        next if m{^(/\.|/opt|/opt/myperl|/etc.*|/usr.*|/var.*)$};
        $pkgfilelisthash->{$_}++;
    }
}
my $pkgfilelist = [ sort keys %{ $pkgfilelisthash } ];

is_deeply( $dirlist, $pkgfilelist, 'compare installed packages with actual file list' );
}

done_testing();
