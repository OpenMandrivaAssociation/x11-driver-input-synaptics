Name: x11-driver-input-synaptics
Version: 1.3.0
Release: %mkrel 2
Summary: X.org input driver for Synaptics touchpad devices
Group: System/X11
URL: http://xorg.freedesktop.org
Source0: xf86-input-synaptics-%{version}.tar.bz2
Source1: 10-synaptics.fdi
Patch2: 0002-When-appling-changes-via-property-mode-apply-to-all.patch

License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-proto-devel
BuildRequires: x11-server-devel
BuildRequires: x11-util-macros >= 1.3.0
BuildRequires: libxi-devel
Provides: synaptics = %{version}-%{release}
Obsoletes: synaptics < %{version}-%{release}

%description
Synaptics touchpad devices are extremely popular on laptops and this driver
is an MIT licensed alternative to the older GPL synaptics driver which is
no longer actively maintained.

%package devel
Summary:        Development files for programing with the xorg synaptics driver
Group:          Development/C

%description devel
Development files for programing with the xorg synaptics driver


%prep
%setup -q -n xf86-input-synaptics-%{version}
%patch2 -p1

%build
autoreconf
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

install -d %{buildroot}%{_datadir}/hal/fdi/policy/20thirdparty
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/hal/fdi/policy/20thirdparty

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/synclient
%{_bindir}/syndaemon
%{_datadir}/hal/fdi/policy/20thirdparty/10-synaptics.fdi
%{_libdir}/xorg/modules/input/synaptics_drv.la
%{_libdir}/xorg/modules/input/synaptics_drv.so
%{_mandir}/man1/synclient.*
%{_mandir}/man1/syndaemon.*
%{_mandir}/man4/synaptics.*
%{_datadir}/X11/xorg.conf.d/50-synaptics.conf

%files devel
%defattr(-,root,root)
%{_includedir}/xorg/synaptics.h
%{_includedir}/xorg/synaptics-properties.h
%{_libdir}/pkgconfig/xorg-synaptics.pc
