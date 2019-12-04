#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Unix
%define		pnam	Syslog
Summary:	Unix::Syslog - Perl interface to the UNIX system logger
Summary(pl.UTF-8):	Unix::Syslog - interfejs Perla do uniksowego systemowego programu logującego
Name:		perl-Unix-Syslog
Version:	1.1
Release:	15
License:	Artistic
Group:		Development/Languages/Perl
#Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Source0:	http://search.cpan.org/CPAN/authors/id/M/MH/MHARNISCH/Unix-Syslog-%{version}.tar.gz
# Source0-md5:	73d78e309fe9508ffc9a54d84d79aac9
URL:		http://search.cpan.org/dist/Unix-Syslog/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-dirs >= 1.0-7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Unix::Syslog Perl module provides access to the system logger
available on most UNIX systems via Perl's XSUBs (Perl's C interface).

%description -l pl.UTF-8
Moduł Perla Unix::Syslog umożliwia za pośrednictwem XSUB Perla
(perlowy interfejs do C) dostęp do występującego w większości systemów
uniksowych rejestratora systemowego.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
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
%attr(755,root,root) %{perl_vendorarch}/auto/Unix/Syslog/Syslog.so
%{_mandir}/man3/*
