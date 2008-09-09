Name: x11-driver-input-synaptics
Version: 0.15.1
Release: %mkrel 1
Summary: X.org input driver for Synaptics touchpad devices
Group: System/X11
URL: http://xorg.freedesktop.org
Source: xf86-input-synaptics-%{version}.tar.bz2

License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-proto-devel
BuildRequires: x11-server-devel
BuildRequires: x11-util-macros
Conflicts: synaptics

%description
Synaptics devices are extremely popular on laptops and this driverer
repsents an MIT licnenced alternative to the GPL synaptics driver

%prep
%setup -q -n xf86-input-synaptics-%{version}

%build
autoreconf
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/synclient
%{_bindir}/syndaemon
%{_libdir}/xorg/modules/input/synaptics_drv.la
%{_libdir}/xorg/modules/input/synaptics_drv.so
%{_mandir}/man1/synclient.*
%{_mandir}/man1/syndaemon.*
%{_mandir}/man4/synaptics.*
