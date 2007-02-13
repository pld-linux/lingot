Summary:	LINGOT - LINGOT Is Not a Guitar-Only Tuner
Summary(pl.UTF-8):	LINGOT - LINGOT to nie tylko tuner gitarowy
Name:		lingot
Version:	0.6.2
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://savannah.nongnu.org/download/lingot/%{name}-%{version}.tar.gz
# Source0-md5:	c9d0f11f6c5ff211c3c222a66e2d3d02
URL:		http://www.nongnu.org/lingot/
BuildRequires:	gtk+2-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LINGOT is a musical instrument tuner. It's accurate, easy to use, and
highly configurable. Originally conceived to tune electric guitars.
(Tuning another instruments has not been tested).

%description -l pl.UTF-8
LINGOT to stroik do instrumentów. Jest dokładny, łatwy w użyciu, i
wysoce konfigurowalny. Oryginalnie stworzony do strojenia gitar
elektrycznych. (Strojenie innych instrumentów nie było testowane).

%prep
%setup -q

%build
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
