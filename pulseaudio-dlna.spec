%global commit 10bc454b958ae58d316114e1f3a0cbb8eac26161
%global gittag 0.5.2-py3-0.4
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%define owner Tinigriffy
%define name pulseaudio-dlna
%define version 0.5.2.py3.0.4
%define release %{shortcommit}

Summary: A small DLNA server which brings DLNA / UPNP supportto PulseAudio and Linux.
Name: %{name}
Version: %{version}
Release: %{release}
Source0: https://github.com/%{owner}/%{name}/archive/%{gittag}/%{name}-%{version}.tar.gz
License: GPLv3
Group: "Multimedia/PulseAudio"
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Massimo Mund <mo@lancode.de>
Packager: Tinigriffy
Url: https://github.com/Tinigriffy/pulseaudio-dlna

BuildRequires:  python3-devel
BuildRequires: 	python3-setuptools
BuildRequires:	python3-pip
Requires:	python3-pip
Requires:	python3-gobject
Requires: python3-dbus
Requires: python3-docopt
Requires:	python3-requests
Requires:	python3-setproctitle
Requires:	python3-protobuf
Requires:	python3-notify2
Requires: python3-psutil
Requires: python3-chardet
Requires: python3-zeroconf
Requires: python3-netifaces
Requires: python3-pyroute2
Requires:	python3-lxml
Requires:	python3-future
Requires:	sox
Requires:	lame
Requires:	flac
Requires:	faac
Requires:	opus-tools

%description
A port to python3 of a small DLNA server which brings DLNA / UPNP support to PulseAudio and Linux.

It can stream your current PulseAudio playback to different UPNP devices (UPNP Media Renderers) in your network. It's main goals are: easy to use, no configuration hassle, no big dependencies.

https://github.com/Tinigriffy/pulseaudio-dlna

Original project:
https://github.com/masmu/pulseaudio-dlna

%prep
%autosetup -n %{name}-%{gittag}

%build
%py3_build

%install
%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%{python3_sitelib}/*
/usr/bin/pulseaudio-dlna
/usr/share/man/man1/pulseaudio-dlna.1.gz
%doc README.md
