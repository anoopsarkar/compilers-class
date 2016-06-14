#!/usr/bin/perl

# input grammar format:
# 0.258426966292135 SQ NP VP 
# 0.112359550561798 SQ MD NP VP 
# 0.0786516853932584 SQ VBZ NP VP 

use Getopt::Std;
my %Options;
getopts('hpg:n:t:', \%Options);

my $usage = <<EOU;

$0 -h -p -v -g <grammar> -n <num-sents> -t <toplabel>

-h   help
-p   print parentheses to get explicit tree structure
-v   increase verbosity
-g   grammar contains the PCFG
-n   num-sents is the number of sentences to produce
-t   toplabel is the start symbol

EOU

my $model;
my $len = 1;
my $printparens = 0;
my $toplabel = "program";
my $verbose = 0;

if (defined $Options{'h'}) {
    die $usage;
}

if (defined $Options{'g'}) {
    $model = $Options{'g'};
}
die $usage if (!defined $model);

if (defined $Options{'n'}) {
    $len = $Options{'n'};
}

if (defined $Options{'t'}) {
    $toplabel = $Options{'t'};
}

if (defined $Options{'p'}) {
    $printparens = 1;
}

if (defined $Options{'v'}) {
    $verbose = 1;
}

# if ($#ARGV < 1) { die "usage: $0 <grammar> <num-sents>\n"; }
# my $model = $ARGV[0];
# my $len = $ARGV[1];
# my $toplabel = "program";

my $totpr = 1.0;
my $limitpr = 1e-100;
my @out = ();
my $fail = "__FAILED__";

if ($model =~ /\.gz$/) {
    open (M, "gzip -dc $model |") or die "cannot find $model\n";
} elsif ($model =~ /\.bz2$/) {
    open (M, "bzip2 -dc $model |") or die "cannot find $model\n";
} else {
    open (M, $model) or die "cannot find $model\n";
}
print STDERR "loading model from $model...\n" if ($verbose);
while (<M>)
{
    chomp;
    my ($pr, $lhs, $rhs) = split(/\s+/, $_, 3);

    (defined $gram{$lhs}) or $gram{$lhs} = [];
    (defined $pr{$lhs}) or $pr{$lhs} = [];

    push(@{$gram{$lhs}}, $rhs);
    push(@{$pr{$lhs}}, $pr);
}
close(M);
print STDERR "done\n" if ($verbose);

sub cfggen
{
    my ($lhs, $rhs) = @_;
    my $i;

    my @rl = split(' ', $rhs);
    my $sz = $#rl + 1;

    push(@out, "LPAREN $lhs ") if ($printparens and ($sz > 0));
    for ($i = 0; $i < $sz; $i++)
    {
	my $r = pickone($rl[$i]);
        if ($out[0] eq $fail) { return; }
	cfggen($rl[$i], $r) if ($r ne "");
    }
    push(@out, " RPAREN")  if ($printparens and ($sz > 0));
}

sub pickone
{
    my $lhs = @_[0];
    my $k;

    if (!(defined $gram{$lhs})) {
	push(@out, $lhs);
	return("");
    }

    (defined $pr{$lhs}) or die "could not find pr table for: $lhs\n";

    my @tl = @{$gram{$lhs}};
    my @prl = @{$pr{$lhs}};
    my $tlen = $#tl + 1;

    my $prob_out = rand();
    my $accum = 0.0;
    my $ind = $tlen-1;

    # pick rule to expand
    for ($k = 0; $k < $tlen; $k++)
    {
	if ($prob_out < ($prl[$k] + $accum)) { $ind = $k; last; }
	else { $accum += $prl[$k]; }
    }
    $totpr *= $prl[$ind];
    if ($totpr < $limitpr) { @out = ($fail); return(""); }
    return($tl[$ind]);
}

for (my $i = 0; $i < $len; $i++)
{
    $totpr = 1.0;
    @out = ();
    cfggen($toplabel, pickone($toplabel));
    if ($out[0] eq $fail) { $i--; next; }
    if ($printparens) {
	my $outstr = join(' ', @out);
	$outstr =~ s/\(/LPRN/g;
	$outstr =~ s/\)/RPRN/g;
	$outstr =~ s/\{/LCB/g;
	$outstr =~ s/\}/RCB/g;
	$outstr =~ s/LPAREN/(/g;
	$outstr =~ s/RPAREN/)/g;
	print "$outstr\n";
    } else {
	print join(' ', @out), "\n"; # print " :$totpr\n";
    }
}

