Summary:	Compiz option code generator
Summary(pl.UTF-8):	Generator kodu opcji Compiza
Name:		compiz-bcop
Version:	0.5.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://releases.compiz-fusion.org/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	f6d5bcd605cdbf4f49f2bb7e602d3bb5
Patch0:		%{name}-pkgconfig.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libxslt-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BCOP is a code generator that provides an easy way to handle plugin
options by generating parts of the plugin code directly from the xml
metadata file. It is used for most of the Compiz Fusion plugins.

%description -l pl.UTF-8
BCOP jest generatorem kodu, który pozwala na łatwą obsługę opcji
wtyczek poprzez generowanie części kodu wtyczki bezpośrednio z pliku
xml metadanych. Jest używany przez większość wtyczek Compiz Fusion.

%prep
%setup -q
%patch0 -p1

echo "echo -n %{version}" > VERSION

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/bcop
%{_pkgconfigdir}/*
