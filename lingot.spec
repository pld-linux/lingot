Summary:	LINGOT - LINGOT Is Not a Guitar-Only Tuner
Summary(pl.UTF-8):	LINGOT - LINGOT to nie tylko tuner gitarowy
Name:		lingot
Version:	0.9.1
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://savannah.nongnu.org/download/lingot/%{name}-%{version}.tar.gz
# Source0-md5:	5a61c88e3770270246385ab9dbc39793
URL:		http://www.nongnu.org/lingot/
BuildRequires:	gettext-tools
BuildRequires:	gtk+2-devel
BuildRequires:	jack-audio-connection-kit-devel >= 0.102.0
BuildRequires:	libglade2-devel
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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README NEWS THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/lingot
%{_pixmapsdir}/lingot
%{_desktopdir}/lingot.desktop
