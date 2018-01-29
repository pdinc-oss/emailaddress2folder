#!/usr/bin/perl

use Email::Address;
use URI::Escape;

#http://search.cpan.org/~rjbs/Email-Address-1.898/lib/Email/Address.pm

my $mode;
my $prefix;

if (@ARGV==0)
{
 $mode="DEFAULT";
 $prefix="";
}
else
{
 $mode=$ARGV[0];
 $prefix=".$mode";
 shift
}

if ($mode eq "FROM" )
{
	$PAT='Return-Path';
}
else
{
	$PAT='X-Original-To';
}


$folder="";

while(<>)
{
 if (m/^$PAT: *(.*)/)
 {
  $folder=$1;
  break;
 }
}

if ($folder eq "")
{
 print "\n";
 exit;
}


my @addresses = Email::Address->parse($folder);

if (defined $addresses[0])
{
 print $prefix,'.', join('.',reverse(split /\./,  $addresses[0]->host)), '.@', uri_escape($addresses[0]->user,"^A-Za-z0-9_"), "\n";
}
else
{
 print $prefix,'.@', uri_escape($folder,"^A-Za-z0-9_"), "\n";
}
