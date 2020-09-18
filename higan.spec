Name: higan
Version: 115
Release: 1%{?dist}

License: GPLv3
Summary: Emulator
URL:     http://byuu.org/emulation/higan
Source:  https://github.com/byuu/higan/archive/v%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: gtk2-devel
BuildRequires: gtksourceview2-devel
BuildRequires: libao-devel
BuildRequires: libX11-devel
BuildRequires: libXv-devel
BuildRequires: openal-soft-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: SDL2-devel
BuildRequires: systemd-devel
BuildRequires: mesa-libGL-devel
BuildRequires: alsa-lib-devel


%description
Higan is an emulator.


%prep
%autosetup -p1

sed -i \
        -e "/handle/s#/usr/local/lib#/usr/%{_libdir}#" \
        nall/dl.hpp || die "fixing libdir failed!"

# fix so that it doesn't build march=native
sed -i \
        -e 's/march=native/march=x86-64/g' \
        -e 's/^\(flags.*\)/\1 -g/' \
        luna/GNUmakefile lucia/GNUmakefile


%build
pushd lucia
make %{?_smp_mflags} compiler="$(which g++)" phoenix="gtk" platform="linux"
popd

pushd luna
make %{?_smp_mflags} compiler="$(which g++)" phoenix="gtk" platform="linux" profile="profile_accuracy"
popd


%install
install -d %{buildroot}/%{_datadir}/applications

pushd luna
%make_install prefix=%{buildroot}/%{_prefix}
popd
pushd lucia
%make_install prefix=%{buildroot}/%{_prefix}
popd


%files
%{_bindir}/luna
%{_bindir}/lucia
%{_datadir}/applications/luna.desktop
%{_datadir}/applications/lucia.desktop
%{_datadir}/luna
%{_datadir}/lucia
%{_datadir}/icons/luna.png
%{_datadir}/icons/lucia.png


%changelog
* Fri Sep 18 2020 Dick Marinus <dick@mrns.nl> - 115-1
- Update to 115

* Sun May 24 2020 Dick Marinus <dick@mrns.nl> - 110-1
- Update to 110

* Fri Feb 28 2020 Dick Marinus <dick@mrns.nl> - 107-1
- Update to 107

* Sat Oct 27 2018 Dick Marinus <dick@mrns.nl> - 106-3
- Update source (removed rom files)

* Sun Mar 04 2018 Dick Marinus <dick@mrns.nl> - 106-2
- Change URL, add use_sharedpath patch from Tobias Hansen

* Thu Jan 04 2018 Dick Marinus <dick@mrns.nl> - 106-1
- Update to 106

* Fri Dec 29 2017 Dick Marinus <dick@mrns.nl> - 102-2
- Add debug symbols for find-debuginfo.sh

* Mon Feb 20 2017 Mirko Rolfes <songokussj@gmx.net> - 102
- Update to 102

* Mon Aug 22 2016 Mirko Rolfes <songokussj@gmx.net> - 101-1
- Update to 101

* Tue Aug 02 2016 Mirko Rolfes <songokussj@gmx.net> - 100-1
- Update to 100

* Tue Jun 21 2016 Randy Barlow <bowlofeggs@fedoraproject.org> - 099-1
- Initial release.
