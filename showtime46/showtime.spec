%global app_id org.gnome.Showtime
%global debug_package %{nil}

Name:           showtime
Version:        46.3
Release:        1%{?dist}
Summary:        A GTK video player

License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/GNOME/Incubator/showtime
Source0:        %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  blueprint-compiler
BuildRequires:  desktop-file-utils
BuildRequires:  python3-devel

%description
Play your favorite movies and video files without hassle. Showtime features
simple playback controls that fade out of your way when you're watching,
fullscreen, adjustable playback speed, multiple language and subtitle tracks,
and screenshots — everything you need for a straightforward viewing experience.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
chmod 755 %{buildroot}/%{_bindir}/%{name}
%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/glib-2.0/schemas/%{app_id}.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/%{app_id}.svg
%{_datadir}/icons/hicolor/symbolic/apps/%{app_id}-symbolic.svg
%{_metainfodir}/%{app_id}.metainfo.xml
%{_datadir}/%{name}/
%{python3_sitelib}/%{name}/

%changelog
* Initial build
