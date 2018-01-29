Name:           emailAddress2Folder
Version:        2
Release:        1%{?dist}
Summary:        A Perl procmail helper to create Maildir folder names based on the email address of the recipient

Group:          Development/Libraries
License:        BSD
URL:            http://127.0.0.1
Source0:        http://127.0.0.1/emailAddress2Folder-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
Requires:	perl(URI)
Requires:	perl(Email::Address)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))


%description 
This utility converts the email address specified in X-Original-To header in to a Maildir folder name.
The folder name is most significant first format. Example: test@test.com becomes .com.test.@test. 
If the email address has characters not supported then they are URI encoded.



%prep
%setup -q -c Email-Address-%{version}
#-n Email-Address-%{version}

%build
#%{__perl} Makefile.PL INSTALLDIRS=vendor
#make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

mkdir -p "$RPM_BUILD_ROOT/%{_bindir}/"

cp emailaddress2folder.pl "$RPM_BUILD_ROOT/%{_bindir}/"


#make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
#find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
#find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
#chmod -R u+w $RPM_BUILD_ROOT/*

#for file in Changes; do
#  iconv -f iso-8859-1 -t utf-8 < "$file" > "${file}_"
#  mv -f "${file}_" "$file"
#done


%clean 
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/emailaddress2folder.pl


%changelog
* Sun Jan 28 2018 Jason Pyeron <support@pdinc.us> - 2-1
- added support for TO/FROM based processing

* Tue May 28 2013 Jason Pyeron <support@pdinc.us> - 1-1
- dependency corrections

* Tue May 28 2013 Jason Pyeron <support@pdinc.us> - 1-0
- initial build
