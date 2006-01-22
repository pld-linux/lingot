Summary:	LINGOT - LINGOT Is Not a Guitar-Only Tuner
Summary(pl):	LINGOT - LINGOT to nie tylko tuner gitarowy
Name:		lingot
Version:	0.6.1
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://savannah.nongnu.org/download/lingot/%{name}-%{version}.tar.gz
# Source0-md5:	0131232953c7dc85e0042caa58fc15c8
Patch0:		%{name}-makefile.patch
URL:		http://www.nongnu.org/lingot/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LINGOT is a musical instrument tuner. It's accurate, easy to use, and
highly configurable. Originally conceived to tune electric guitars.
(Tuning another instruments has not been tested).

%description -l pl
LINGOT to stroik do instrumentów. Jest dok³adny, ³atwy w u¿yciu, i
wysoce konfigurowalny. Oryginalnie stworzony do strojenia gitar
elektrycznych. (Strojenie innych instrumentów nie by³o testowane).

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.ES
%attr(755,root,root) %{_bindir}/*
