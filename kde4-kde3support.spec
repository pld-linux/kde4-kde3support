#
# Conditional build:
%bcond_without	alsa			# build without ALSA support
%bcond_with	arts			# build with aRts support
%bcond_with	jasper			# build with jasper support
%bcond_without	autoreqdep		# don't care about package name deps generated by rpm
%bcond_without	kerberos5		# disable kerberos
%bcond_without	hidden_visibility	# no gcc hidden visibility

%define		_state		stable
%define		origname	kdelibs
%define     artsver     13:1.5.10
Summary:	K Desktop Environment 3 libraries
Summary(es.UTF-8):	K Desktop Environment 3 - bibliotecas
Summary(ko.UTF-8):	KDE 3 - 라이브러리
Summary(pl.UTF-8):	Biblioteki K Desktop Environment 3
Summary(pt_BR.UTF-8):	Bibliotecas de fundação do KDE 3
Summary(ru.UTF-8):	K Desktop Environment 3 - Библиотеки
Summary(uk.UTF-8):	K Desktop Environment 3 - Бібліотеки
Name:		kde4-kde3support
Version:	3.5.10
Release:	61
License:	LGPL v2
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{origname}-%{version}.tar.bz2
# Source0-md5:	43cd55ed15f63b5738d620ef9f9fd568
Source1:	http://everaldo.com/crystal/crystal_project.tar.gz
# Source1-md5:	338dfdb8918e0bb1085bd8109efd71df
Patch0:		kde-ac260-lt.patch
Patch1:		kde-common-PLD.patch
Patch2:		kdelibs-lib_loader.patch
Patch3:		kdelibs-inotify.patch
Patch4:		kde-am.patch
Patch5:		kdelibs-gcc4.patch
Patch6:		%{name}-ac.patch
Patch7:		crystalsvg-theme_index.patch
Patch8:		openssl1.patch
Patch9:		%{name}-qt4.patch
Patch10:	boost-1.50.patch
Patch11:	kdelibs-cups16.patch
Patch12:	kdelibs-cups20.patch
Patch13:	kdelibs-cups22.patch
Patch14:	gcc6.patch
Patch15:	gcc7.patch
Patch16:	openssl-1.1.patch
Patch17:	x32.patch
URL:		http://www.kde.org/
BuildRequires:	OpenEXR-devel >= 1.4.0.a
BuildRequires:	acl-devel
%{?with_alsa:BuildRequires:	alsa-lib-devel}
%{?with_arts:BuildRequires:	arts-qt-devel >= %{artsver}}
%{?with_arts:BuildRequires:	artsc-devel >= %{artsver}}
BuildRequires:	aspell-devel
BuildRequires:	audiofile-devel
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.6.1
BuildRequires:	boost-devel >= 1.35.0
BuildRequires:	bzip2-devel
BuildRequires:	cups-devel >= 1:1.3.0
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	docbook-utils
BuildRequires:	ed
BuildRequires:	fam-devel
%{?with_hidden_visibility:BuildRequires:	gcc-c++ >= 5:4.1.0-0.20051206r108118.1}
BuildRequires:	gettext-tools
# <sys/inotify.h>
BuildRequires:	glibc-devel >= 6:2.4
%{?with_kerberos5:BuildRequires:	heimdal-devel}
BuildRequires:	hspell-devel
%{?with_jasper:BuildRequires:	jasper-devel >= 1.600}
BuildRequires:	libart_lgpl-devel
BuildRequires:	libidn-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmad-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel >= 2.0
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 2:1.5-2
BuildRequires:	libvorbis-devel
BuildRequires:	libwmf-devel >= 2:0.2.0
BuildRequires:	libxml2-devel >= 2.4.9
BuildRequires:	libxml2-progs
BuildRequires:	libxslt-devel >= 1.0.7
BuildRequires:	lua50-devel
BuildRequires:	mdns-bonjour-devel
BuildRequires:	motif-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pcre-devel >= 3.5
BuildRequires:	pkgconfig
BuildRequires:	qt-devel >= 6:3.3.3-4
%{?with_hidden_visibility:BuildRequires:	qt-devel >= 6:3.3.5.051113-1}
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpmbuild(macros) >= 1.129
#BuildRequires:	unsermake >= 040511
BuildRequires:	zlib-devel
BuildRequires:	zstd-devel
%if %{with autoreqdep}
BuildConflicts:	kdebase-core < 9:3.4.0
BuildConflicts:	kdepim-korganizer-libs
BuildConflicts:	kdepim-libkdepim < 3:3.3.0
%endif
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
%{?with_arts:Requires:	arts >= %{artsver}}
Requires:	docbook-dtd412-xml
Requires:	docbook-dtd42-xml
Requires:	docbook-style-xsl
Requires:	hicolor-icon-theme
Requires:	kde-common-dirs >= 0.5
Requires:	libxml2-progs
Requires:	qt >= 6:3.3.3-4
Requires:	setup >= 2.4.6-7
Requires:	xorg-app-iceauth
Provides:	kdelibs = 9:%{version}-%{release}
Obsoletes:	kde4-icons-crystalsvg < 4.3.0
Obsoletes:	kdelibs < 9:%{version}-%{release}
# for meinproc4 - it's not Requeres on purpose
# not everyone needs meinproc4 and not everyone want's kde4 while having kde3 apps
Suggests:	kde4-kdelibs
Conflicts:	sim < 0.9.3-4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# confuses OpenEXR detection
%undefine	configure_cache

# kde3 does not work well with ccache (CC with spaces)
%unglobal	with_ccache

%define		no_install_post_check_so	1
# unresolved symbols in libkscreensaver.so.X (by design)

%description
This package includes libraries that are central to the development
and execution of a KDE 3 programs, misc HTML documentation and theme
modules.

Included in this package are among others:
- kdecore - KDE core library,
- kdeui - KDE user interface library,
- khtml - KDE HTML widget with javascript and CSS support,
- kwallet - KDE password manager.

%description -l es.UTF-8
Bibliotecas para KDE 3.

%description -l pl.UTF-8
Ten pakiet zawiera biblioteki potrzebne do rozwijania i uruchamiania
aplikacji KDE 3, różną dokumentację oraz moduły z motywami wyglądu
KDE.

Pakiet ten zawiera między innymi:
- kdecore - podstawową bibliotekę KDE,
- kdeui - interfejs użytkownika KDE,
- khtml - obsługę HTML, javascript oraz CSS dla KDE,
- kwallet - system zarządzania hasłami w KDE.

%description -l pt_BR.UTF-8
Bibliotecas de fundação do KDE 3 requeridas por todo e qualquer
aplicativo KDE.

%description -l ru.UTF-8
Библиотеки для K Desktop Environment 3.

Включены библиотеки KDE:
- jscript (javascript),
- kdecore (ядро KDE),
- kdeui (интерфейс пользователя),
- khtmlw (работа с HTML),
- kimgio (обработка изображений).
- kspell (проверка орфографии),

%description -l uk.UTF-8
Бібліотеки для K Desktop Environment 3.

Включені такі бібліотеки KDE:
- jscript (javascript),
- kdecore (ядро KDE),
- kdeui (інтерфейс користувача),
- khtmlw (робота з HTML),
- kimgio (обробка зображень).
- kspell (перевірка орфографії),

%package libs
Summary:	KDE 3 libraries
Summary(pl.UTF-8):	Biblioteki KDE 3
Group:		Libraries
Requires:	cups-lib >= 1:1.3.0
Obsoletes:	kdelibs-libs

%description libs
KDE 3 libraries.

%description libs -l pl.UTF-8
Biblioteki KDE 3.

%package devel
Summary:	kdelibs 3 - header files and development documentation
Summary(pl.UTF-8):	kdelibs 3 - pliki nagłówkowe i dokumentacja do kdelibs
Summary(pt_BR.UTF-8):	Arquivos de inclusão e documentação para compilar aplicativos KDE 3
Summary(ru.UTF-8):	Хедеры и документация для компилляции программ KDE 3
Summary(uk.UTF-8):	Хедери та документація для компіляції програм KDE 3
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	acl-devel
%{?with_arts:Requires:	arts-qt-devel >= %{artsver}}
%{?with_arts:Requires:	artsc-devel >= %{artsver}}
Requires:	fam-devel
Requires:	libart_lgpl-devel
Requires:	libidn-devel
Requires:	mdns-bonjour-devel
Requires:	pcre-devel
Requires:	qt-devel >= 6:3.3.3-4
Requires:	xorg-lib-libXmu-devel
Requires:	xorg-lib-libXt-devel
%{?with_arts:Obsoletes:	arts-kde-devel}
Obsoletes:	kdelibs-devel
Obsoletes:	kdelibs-sound-devel
Obsoletes:	kdelibs-static
Obsoletes:	kdelibs2-devel
Obsoletes:	kdelibs2-sound-devel
Obsoletes:	kttsd-devel
Conflicts:	kdebase-devel <= 9:3.1.90

%description devel
This package contains header files and development documentation for
kdelibs.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe i dokumentację potrzebną przy
pisaniu własnych programów wykorzystujących kdelibs.

%description devel -l pt_BR.UTF-8
Este pacote contém os arquivos de inclusão que são necessários para
compilar aplicativos KDE.

%description devel -l ru.UTF-8
Этот пакет содержит хедеры, необходимые для компиляции программ для
KDE.

%description devel -l uk.UTF-8
Цей пакет містить хедери, необхідні для компіляції програм для KDE.

%prep
%setup -q -n %{origname}-%{version} -a1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1

mv -f configure{,.dist}
:>admin/test-driver

%build
# merge cacert root certificate
cd kio/kssl/kssl
./mergelocal
cd -

cd kabc/scripts
./makeaddressee
cd -

cp /usr/share/automake/config.sub admin
export kde_htmldir=%{_kdedocdir}
export kde_libs_htmldir=%{_kdedocdir}
if [ ! -f configure ]; then
	%{__make} -f admin/Makefile.common cvs
fi

export path_sudo=%{_bindir}/sudo
export CXXFLAGS="%{rpmcxxflags} -Wno-narrowing"
%configure \
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	%{!?debug:--disable-rpath} \
	--disable-final \
	%{?with_hidden_visibility:--enable-gcc-hidden-visibility} \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
%if "%{_lib}" == "libx32"
	--enable-libsuffix=x32 \
%endif
	--enable-mitshm \
	--with%{!?with_alsa:out}-alsa \
	--with%{!?with_arts:out}-arts \
	--with-distribution="PLD Linux Distribution" \
	--with-ldap=no \
	--with-lua-includes=%{_includedir}/lua50 \
	--with-qt-libraries=%{_libdir} \
	--with-sudo-kdesu-backend \
	--oldincludedir=%{_includedir}/kde3

%{__make}
rm -f makeinstall.stamp

%install
rm -rf $RPM_BUILD_ROOT
if [ ! -f makeinstall.stamp -o ! -d $RPM_BUILD_ROOT ]; then
	rm -rf makeinstall.stamp installed.stamp $RPM_BUILD_ROOT

	%{__make} install \
		DESTDIR=$RPM_BUILD_ROOT \
		kde_htmldir=%{_kdedocdir}
		kde_libs_htmldir=%{_kdedocdir}
	touch makeinstall.stamp
fi

if [ ! -f installed.stamp ]; then
	install -d \
		$RPM_BUILD_ROOT/etc/security \
		$RPM_BUILD_ROOT%{_libdir}/kconf_update_bin \
		$RPM_BUILD_ROOT%{_libdir}/kde3dev \
		$RPM_BUILD_ROOT%{_datadir}/applnk/.hidden \
		$RPM_BUILD_ROOT%{_datadir}/services/kconfiguredialog \

	mv $RPM_BUILD_ROOT%{_includedir} $RPM_BUILD_ROOT/kde3inc
	install -d $RPM_BUILD_ROOT%{_includedir}
	mv $RPM_BUILD_ROOT/kde3inc $RPM_BUILD_ROOT%{_includedir}/kde3
	# packaged by hicolor-icon-theme
	%{__rm} $RPM_BUILD_ROOT%{_iconsdir}/hicolor/index.theme

	# remove *.la for dynamic plugins. kde lib loader handles .so now.
	%{__rm} $RPM_BUILD_ROOT%{_libdir}/kde3/*.la
	# keep $RPM_BUILD_ROOT%{_libdir}/kde3/plugins/designer/kdewidget.la for kdebase and others.
	%{__rm} $RPM_BUILD_ROOT%{_libdir}/kde3/plugins/styles/*.la
	%{__rm} $RPM_BUILD_ROOT%{_libdir}/libkdeinit_*.la
	%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/{apps,doc,locale,config,emoticons}
	%{__rm} -r $RPM_BUILD_ROOT/etc
	%{?with_arts:%{__rm} $RPM_BUILD_ROOT%{_bindir}/artsmessage}
	%{__rm} $RPM_BUILD_ROOT%{_bindir}/{checkXML,kgrantpty,ksvgtopng,kunittestmodrunner,makekdewidgets,kconfig_compiler}

	# install actual crystalsvg icons
	%{__rm} -r $RPM_BUILD_ROOT%{_iconsdir}
	install -d $RPM_BUILD_ROOT%{_iconsdir}/crystalsvg
	cp -a crystal_project/*/ $RPM_BUILD_ROOT%{_iconsdir}/crystalsvg
	cp -p crystal_project/index.theme $RPM_BUILD_ROOT%{_iconsdir}/crystalsvg

	# remove meinproc binary and link to meinproc4 which works
	%{__rm} $RPM_BUILD_ROOT%{_bindir}/meinproc
	ln -s %{_bindir}/meinproc4 $RPM_BUILD_ROOT%{_bindir}/meinproc

	%{__rm} $RPM_BUILD_ROOT%{_bindir}/preparetips

	# remove unwanted boost deps from .la
	sed -i 's:-lboost_filesystem -lboost_system -lboost_regex::' $RPM_BUILD_ROOT%{_libdir}/kde3/plugins/designer/kdewidgets.la
	%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
	%{__rm} $RPM_BUILD_ROOT%{_libdir}/kde3/plugins/designer/kdewidgets.la

	touch installed.stamp
fi

# put symlinks to a different folder in %_libdir
cd $RPM_BUILD_ROOT%{_libdir}
for link in $(ls *.so); do
	sover=$(ls $link.*.*.* | sed -e s@$link@@)
	if [ -h $link ]; then
		%{__rm} $link
		ln -s ../$link$sover kde3dev/$link
	fi
done
mv libkdefakes_nonpic.a kde3dev
cd -

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cupsdconf
%attr(755,root,root) %{_bindir}/cupsdoprint
%attr(755,root,root) %{_bindir}/dcop
%attr(755,root,root) %{_bindir}/dcopclient
%attr(755,root,root) %{_bindir}/dcopfind
%attr(755,root,root) %{_bindir}/dcopidlng
%attr(755,root,root) %{_bindir}/dcopobject
%attr(755,root,root) %{_bindir}/dcopquit
%attr(755,root,root) %{_bindir}/dcopref
%attr(755,root,root) %{_bindir}/dcopserver
%attr(755,root,root) %{_bindir}/dcopserver_shutdown
%attr(755,root,root) %{_bindir}/dcopstart
#%attr(755,root,root) %{_bindir}/ghns
%attr(2755,root,fileshare) %{_bindir}/filesharelist
%attr(2755,root,fileshare) %{_bindir}/fileshareset
%attr(755,root,root) %{_bindir}/imagetops
%attr(755,root,root) %{_bindir}/kaddprinterwizard
%attr(755,root,root) %{_bindir}/kbuildsycoca
%attr(755,root,root) %{_bindir}/kcmshell
%attr(755,root,root) %{_bindir}/kconf_update
%attr(755,root,root) %{_bindir}/kcookiejar
%attr(755,root,root) %{_bindir}/kde-config
%attr(755,root,root) %{_bindir}/kde-menu
%attr(755,root,root) %{_bindir}/kded
%attr(755,root,root) %{_bindir}/kdeinit
%attr(755,root,root) %{_bindir}/kdeinit_shutdown
%attr(755,root,root) %{_bindir}/kdeinit_wrapper
%attr(755,root,root) %{_bindir}/kdesu_stub
%attr(755,root,root) %{_bindir}/kdontchangethehostname
%attr(755,root,root) %{_bindir}/kdostartupconfig
%attr(755,root,root) %{_bindir}/kfile
%attr(755,root,root) %{_bindir}/kfmexec
%attr(755,root,root) %{_bindir}/khotnewstuff
# removed?
#%attr(755,root,root) %{_bindir}/kimage_concat
%attr(755,root,root) %{_bindir}/kinstalltheme
%attr(755,root,root) %{_bindir}/kio_http_cache_cleaner
%attr(755,root,root) %{_bindir}/kio_uiserver
%attr(755,root,root) %{_bindir}/kioexec
%attr(755,root,root) %{_bindir}/kioslave
%attr(755,root,root) %{_bindir}/klauncher
# use kmailservice from kde 4.10
#%attr(755,root,root) %{_bindir}/kmailservice
%attr(755,root,root) %{_bindir}/kpac_dhcp_helper
%attr(755,root,root) %{_bindir}/ksendbugmail
%attr(755,root,root) %{_bindir}/kshell
%attr(755,root,root) %{_bindir}/kstartupconfig
# use ktelnetservice from kde 4.10
#%attr(755,root,root) %{_bindir}/ktelnetservice
%attr(755,root,root) %{_bindir}/ktradertest
%attr(755,root,root) %{_bindir}/kwrapper
%attr(755,root,root) %{_bindir}/lnusertemp
%attr(755,root,root) %{_bindir}/make_driver_db_cups
%attr(755,root,root) %{_bindir}/make_driver_db_lpr
# use link to meinproc4
%attr(755,root,root) %{_bindir}/meinproc
# use preparetips from kde 4.4
#%attr(755,root,root) %{_bindir}/preparetips
%attr(4755,root,root) %{_bindir}/start_kdeinit
%attr(755,root,root) %{_bindir}/start_kdeinit_wrapper

%{_datadir}/mimelnk
%dir %{_datadir}/services/kresources
%{_datadir}/services/kresources/kabc_manager.desktop
%{_datadir}/services/kded
%{_datadir}/services/http_cache_cleaner.desktop
%{_datadir}/services/katepart.desktop
%{_datadir}/services/kbzip2filter.desktop
%{_datadir}/services/kcertpart.desktop
%{_datadir}/services/kgzipfilter.desktop
%{_datadir}/services/khtml.desktop
%{_datadir}/services/khtmlimage.desktop
%{_datadir}/services/kio_uiserver.desktop
%{_datadir}/services/kjavaappletviewer.desktop
%{_datadir}/services/kmailservice.protocol
%{_datadir}/services/kmultipart.desktop
%{_datadir}/services/knotify.desktop
%{_datadir}/services/kspell_aspell.desktop
%{_datadir}/services/kspell_ispell.desktop
%{_datadir}/services/kspell_hspell.desktop
%{_datadir}/services/ktexteditor_docwordcompletion.desktop
%{_datadir}/services/ktexteditor_insertfile.desktop
%{_datadir}/services/ktexteditor_isearch.desktop
%{_datadir}/services/ktexteditor_kdatatool.desktop
%{_datadir}/services/bmp.kimgio
%{_datadir}/services/dds.kimgio
%{_datadir}/services/eps.kimgio
%{_datadir}/services/exr.kimgio
%{_datadir}/services/gif.kimgio
%{_datadir}/services/hdr.kimgio
%{_datadir}/services/ico.kimgio
%{?with_jasper:%{_datadir}/services/jp2.kimgio}
%{_datadir}/services/jpeg.kimgio
#%{_datadir}/services/krl.kimgio
%{_datadir}/services/mng.kimgio
%{_datadir}/services/pbm.kimgio
%{_datadir}/services/pcx.kimgio
%{_datadir}/services/pgm.kimgio
%{_datadir}/services/png.kimgio
%{_datadir}/services/ppm.kimgio
%{_datadir}/services/psd.kimgio
%{_datadir}/services/rgb.kimgio
%{_datadir}/services/tga.kimgio
%{_datadir}/services/tiff.kimgio
%{_datadir}/services/xbm.kimgio
%{_datadir}/services/xcf.kimgio
%{_datadir}/services/xpm.kimgio
%{_datadir}/services/xv.kimgio
%{_datadir}/services/data.protocol
%{_datadir}/services/file.protocol
%{_datadir}/services/ftp.protocol
%{_datadir}/services/ghelp.protocol
%{_datadir}/services/help.protocol
%{_datadir}/services/http.protocol
%{_datadir}/services/https.protocol
%{_datadir}/services/metainfo.protocol
%{_datadir}/services/mms.protocol
%{_datadir}/services/pnm.protocol
%{_datadir}/services/rlogin.protocol
%{_datadir}/services/rtsp.protocol
%{_datadir}/services/shellscript.desktop
%{_datadir}/services/ssh.protocol
%{_datadir}/services/telnet.protocol
%{_datadir}/services/webdav.protocol
%{_datadir}/services/webdavs.protocol
%{_datadir}/services/mmst.protocol
%{_datadir}/services/mmsu.protocol
%{_datadir}/services/rtspt.protocol
%{_datadir}/services/rtspu.protocol
%{_datadir}/servicetypes
%dir %{_desktopdir}/kde
%{_iconsdir}/crystalsvg

# 3rdparty directories
%dir %{_datadir}/services/kconfiguredialog

# merged kabc files
%attr(755,root,root) %{_bindir}/kab2kabc
%{_datadir}/autostart/kab2kabc.desktop
%{_datadir}/services/kresources/kabc
%{_desktopdir}/kde/kresources.desktop

%files libs
%defattr(644,root,root,755)
%dir %{_libdir}/kde3
%dir %{_libdir}/kde3/plugins
%dir %{_libdir}/kde3/plugins/designer
%attr(755,root,root) %{_libdir}/kde3/plugins/designer/kdewidgets.so
%dir %{_libdir}/kde3/plugins/styles
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/highcolor.so
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/highcontrast.so
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/keramik.so
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/kthemestyle.so
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/light.so
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/plastik.so
%attr(755,root,root) %{_libdir}/kde3/cupsdconf.so
%attr(755,root,root) %{_libdir}/kde3/dcopserver.so
%attr(755,root,root) %{_libdir}/kde3/kaddprinterwizard.so
%attr(755,root,root) %{_libdir}/kde3/kbuildsycoca.so
%attr(755,root,root) %{_libdir}/kde3/kbzip2filter.so
%attr(755,root,root) %{_libdir}/kde3/kcmshell.so
%attr(755,root,root) %{_libdir}/kde3/kconf_update.so
%attr(755,root,root) %{_libdir}/kde3/kcookiejar.so
%attr(755,root,root) %{_libdir}/kde3/kded.so
%attr(755,root,root) %{_libdir}/kde3/kded_kcookiejar.so
%attr(755,root,root) %{_libdir}/kde3/kded_kdeprintd.so
%attr(755,root,root) %{_libdir}/kde3/kded_kdetrayproxy.so
%attr(755,root,root) %{_libdir}/kde3/kded_kpasswdserver.so
%attr(755,root,root) %{_libdir}/kde3/kded_kssld.so
%attr(755,root,root) %{_libdir}/kde3/kded_kwalletd.so
%attr(755,root,root) %{_libdir}/kde3/kded_proxyscout.so
%attr(755,root,root) %{_libdir}/kde3/kdeprint_cups.so
%attr(755,root,root) %{_libdir}/kde3/kdeprint_ext.so
%attr(755,root,root) %{_libdir}/kde3/kdeprint_lpdunix.so
%attr(755,root,root) %{_libdir}/kde3/kdeprint_lpr.so
%attr(755,root,root) %{_libdir}/kde3/kdeprint_rlpr.so
%attr(755,root,root) %{_libdir}/kde3/kdeprint_tool_escputil.so
%if %{with arts}
%attr(755,root,root) %{_libdir}/kde3/kfileaudiopreview.so
%endif
%attr(755,root,root) %{_libdir}/kde3/kgzipfilter.so
%attr(755,root,root) %{_libdir}/kde3/khtmlimagepart.so
%attr(755,root,root) %{_libdir}/kde3/kimg_dds.so
%attr(755,root,root) %{_libdir}/kde3/kimg_eps.so
%attr(755,root,root) %{_libdir}/kde3/kimg_exr.so
%attr(755,root,root) %{_libdir}/kde3/kimg_hdr.so
%attr(755,root,root) %{_libdir}/kde3/kimg_ico.so
%{?with_jasper:%attr(755,root,root) %{_libdir}/kde3/kimg_jp2.so}
%attr(755,root,root) %{_libdir}/kde3/kimg_pcx.so
%attr(755,root,root) %{_libdir}/kde3/kimg_psd.so
%attr(755,root,root) %{_libdir}/kde3/kimg_rgb.so
%attr(755,root,root) %{_libdir}/kde3/kimg_tga.so
%attr(755,root,root) %{_libdir}/kde3/kimg_tiff.so
%attr(755,root,root) %{_libdir}/kde3/kimg_xcf.so
%attr(755,root,root) %{_libdir}/kde3/kimg_xview.so
%attr(755,root,root) %{_libdir}/kde3/kio_file.so
%attr(755,root,root) %{_libdir}/kde3/kio_ftp.so
%attr(755,root,root) %{_libdir}/kde3/kio_ghelp.so
%attr(755,root,root) %{_libdir}/kde3/kio_help.so
%attr(755,root,root) %{_libdir}/kde3/kio_http.so
%attr(755,root,root) %{_libdir}/kde3/kio_http_cache_cleaner.so
%attr(755,root,root) %{_libdir}/kde3/kio_metainfo.so
%attr(755,root,root) %{_libdir}/kde3/kio_uiserver.so
%attr(755,root,root) %{_libdir}/kde3/kjavaappletviewer.so
%attr(755,root,root) %{_libdir}/kde3/klauncher.so
%attr(755,root,root) %{_libdir}/kde3/knotify.so
%attr(755,root,root) %{_libdir}/kde3/kspell_aspell.so
%attr(755,root,root) %{_libdir}/kde3/kspell_ispell.so
%attr(755,root,root) %{_libdir}/kde3/kspell_hspell.so
%attr(755,root,root) %{_libdir}/kde3/kstyle_highcontrast_config.so
%attr(755,root,root) %{_libdir}/kde3/kstyle_plastik_config.so
%attr(755,root,root) %{_libdir}/kde3/ktexteditor_docwordcompletion.so
%attr(755,root,root) %{_libdir}/kde3/ktexteditor_insertfile.so
%attr(755,root,root) %{_libdir}/kde3/ktexteditor_isearch.so
%attr(755,root,root) %{_libdir}/kde3/ktexteditor_kdatatool.so
%attr(755,root,root) %{_libdir}/kde3/libkatepart.so
%attr(755,root,root) %{_libdir}/kde3/libkcertpart.so
%attr(755,root,root) %{_libdir}/kde3/libkdeprint_management_module.so
%attr(755,root,root) %{_libdir}/kde3/libkhtmlpart.so
%attr(755,root,root) %{_libdir}/kde3/libkmultipart.so
%attr(755,root,root) %{_libdir}/kde3/libshellscript.so
%attr(755,root,root) %{_libdir}/libDCOP.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libDCOP.so.4
%if %{with arts}
%attr(755,root,root) %{_libdir}/libartskde.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libartskde.so.1
%endif
%attr(755,root,root) %{_libdir}/libkabc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkabc.so.1
%attr(755,root,root) %{_libdir}/libkabc_dir.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkabc_dir.so.1
%attr(755,root,root) %{_libdir}/libkabc_file.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkabc_file.so.1
%attr(755,root,root) %{_libdir}/libkabc_ldapkio.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkabc_ldapkio.so.1
%attr(755,root,root) %{_libdir}/libkatepartinterfaces.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkatepartinterfaces.so.0
%attr(755,root,root) %{_libdir}/libkdecore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdecore.so.4
%attr(755,root,root) %{_libdir}/libkdefakes.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdefakes.so.4
%attr(755,root,root) %{_libdir}/libkdefx.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdefx.so.4
%attr(755,root,root) %{_libdir}/libkdeinit_cupsdconf.so
%attr(755,root,root) %{_libdir}/libkdeinit_dcopserver.so
%attr(755,root,root) %{_libdir}/libkdeinit_kaddprinterwizard.so
%attr(755,root,root) %{_libdir}/libkdeinit_kbuildsycoca.so
%attr(755,root,root) %{_libdir}/libkdeinit_kcmshell.so
%attr(755,root,root) %{_libdir}/libkdeinit_kconf_update.so
%attr(755,root,root) %{_libdir}/libkdeinit_kcookiejar.so
%attr(755,root,root) %{_libdir}/libkdeinit_kded.so
%attr(755,root,root) %{_libdir}/libkdeinit_kio_http_cache_cleaner.so
%attr(755,root,root) %{_libdir}/libkdeinit_kio_uiserver.so
%attr(755,root,root) %{_libdir}/libkdeinit_klauncher.so
%attr(755,root,root) %{_libdir}/libkdeprint.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdeprint.so.4
%attr(755,root,root) %{_libdir}/libkdeprint_management.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdeprint_management.so.4
%attr(755,root,root) %{_libdir}/libkdesasl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdesasl.so.1
%attr(755,root,root) %{_libdir}/libkdesu.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdesu.so.4
%attr(755,root,root) %{_libdir}/libkdeui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdeui.so.4
%attr(755,root,root) %{_libdir}/libkdnssd.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdnssd.so.1
%attr(755,root,root) %{_libdir}/libkhtml.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkhtml.so.4
%attr(755,root,root) %{_libdir}/libkimproxy.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkimproxy.so.0
%attr(755,root,root) %{_libdir}/libkio.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkio.so.4
%attr(755,root,root) %{_libdir}/libkjava.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkjava.so.1
%attr(755,root,root) %{_libdir}/libkjs.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkjs.so.1
%attr(755,root,root) %{_libdir}/libkmdi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmdi.so.1
%attr(755,root,root) %{_libdir}/libkmdi2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmdi2.so.1
%attr(755,root,root) %{_libdir}/libkmediaplayer.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmediaplayer.so.0
%attr(755,root,root) %{_libdir}/libkmid.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmid.so.0
%attr(755,root,root) %{_libdir}/libknewstuff.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libknewstuff.so.1
%attr(755,root,root) %{_libdir}/libkntlm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkntlm.so.0
%attr(755,root,root) %{_libdir}/libkparts.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkparts.so.2
%attr(755,root,root) %{_libdir}/libkresources.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkresources.so.1
%attr(755,root,root) %{_libdir}/libkscreensaver.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkscreensaver.so.4
%attr(755,root,root) %{_libdir}/libkscript.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkscript.so.0
%attr(755,root,root) %{_libdir}/libkspell.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkspell.so.4
%attr(755,root,root) %{_libdir}/libkspell2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkspell2.so.1
%attr(755,root,root) %{_libdir}/libktexteditor.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libktexteditor.so.0
%attr(755,root,root) %{_libdir}/libkunittest.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkunittest.so.1
%attr(755,root,root) %{_libdir}/libkutils.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkutils.so.1
%attr(755,root,root) %{_libdir}/libkwalletbackend.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkwalletbackend.so.1
%attr(755,root,root) %{_libdir}/libkwalletclient.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkwalletclient.so.1
%attr(755,root,root) %{_libdir}/libvcard.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvcard.so.0

# merged kabc files
%attr(755,root,root) %{_libdir}/kde3/kabc_dir.so
%attr(755,root,root) %{_libdir}/kde3/kabc_file.so
%attr(755,root,root) %{_libdir}/kde3/kabc_ldapkio.so
%attr(755,root,root) %{_libdir}/kde3/kabcformat_binary.so
%attr(755,root,root) %{_libdir}/kde3/kcm_kresources.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dcopidl
%attr(755,root,root) %{_bindir}/dcopidl2cpp
#%attr(755,root,root) %{_bindir}/kconfig_compiler
%{_includedir}/kde3
#%{_libdir}/kde3/plugins/designer/kdewidgets.la
%dir %{_libdir}/kde3dev
%attr(755,root,root) %{_libdir}/kde3dev/libDCOP.so
%if %{with arts}
%attr(755,root,root) %{_libdir}/kde3dev/libartskde.so
%endif
%attr(755,root,root) %{_libdir}/kde3dev/libkabc.so
%attr(755,root,root) %{_libdir}/kde3dev/libkabc_dir.so
%attr(755,root,root) %{_libdir}/kde3dev/libkabc_file.so
%attr(755,root,root) %{_libdir}/kde3dev/libkabc_ldapkio.so
%attr(755,root,root) %{_libdir}/kde3dev/libkatepartinterfaces.so
%attr(755,root,root) %{_libdir}/kde3dev/libkdecore.so
%attr(755,root,root) %{_libdir}/kde3dev/libkdefakes.so
%attr(755,root,root) %{_libdir}/kde3dev/libkdefx.so
%attr(755,root,root) %{_libdir}/kde3dev/libkdeprint.so
%attr(755,root,root) %{_libdir}/kde3dev/libkdeprint_management.so
%attr(755,root,root) %{_libdir}/kde3dev/libkdesasl.so
%attr(755,root,root) %{_libdir}/kde3dev/libkdesu.so
%attr(755,root,root) %{_libdir}/kde3dev/libkdeui.so
%attr(755,root,root) %{_libdir}/kde3dev/libkdnssd.so
%attr(755,root,root) %{_libdir}/kde3dev/libkhtml.so
%attr(755,root,root) %{_libdir}/kde3dev/libkimproxy.so
%attr(755,root,root) %{_libdir}/kde3dev/libkio.so
%attr(755,root,root) %{_libdir}/kde3dev/libkjava.so
%attr(755,root,root) %{_libdir}/kde3dev/libkjs.so
%attr(755,root,root) %{_libdir}/kde3dev/libkmdi.so
%attr(755,root,root) %{_libdir}/kde3dev/libkmdi2.so
%attr(755,root,root) %{_libdir}/kde3dev/libkmediaplayer.so
%attr(755,root,root) %{_libdir}/kde3dev/libkmid.so
%attr(755,root,root) %{_libdir}/kde3dev/libknewstuff.so
%attr(755,root,root) %{_libdir}/kde3dev/libkntlm.so
%attr(755,root,root) %{_libdir}/kde3dev/libkparts.so
%attr(755,root,root) %{_libdir}/kde3dev/libkresources.so
%attr(755,root,root) %{_libdir}/kde3dev/libkscreensaver.so
%attr(755,root,root) %{_libdir}/kde3dev/libkscript.so
%attr(755,root,root) %{_libdir}/kde3dev/libkspell.so
%attr(755,root,root) %{_libdir}/kde3dev/libkspell2.so
%attr(755,root,root) %{_libdir}/kde3dev/libktexteditor.so
%attr(755,root,root) %{_libdir}/kde3dev/libkunittest.so
%attr(755,root,root) %{_libdir}/kde3dev/libkutils.so
%attr(755,root,root) %{_libdir}/kde3dev/libkwalletbackend.so
%attr(755,root,root) %{_libdir}/kde3dev/libkwalletclient.so
%attr(755,root,root) %{_libdir}/kde3dev/libvcard.so
%{_libdir}/kde3dev/libkdefakes_nonpic.a
