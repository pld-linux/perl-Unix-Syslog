#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	Unix
%define		pnam	Syslog
Summary:	Perl interface to the UNIX system logger
Summary(pl):	Interfejs Perla do systemowego logera UNIX
Name:		perl-Unix-Syslog
Version:	0.99
Release:	2
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl >= 5.005_03-14
Requires:	perl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Th Unix::Syslog Perl module provides access to the system logger
available on most UNIX systems via Perl's XSUBs (Perl's C interface).

%description -l pl
Moduł Perla Unix::Syslog umożliwia za pośrednictwem XSUB Perla
(perlowy interfejs do C) dostęp do występującego w większosci systemów
uniksowych rejestratora systemowego.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%{perl_vendorarch}/Unix
%dir %{perl_vendorarch}/auto/Unix
%dir %{perl_vendorarch}/auto/Unix/Syslog
%{perl_vendorarch}/auto/Unix/Syslog/autosplit.ix
%{perl_vendorarch}/auto/Unix/Syslog/Syslog.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Unix/Syslog/Syslog.so
%{_mandir}/man3/*
