Name:		x11-driver-input-synaptics
Version:	1.7.2
Release:	2
Summary:	X.org input driver for Synaptics touchpad devices
Group:		System/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-synaptics-%{version}.tar.bz2
Source3:	50-synaptics.conf
Source4:	70-touchpad-quirks.rules
Patch1: 0001-Always-enable-tapping-and-vertical-edge-scroll.patch
Patch2: 0002-When-appling-changes-via-property-mode-apply-to-all.patch
BuildRequires:	x11-proto-devel
BuildRequires:	x11-server-devel >= 1.12
BuildRequires:	x11-util-macros >= 1.3.0
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xtst)
BuildRequires:	pkgconfig(mtdev)
Requires:	x11-server-common %(xserver-sdk-abi-requires xinput)
%rename		synaptics

%description
Synaptics touchpad devices are extremely popular on laptops and this driver
is an MIT licensed alternative to the older GPL synaptics driver which is
no longer actively maintained.

%package devel
Summary:		Development files for programing with the xorg synaptics driver
Group:			Development/C

%description devel
Development files for programing with the xorg synaptics driver.

%prep
%setup -qn xf86-input-synaptics-%{version}
%apply_patches

%build
%configure2_5x
%make

%install
%makeinstall_std

install -m644 %{SOURCE3} -D %{buildroot}%{_datadir}/X11/xorg.conf.d/50-synaptics.conf
install -m644 %{SOURCE4} -D %{buildroot}/lib/udev/rules.d/70-touchpad-quirks.rules

%files
%{_bindir}/synclient
%{_bindir}/syndaemon
%{_libdir}/xorg/modules/input/synaptics_drv.so
%{_mandir}/man1/synclient.*
%{_mandir}/man1/syndaemon.*
%{_mandir}/man4/synaptics.*
%{_datadir}/X11/xorg.conf.d/50-synaptics.conf
/lib/udev/rules.d/70-touchpad-quirks.rules

%files devel
#removed since 1.7.0
#% {_includedir}/xorg/synaptics.h
%{_includedir}/xorg/synaptics-properties.h
%{_libdir}/pkgconfig/xorg-synaptics.pc
