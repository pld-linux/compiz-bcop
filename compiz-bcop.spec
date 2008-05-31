Summary:	Compiz option code generator
Summary(pl.UTF-8):	Generator kodu opcji Compiza
Name:		compiz-bcop
Version:	0.7.6
Release:	1
License:	GPL v2+
Group:		Development/Tools
Source0:	http://releases.compiz-fusion.org/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	a35d3e3c614577061ef0fb50b1cdb7f5
URL:		http://forum.compiz-fusion.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.9
# only for configure check
BuildRequires:	libxslt-devel
BuildRequires:	pkgconfig
Requires:	/usr/bin/getopt
# xsltproc
Requires:	libxslt-progs
Requires:	pkgconfig >= 1:0.19
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noarchpkgconfigdir	%{_datadir}/pkgconfig

%description
BCOP is a code generator that provides an easy way to handle plugin
options by generating parts of the plugin code directly from the XML
metadata file. It is used for most of the Compiz Fusion plugins.

%description -l pl.UTF-8
BCOP jest generatorem kodu, który pozwala na łatwą obsługę opcji
wtyczek poprzez generowanie części kodu wtyczki bezpośrednio z pliku
XML metadanych. Jest używany przez większość wtyczek Compiz Fusion.

%prep
%setup -q

echo "echo -n %{version}" > VERSION

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

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
%doc AUTHORS
%attr(755,root,root) %{_bindir}/bcop
%{_datadir}/bcop
%{_noarchpkgconfigdir}/bcop.pc
