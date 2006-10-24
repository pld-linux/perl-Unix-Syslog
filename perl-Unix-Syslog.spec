#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Unix
%define		pnam	Syslog
Summary:	Unix::Syslog - Perl interface to the UNIX system logger
Summary(pl):	Unix::Syslog - interfejs Perla do uniksowego systemowego programu loguj±cego
Name:		perl-Unix-Syslog
Version:	0.99
Release:	5
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0f16c5e4e65cb51df9a0342318b1f221
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
Requires:	perl-dirs >= 1.0-7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Unix::Syslog Perl module provides access to the system logger
available on most UNIX systems via Perl's XSUBs (Perl's C interface).

%description -l pl
Modu³ Perla Unix::Syslog umo¿liwia za po¶rednictwem XSUB Perla
(perlowy interfejs do C) dostêp do wystêpuj±cego w wiêkszo¶ci systemów
uniksowych rejestratora systemowego.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%{perl_vendorarch}/Unix/*
%dir %{perl_vendorarch}/auto/Unix/Syslog
%{perl_vendorarch}/auto/Unix/Syslog/Syslog.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Unix/Syslog/Syslog.so
%{_mandir}/man3/*
