Name: x11-driver-input-synaptics
Version: 1.6.1
Release: 1
Summary: X.org input driver for Synaptics touchpad devices
Group: System/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/driver/xf86-input-synaptics-%{version}.tar.bz2
Source1: 10-synaptics.fdi
Patch1: 0001-Always-enable-tapping-and-vertical-edge-scroll.patch


BuildRequires: x11-proto-devel
BuildRequires: x11-server-devel >= 1.12
BuildRequires: x11-util-macros >= 1.3.0
BuildRequires: libxi-devel
BuildRequires: libxtst-devel
BuildRequires: mtdev-devel

%rename synaptics
Requires: x11-server-common %(xserver-sdk-abi-requires xinput)

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
%setup -qn xf86-input-synaptics-%{version}
#% apply_patches

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

install -d %{buildroot}%{_datadir}/hal/fdi/policy/20thirdparty
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/hal/fdi/policy/20thirdparty

%files
%{_bindir}/synclient
%{_bindir}/syndaemon
%{_datadir}/hal/fdi/policy/20thirdparty/10-synaptics.fdi
%{_libdir}/xorg/modules/input/synaptics_drv.so
%{_mandir}/man1/synclient.*
%{_mandir}/man1/syndaemon.*
%{_mandir}/man4/synaptics.*
%{_datadir}/X11/xorg.conf.d/50-synaptics.conf

%files devel
%{_includedir}/xorg/synaptics.h
%{_includedir}/xorg/synaptics-properties.h
%{_libdir}/pkgconfig/xorg-synaptics.pc

