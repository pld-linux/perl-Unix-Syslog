%include	/usr/lib/rpm/macros.perl
%define		pdir	Unix
%define		pnam	Syslog
Summary:	Perl interface to the UNIX system logger
Summary(pl):	Interfejs Perla do systemowego logera UNIX
Name:		perl-Unix-Syslog
Version:	0.98
Release:	2
License:	Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	perl >= 5.005_03-14
Requires:	perl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl interface to the UNIX system logger.

%description -l pl
Interfejs Perla do systemowego logera UNIX.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%{perl_sitearch}/Unix
%dir %{perl_sitearch}/auto/Unix
%dir %{perl_sitearch}/auto/Unix/Syslog
%{perl_sitearch}/auto/Unix/Syslog/Syslog.bs
%attr(755,root,root) %{perl_sitearch}/auto/Unix/Syslog/Syslog.so
%{_mandir}/man3/*
