Summary:	Free replacement of the base sounds for OpenTTD
Summary(pl.UTF-8):	Darmowy zastępnik podstawowych dźwięków dla OpenTTD
Name:		openttd-opensfx
Version:	0.2.3
Release:	1
License:	GPL v2+
Group:		Applications/Games
Source0:	http://bundles.openttdcoop.org/opensfx/releases/opensfx-%{version}-source.tar.gz
# Source0-md5:	220642e895c5e490db90c01e33336f53
URL:		http://bundles.openttdcoop.org/opensfx/
BuildRequires:	catcodec
BuildRequires:	sed >= 4.0
Requires:	openttd-data
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenSFX is a free replacement of the base sounds for OpenTTD, so that
OpenTTD can be played without requiring the (copyrighted) files from
the TTD CD.

%description -l pl.UTF-8
OpenSFX to darmowy zastępnik podstawowych dźwięków dla OpenTTD, który
umożliwa granie w OpenTTD bez potrzeby wgrywania oryginalnych plików z
TTD, chronionych prawami autorskimi.

%prep
%setup -q -n opensfx-%{version}-source
%{__sed} -i 's,$(INSTALL_DIR),$(DESTDIR)$(INSTALL_DIR),' scripts/Makefile.bundles

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_DIR="%{_datadir}/openttd/data" \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/{changelog.txt,readme.txt}
%{_datadir}/openttd/data/opensfx-0.2.3.tar
