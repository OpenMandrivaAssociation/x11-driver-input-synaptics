Name:		x11-driver-input-synaptics
Version:	1.7.1
Release:	1
Summary:	X.org input driver for Synaptics touchpad devices
Group:		System/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-synaptics-%{version}.tar.bz2

Source3:	50-synaptics.conf
Source4:	70-touchpad-quirks.rules

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
Development files for programing with the xorg synaptics driver

%prep
%setup -qn xf86-input-synaptics-%{version}
%apply_patches
autoreconf -fi

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

%changelog
* Sat Nov 17 2012 akdengi <akdengi> 1.6.2+git20120912
- Install udev rules to /lib
- Use signal-safe logging
- Fix memory corruption on resume. Triggered if fingers are still on the
  touchpad when the device is disabled.

* Wed Jun 13 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.6.2-1
+ Revision: 805375
- version update 1.6.2

* Mon May 21 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1.6.1-1
+ Revision: 799764
- Use pkgconfig(*) requirements in BuildRequires

  + Alexander Khrukin <akhrukin@mandriva.org>
    - version update 1.6.1

* Tue Mar 27 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1.5.2-2
+ Revision: 787167
- Build for x11-server 1.12

* Mon Mar 26 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.5.2-1
+ Revision: 787016
- version update 1.5.2

* Fri Dec 30 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.5.0-3
+ Revision: 748323
- fixed files list
- rebuild, cleaned up spec

* Sat Oct 08 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.5.0-2
+ Revision: 703624
- rebuild for new x11-server

* Sat Sep 10 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.5.0-1
+ Revision: 699288
- update to new version 1.5.0

* Tue Jun 28 2011 Eugeni Dodonov <eugeni@mandriva.com> 1.4.1-1
+ Revision: 687823
- Updated to 1.4.1

* Fri Mar 04 2011 tv <tv> 1.4.0-2.mga1
+ Revision: 64381
- rebuild for new xserver-1.10

* Fri Mar 04 2011 tv <tv> 1.4.0-1.mga1
+ Revision: 63990
- new release

* Thu Jan 13 2011 colin <colin> 1.3.0-5.mga1
+ Revision: 16490
- imported package x11-driver-input-synaptics


* Tue Dec 28 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.3.0-5mdv2011.0
+ Revision: 625655
- Use configure2_5x
- We don't need to autoreconf
- Add back the good and old patch 0001 (aka: tapping is back)
  It was removed without any explanation (at least in the commit log) and makes
  people angry by disabling tapping on their touchpads "that always worked".

* Wed Nov 24 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 1.3.0-4mdv2011.0
+ Revision: 600881
- BR libxtst-devel for RECORD extension

* Wed Nov 10 2010 Thierry Vignaud <tv@mandriva.org> 1.3.0-3mdv2011.0
+ Revision: 595755
- require xorg server with proper ABI

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 1.3.0-2mdv2011.0
+ Revision: 584626
- bump release before rebuilding for xserver 1.9
- adjust file list for xserver1.9

* Wed Sep 01 2010 Thierry Vignaud <tv@mandriva.org> 1.3.0-1mdv2011.0
+ Revision: 575032
- adjust file list
- drop patch 1
- new release

* Thu May 06 2010 Colin Guthrie <cguthrie@mandriva.org> 1.2.2-2mdv2010.1
+ Revision: 542800
- Rebuild against latest xserver
  CCBUG: 55501

* Fri Mar 26 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.2.2-1mdv2010.1
+ Revision: 527635
- New version: 1.2.2

* Mon Dec 14 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.2.1-1mdv2010.1
+ Revision: 478507
- New version: 1.2.1

* Wed Nov 11 2009 Andrey Borzenkov <arvidjaar@mandriva.org> 1.2.0-3mdv2010.1
+ Revision: 464874
- rebuid with new xorg

  + Paulo Ricardo Zanoni <pzanoni@mandriva.com>
    - Fix BuildRequirement

* Tue Nov 10 2009 Andrey Borzenkov <arvidjaar@mandriva.org> 1.2.0-2mdv2010.1
+ Revision: 464260
- oops, rediff and add patches back
- remove patch1, patch2 - integrated upstream

  + Thierry Vignaud <tv@mandriva.org>
    - new release

* Mon Aug 03 2009 Colin Guthrie <cguthrie@mandriva.org> 1.1.3-1mdv2010.0
+ Revision: 407695
- New version: 1.1.3 (right scroll zone size issue mdv#51845, fdo#21001)

* Thu May 28 2009 Thierry Vignaud <tv@mandriva.org> 1.1.2-1mdv2010.0
+ Revision: 380328
- new release

* Thu May 21 2009 Colin Guthrie <cguthrie@mandriva.org> 1.1.1-1mdv2010.0
+ Revision: 378307
- New version: 1.1.1

* Thu Apr 23 2009 Colin Guthrie <cguthrie@mandriva.org> 1.1.0-4mdv2009.1
+ Revision: 368813
- Apply properties to all synaptics devices (fixes problem of settings not being applied when both hal and xorg.conf load a synaptics device)

* Sat Apr 18 2009 Colin Guthrie <cguthrie@mandriva.org> 1.1.0-3mdv2009.1
+ Revision: 367981
- Enable all button taps

* Tue Mar 31 2009 Frederic Crozat <fcrozat@mandriva.com> 1.1.0-2mdv2009.1
+ Revision: 362912
- Update fdi file to not assign synaptics driver on wacom handled tablets

* Mon Mar 09 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 1.1.0-1mdv2009.1
+ Revision: 353238
- New version 1.1.0

* Fri Mar 06 2009 Colin Guthrie <cguthrie@mandriva.org> 1.0.99.4-1mdv2009.1
+ Revision: 349613
- New version 1.0.99.4
- Drop revert of 64 weridness patch (fixed properly)
- Set defaults by patching driver (after upstream discussions)

* Wed Mar 04 2009 Colin Guthrie <cguthrie@mandriva.org> 1.0.99.3-3mdv2009.1
+ Revision: 348683
- Go back to 1.0.99.3 but with offending 64-bit breakage commit reverted

* Wed Mar 04 2009 Colin Guthrie <cguthrie@mandriva.org> 1.0.99.3-2mdv2009.1
+ Revision: 348413
- Temporarily restore 1.0.99.2 version due to segv's

* Wed Mar 04 2009 Colin Guthrie <cguthrie@mandriva.org> 1.0.99.3-1mdv2009.1
+ Revision: 348241
- New version: 1.0.99.3
- Set defaults: TwoFingerScroll: off, VertScroll: on, TapButton1: on

* Sat Feb 28 2009 Colin Guthrie <cguthrie@mandriva.org> 1.0.99.2-1mdv2009.1
+ Revision: 345950
- BuildRequire libxi-devel
- New version: 1.0.99.2

* Mon Feb 02 2009 Colin Guthrie <cguthrie@mandriva.org> 1.0.0-1mdv2009.1
+ Revision: 336376
- New version: 1.0.0

* Sun Jan 11 2009 Colin Guthrie <cguthrie@mandriva.org> 0.99.3-3mdv2009.1
+ Revision: 328326
- Add an fdi file so that the devices are automatically used (liberated from Fedora)

* Tue Dec 30 2008 Colin Guthrie <cguthrie@mandriva.org> 0.99.3-2mdv2009.1
+ Revision: 321381
- Rebuild for new xserver

* Mon Dec 15 2008 Colin Guthrie <cguthrie@mandriva.org> 0.99.3-1mdv2009.1
+ Revision: 314416
- New version 0.99.3
- Provide 'synaptics' to upgrade users on the old package
- Obsolete 'synaptics' to remove the old package from the distro.

* Thu Dec 04 2008 Thierry Vignaud <tv@mandriva.org> 0.99.2-1mdv2009.1
+ Revision: 309901
- new release

* Sun Nov 30 2008 Adam Williamson <awilliamson@mandriva.org> 0.99.1-2mdv2009.1
+ Revision: 308319
- rebuild for new X server

* Sat Nov 29 2008 Colin Guthrie <cguthrie@mandriva.org> 0.99.1-1mdv2009.1
+ Revision: 308001
- New version 0.99.1
- Add devel sub-package

* Wed Sep 10 2008 Colin Guthrie <cguthrie@mandriva.org> 0.15.2-1mdv2009.0
+ Revision: 283638
- New version: 0.15.2
- Remove device-path patch (fixed upstream)

* Wed Sep 10 2008 Colin Guthrie <cguthrie@mandriva.org> 0.15.1-2mdv2009.0
+ Revision: 283360
- Fix description
- Fix crash during initialisation

* Tue Sep 09 2008 Colin Guthrie <cguthrie@mandriva.org> 0.15.1-1mdv2009.0
+ Revision: 283145
- New version: 0.15.1

* Wed Aug 13 2008 Colin Guthrie <cguthrie@mandriva.org> 0.15.0-1mdv2009.0
+ Revision: 271343
- import x11-driver-input-synaptics

