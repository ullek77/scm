Name:       jellyfin-media-player
Version:    1.11.1
Release:    1%{?dist}
Summary:    Jellyfin Desktop Client based on Plex Media Player
License:    GPLv3
URL:        https://github.com/jellyfin/jellyfin-media-player
Source0:    https://github.com/jellyfin/jellyfin-media-player/archive/refs/tags/v%{version}.tar.gz

BuildRequires: autoconf automake libtool cmake wget python g++ qt-devel
BuildRequires: meson ninja-build chrpath
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(fribidi)
BuildRequires: pkgconfig(gnutls)
BuildRequires: pkgconfig(libcec)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libva)
BuildRequires: pkgconfig(mpv)
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(vdpau)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(x11-xcb)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(zlib)
BuildRequires: mesa-libGL-devel mesa-libEGL-devel yasm alsa-lib
BuildRequires: mesa-libGLU-devel
BuildRequires: qt5-qtbase-devel curl unzip qt5-qtwebchannel-devel
BuildRequires: qt5-qtwebengine-devel qt5-qtx11extras-devel
BuildRequires: qwt-qt5-devel qt5-qtbase-private-devel
Requires: mpv-libs
Requires: mpv
Requires: qt5-qtbase

%description
Desktop client using jellyfin-web with embedded MPV player.
Supports Windows, Mac OS, and Linux. Media plays within the same
window using the jellyfin-web interface unlike Jellyfin Desktop.
Supports audio passthrough. Based on Plex Media Player.

%prep
%setup -n jellyfin-media-player-%{version}

%build
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr ..
make

%install
cd build
DESTDIR=%{buildroot} make install
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/jellyfinmediaplayer

%files
%{_bindir}/jellyfinmediaplayer
%{_datarootdir}/jellyfinmediaplayer
%{_datarootdir}/applications/com.github.iwalton3.jellyfin-media-player.desktop
%{_datarootdir}/icons/hicolor/scalable/apps/com.github.iwalton3.jellyfin-media-player.svg
%{_datarootdir}/metainfo/com.github.iwalton3.jellyfin-media-player.appdata.xml

%changelog
* Wed Aug 07 2024 Marc Oliver Koenig <mkoenig@new-cookie-universe.de>
- update to v1.11.1