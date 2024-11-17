Name:           pika-backup
Version:        0.7.4
Release:        1%{?dist}
Summary:        Simple backups based on borg
License:        GPLv3+
URL:            https://gitlab.gnome.org/World/pika-backup
Source:         %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildRequires:  meson
BuildRequires:  git
BuildRequires:  pkgconfig
BuildRequires:  rust-packaging
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  itstool
Requires:       borgbackup
Requires:       python3dist(msgpack)

%description
Doing backups the easy way. Plugin your USB drive and let the Pika do the rest for you.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%files -f %{name}.lang
%license LICENSE
%doc README.md
%doc %{_datadir}/help/*
%{_bindir}/pika-backup
%{_bindir}/pika-backup-monitor
%config %{_sysconfdir}/xdg/autostart/org.gnome.World.PikaBackup.Monitor.desktop
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.svg
%{_datadir}/metainfo/*.metainfo.xml
%{_datadir}/dbus-1/services/*.service

%changelog
- Initial build
