#!/usr/bin/perl

use strict;

my $usage = "$0 cfgfile\n";
my $file = shift or die $usage;
my %cfgrule = ();
my @rules = ();

open(F, $file) or die $usage;
my $line;
while ($line = <F>) {
  chomp($line);
  my ($lhs, $rhs) = split(' ', $line, 2);
  $cfgrule{$lhs}->{$rhs} = 1;
  push(@rules, [$lhs, $rhs]);
}
close(F);

for my $lhs (keys %cfgrule) {
  my @rhslist = keys %{$cfgrule{$lhs}};
  my $rhslen = scalar(@rhslist);
  for my $rhs (@rhslist) {
     $cfgrule{$lhs}->{$rhs} = 1 / $rhslen;
  }
}

for my $rule (@rules) {
  my $lhs = $rule->[0];
  my $rhs = $rule->[1];
  my $prob = $cfgrule{$lhs}->{$rhs};
  print "$prob $lhs $rhs\n";
}

1;

