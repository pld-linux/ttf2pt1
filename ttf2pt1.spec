%define		_prefix		/usr/X11R6

Summary:	TrueType to Adobe Type 1 font converter
Summary(pl):	Konwerter czcionek TrueType do Type1
Name:		ttf2pt1
Version:	3.4.2
Release:	1
Source0:	http://download.sourceforge.net/ttf2pt1/%{name}-%{version}.tgz
Patch0:		%{name}-am.patch
Patch1:		%{name}-nochown.patch
License:	Distributable
Group:		Applications/Printing
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	freetype-devel
Requires:	t1utils
Requires:	freetype > 2.0.4
URL:		http://ttf2pt1.sf.net/

%description
True Type Font to Adobe Type 1 font converter
 - By Mark Heath <mheath@netspace.net.au>
 - Based on ttf2pfa by Andrew Weeks <ccsaw@bath.ac.uk>
 - With help from Frank M. Siegert <fms@this.net>

%description -l pl
Konwerter czcionek TrueType do Type1 autorstwa: Mark Heath
<mheath@netspace.net.au>, oparty o ttf2pfa autorstwa Andrew Weeks
<ccsaw@bath.ac.uk>, z pomoc± Frank M. Siegert <fms@this.net>

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
%{__make} ttf2pt1 docs mans \
		CFLAGS_EXTT1ASM='-DEXTERNAL_T1ASM' \
		CC="gcc" \
		CFLAGS_SYS='-O2 -D_GNU_SOURCE' \
		LIBS_SYS='-lm' \
		CFLAGS_FT='-DUSE_FREETYPE -I/usr/include/freetype2 -I/usr/include' \
		CFLAGS_PREF='-DPREFER_FREETYPE' \
		LIBS_FT='-L/usr/lib -lfreetype'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/bin
install -d $RPM_BUILD_ROOT/usr/libexec/%{name}
install -d $RPM_BUILD_ROOT/usr/share/%{name}
#mkdir -p $RPM_BUILD_ROOT/usr/share/doc-%{name}-%{version}
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install -d $RPM_BUILD_ROOT%{_mandir}/man5

#INSTDIR=$RPM_BUILD_ROOT/usr
#%{__make} install INSTDIR=$RPM_BUILD_ROOT/usr \
#		BINDIR=$INSTDIR/bin \
#		LIBXDIR=$INSTDIR/libexec/ttf2pt1 \
#		SHAREDIR=$INSTDIR/share/ttf2pt1 \
#		MANDIR=$INSTDIR/man

#install -s -m 0555 ttf2pt1 $RPM_BUILD_ROOT/usr/local/bin
#install -m 0555 scripts/* $RPM_BUILD_ROOT/usr/local/share/%{name}
#chmod 0444 $RPM_BUILD_ROOT/usr/local/share/%{name}/convert.cfg.sample

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%defattr(644, root, root, 755)
%doc README README.html INSTALL INSTALL.html
#/usr/local/bin/ttf2pt1
#/usr/local/share/%{name}
