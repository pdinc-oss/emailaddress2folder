#!/usr/bin/perl

use Email::Address;
use URI::Escape;

#http://search.cpan.org/~rjbs/Email-Address-1.898/lib/Email/Address.pm

$folder="";

while(<>)
{
 if (m/^X-Original-To: *(.*)/)
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
 print '.', join('.',reverse(split /\./,  $addresses[0]->host)), '.@', uri_escape($addresses[0]->user,"^A-Za-z0-9_"), "\n";
}
else
{
 print '.@', uri_escape($folder,"^A-Za-z0-9_"), "\n";
}
