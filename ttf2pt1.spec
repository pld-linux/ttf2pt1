Summary:	TrueType to Adobe Type 1 font converter
Summary(pl):	Konwerter czcionek TrueType do Type1
Name:		ttf2pt1
Version:	3.4.4
Release:	1
License:	Distributable
Group:		Applications/Printing
Source0:	http://dl.sourceforge.net/ttf2pt1/%{name}-%{version}.tgz
# Source0-md5:	cb143c07cc83167875ca09ea720d4932
Patch0:		%{name}-am.patch
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-ft2build_h.patch
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
Konwerter fontów TrueType do Type1 autorstwa Marka Heatha
<mheath@netspace.net.au>, oparty o ttf2pfa autorstwa Andrew Weeksa
<ccsaw@bath.ac.uk>, z pomoc± Franka M. Siegerta <fms@this.net>.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1

%build

%{__make} ttf2pt1 docs mans \
	CFLAGS_EXTT1ASM='-DEXTERNAL_T1ASM' \
	CC="%{__cc}" \
	CFLAGS_SYS='%{rpmcflags} -D_GNU_SOURCE' \
	LIBS_SYS='-lm' \
	CFLAGS_FT='-DUSE_FREETYPE -I/usr/include/freetype2' \
	CFLAGS_PREF='-DPREFER_FREETYPE' \
	LIBS_FT='-L/usr/lib -lfreetype' \
	INSTDIR=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTDIR=%{_prefix} \
	MANDIR=%{_mandir} \
	SHAREDIR=%{_datadir}/ttf2pt1 \
	LIBXDIR=%{_libdir}/ttf2pt1

# clean up the mess
rm -rf $RPM_BUILD_ROOT%{_datadir}/ttf2pt1/{app,other,scripts,[CFR]*}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.html COPYRIGHT FONTS.html README.html
%attr(755,root,root) %{_bindir}/ttf2pt1*
%attr(755,root,root) %{_libdir}/ttf2pt1
%{_datadir}/ttf2pt1
%{_mandir}/man1/*
