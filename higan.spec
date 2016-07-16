
Name: higan
Version: 099
Release: 1%{?dist}

License: GPLv3
Summary: Emulator
URL:     http://byuu.org/emulation/higan
Source0: https://gitlab.com/higan/higan/repository/archive.tar.gz?ref=v%{version}

BuildRequires: gcc-c++
BuildRequires: gtk2-devel
BuildRequires: gtksourceview2-devel
BuildRequires: libao-devel
BuildRequires: libX11-devel
BuildRequires: libXv-devel
BuildRequires: openal-soft-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: SDL-devel
BuildRequires: systemd-devel


%description
Higan is an emulator.


%prep
%autosetup -n higan-v%{version}-c074c6e064928f65eea1a6e7ee1bf5e022e33440

sed -i \
        -e "/handle/s#/usr/local/lib#/usr/%{_libdir}#" \
        nall/dl.hpp || die "fixing libdir failed!"


%build
pushd icarus
make %{?_smp_mflags} compiler="$(which g++)" phoenix="gtk" platform="linux"
popd

pushd higan
make %{?_smp_mflags} compiler="$(which g++)" phoenix="gtk" platform="linux" profile="profile_accuracy"
popd


%install
install -d %{buildroot}/%{_datadir}/applications

pushd higan
%make_install prefix=%{buildroot}/%{_prefix}
popd
pushd icarus
%make_install prefix=%{buildroot}/%{_prefix}
popd


%files
%{_bindir}/higan
%{_bindir}/icarus
%{_datadir}/applications/higan.desktop
%{_datadir}/higan
%{_datadir}/icarus
%{_datadir}/icons/higan.png


%changelog
* Tue Jun 21 2016 Randy Barlow <bowlofeggs@fedoraproject.org> - 099-1
- Initial release.