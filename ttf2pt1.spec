Summary:	TrueType to Adobe Type 1 font converter
Summary(pl):	Konwerter czcionek TrueType do Type1
Name:		ttf2pt1
Version:	3.4.2
Release:	1
License:	Distributable
Group:		Applications/Printing
Source0:	http://download.sourceforge.net/ttf2pt1/%{name}-%{version}.tgz
Patch0:		%{name}-am.patch
Patch1:		%{name}-nochown.patch
URL:		http://ttf2pt1.sf.net/
BuildRequires:	freetype-devel >= 2.0.4
Requires:	t1utils
Requires:	freetype > 2.0.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
True Type Font to Adobe Type 1 font converter
 - By Mark Heath <mheath@netspace.net.au>
 - Based on ttf2pfa by Andrew Weeks <ccsaw@bath.ac.uk>
 - With help from Frank M. Siegert <fms@this.net>

%description -l pl
Konwerter czcionek TrueType do Type1 autorstwa Marka Heatha
<mheath@netspace.net.au>, oparty o ttf2pfa autorstwa Andrew Weeksa
<ccsaw@bath.ac.uk>, z pomoc± Franka M. Siegerta <fms@this.net>.

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
%{__make} ttf2pt1 docs mans \
		CFLAGS_EXTT1ASM='-DEXTERNAL_T1ASM' \
		CC="%{__cc}" \
		CFLAGS_SYS='%{rpmcflags} -D_GNU_SOURCE' \
		LIBS_SYS='-lm' \
		CFLAGS_FT='-DUSE_FREETYPE -I/usr/include/freetype2 -I/usr/include' \
		CFLAGS_PREF='-DPREFER_FREETYPE' \
		LIBS_FT='-L/usr/lib -lfreetype'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/%{name},%{_datadir}/%{name},%{_mandir}/man{1,5}}

#%{__make} install INSTDIR=$RPM_BUILD_ROOT%{_prefix} \
#		BINDIR=%{_bindir} \
#		LIBXDIR=%{_libdir}/ttf2pt1 \
#		SHAREDIR=%{_datadir}/ttf2pt1 \
#		MANDIR=%{_mandir}

#install -s -m 0555 ttf2pt1 $RPM_BUILD_ROOT%{_bindir}
#install -m 0555 scripts/* $RPM_BUILD_ROOT%{_datadir}/%{name}
#chmod 0444 $RPM_BUILD_ROOT%{_datadir}/%{name}/convert.cfg.sample

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.html INSTALL INSTALL.html
#%attr(755,root,root) %{_bindir}/ttf2pt1
#%{_datadir}/%{name}
