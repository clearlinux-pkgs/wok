#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : wok
Version  : 2.5.0
Release  : 5
URL      : https://github.com/kimchi-project/wok/archive/2.5.0.tar.gz
Source0  : https://github.com/kimchi-project/wok/archive/2.5.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 LGPL-2.1 MIT
Requires: wok-bin = %{version}-%{release}
Requires: wok-data = %{version}-%{release}
Requires: wok-license = %{version}-%{release}
Requires: wok-locales = %{version}-%{release}
Requires: wok-man = %{version}-%{release}
Requires: wok-python = %{version}-%{release}
Requires: wok-python3 = %{version}-%{release}
Requires: wok-services = %{version}-%{release}
BuildRequires : libxml2-dev
BuildRequires : libxslt
BuildRequires : libxslt-dev
BuildRequires : pkgconfig(systemd)
BuildRequires : systemd-dev

%description
* [What is Wok?](#what-is-wok)
* [Browser Support](#browser-support)
* [Desktop Browser Support](#desktop-browser-support)
* [Mobile Browser Support](#mobile-browser-support)
* [Linux Support](#linux-support)
* [Getting started](#getting-started)
* [Install Dependencies](#install-dependencies)
* [Build and Install](#build-and-install)
* [Starting up Wok](#starting-up-wok)
* [Troubleshooting](/docs/troubleshooting.md)
* [Contributing to Wok Project](#contributing-to-wok-project)

%package bin
Summary: bin components for the wok package.
Group: Binaries
Requires: wok-data = %{version}-%{release}
Requires: wok-license = %{version}-%{release}
Requires: wok-man = %{version}-%{release}
Requires: wok-services = %{version}-%{release}

%description bin
bin components for the wok package.


%package data
Summary: data components for the wok package.
Group: Data

%description data
data components for the wok package.


%package license
Summary: license components for the wok package.
Group: Default

%description license
license components for the wok package.


%package locales
Summary: locales components for the wok package.
Group: Default

%description locales
locales components for the wok package.


%package man
Summary: man components for the wok package.
Group: Default

%description man
man components for the wok package.


%package python
Summary: python components for the wok package.
Group: Default
Requires: wok-python3 = %{version}-%{release}

%description python
python components for the wok package.


%package python3
Summary: python3 components for the wok package.
Group: Default
Requires: python3-core

%description python3
python3 components for the wok package.


%package services
Summary: services components for the wok package.
Group: Systemd services

%description services
services components for the wok package.


%prep
%setup -q -n wok-2.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1540763620
%autogen --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1540763620
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/wok
cp COPYING.ASL2 %{buildroot}/usr/share/package-licenses/wok/COPYING.ASL2
cp COPYING.LGPL %{buildroot}/usr/share/package-licenses/wok/COPYING.LGPL
cp ui/css/src/vendor/bootstrap-sass/LICENSE %{buildroot}/usr/share/package-licenses/wok/ui_css_src_vendor_bootstrap-sass_LICENSE
cp ui/css/src/vendor/compass-mixins/LICENSE %{buildroot}/usr/share/package-licenses/wok/ui_css_src_vendor_compass-mixins_LICENSE
cp ui/libs/bootstrap-editable/LICENSE %{buildroot}/usr/share/package-licenses/wok/ui_libs_bootstrap-editable_LICENSE
cp ui/libs/bootstrap-select/LICENSE %{buildroot}/usr/share/package-licenses/wok/ui_libs_bootstrap-select_LICENSE
cp ui/libs/bootstrap-switch/LICENSE %{buildroot}/usr/share/package-licenses/wok/ui_libs_bootstrap-switch_LICENSE
cp ui/libs/bootstrap/LICENSE %{buildroot}/usr/share/package-licenses/wok/ui_libs_bootstrap_LICENSE
cp ui/libs/datatables/LICENSE %{buildroot}/usr/share/package-licenses/wok/ui_libs_datatables_LICENSE
cp ui/libs/datatables/js/plugins/ip-address/LICENSE %{buildroot}/usr/share/package-licenses/wok/ui_libs_datatables_js_plugins_ip-address_LICENSE
cp ui/libs/es5-shim/LICENSE %{buildroot}/usr/share/package-licenses/wok/ui_libs_es5-shim_LICENSE
cp ui/libs/jquery-bootgrid/LICENSE %{buildroot}/usr/share/package-licenses/wok/ui_libs_jquery-bootgrid_LICENSE
cp ui/libs/jquery-containsNC/LICENSE %{buildroot}/usr/share/package-licenses/wok/ui_libs_jquery-containsNC_LICENSE
cp ui/libs/jquery-i18n/LICENSE %{buildroot}/usr/share/package-licenses/wok/ui_libs_jquery-i18n_LICENSE
cp ui/libs/jquery-ui/LICENSE %{buildroot}/usr/share/package-licenses/wok/ui_libs_jquery-ui_LICENSE
cp ui/libs/jquery/LICENSE %{buildroot}/usr/share/package-licenses/wok/ui_libs_jquery_LICENSE
cp ui/libs/list-js/LICENSE %{buildroot}/usr/share/package-licenses/wok/ui_libs_list-js_LICENSE
cp ui/libs/lodash/LICENSE %{buildroot}/usr/share/package-licenses/wok/ui_libs_lodash_LICENSE
cp ui/libs/moment/LICENSE %{buildroot}/usr/share/package-licenses/wok/ui_libs_moment_LICENSE
cp ui/libs/typeahead/LICENSE %{buildroot}/usr/share/package-licenses/wok/ui_libs_typeahead_LICENSE
%make_install
%find_lang wok
## install_append content
rm -rf %{buildroot}/var
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib/firewalld/services/wokd.xml

%files bin
%defattr(-,root,root,-)
/usr/bin/wokd

%files data
%defattr(-,root,root,-)
/usr/share/wok/doc/API/README.md
/usr/share/wok/doc/API/config.md
/usr/share/wok/doc/API/logs.md
/usr/share/wok/doc/API/notifications.md
/usr/share/wok/doc/API/peers.md
/usr/share/wok/doc/API/tasks.md
/usr/share/wok/doc/README-federation.md
/usr/share/wok/doc/README.md
/usr/share/wok/doc/fedora-deps.md
/usr/share/wok/doc/opensuse-deps.md
/usr/share/wok/doc/troubleshooting.md
/usr/share/wok/doc/ubuntu-deps.md
/usr/share/wok/doc/wokd.8
/usr/share/wok/ui/base64/jquery.base64.js
/usr/share/wok/ui/config/tab-ext.xml
/usr/share/wok/ui/css/bootstrap-select.custom.css
/usr/share/wok/ui/css/bootstrap.custom.css
/usr/share/wok/ui/css/datatables.bootstrap.css
/usr/share/wok/ui/css/fontawesome/fontawesome.css
/usr/share/wok/ui/css/jquery-ui.custom.css
/usr/share/wok/ui/css/settings.css
/usr/share/wok/ui/css/user-log.css
/usr/share/wok/ui/css/wok.css
/usr/share/wok/ui/images/android-chrome-144x144.png
/usr/share/wok/ui/images/android-chrome-192x192.png
/usr/share/wok/ui/images/android-chrome-36x36.png
/usr/share/wok/ui/images/android-chrome-48x48.png
/usr/share/wok/ui/images/android-chrome-72x72.png
/usr/share/wok/ui/images/android-chrome-96x96.png
/usr/share/wok/ui/images/apple-touch-icon-114x114.png
/usr/share/wok/ui/images/apple-touch-icon-120x120.png
/usr/share/wok/ui/images/apple-touch-icon-144x144.png
/usr/share/wok/ui/images/apple-touch-icon-152x152.png
/usr/share/wok/ui/images/apple-touch-icon-180x180.png
/usr/share/wok/ui/images/apple-touch-icon-57x57.png
/usr/share/wok/ui/images/apple-touch-icon-60x60.png
/usr/share/wok/ui/images/apple-touch-icon-72x72.png
/usr/share/wok/ui/images/apple-touch-icon-76x76.png
/usr/share/wok/ui/images/apple-touch-icon-precomposed.png
/usr/share/wok/ui/images/apple-touch-icon.png
/usr/share/wok/ui/images/favicon-16x16.png
/usr/share/wok/ui/images/favicon-194x194.png
/usr/share/wok/ui/images/favicon-32x32.png
/usr/share/wok/ui/images/favicon-96x96.png
/usr/share/wok/ui/images/favicon.ico
/usr/share/wok/ui/images/favicon.png
/usr/share/wok/ui/images/mstile-144x144.png
/usr/share/wok/ui/images/mstile-150x150.png
/usr/share/wok/ui/images/mstile-310x150.png
/usr/share/wok/ui/images/mstile-310x310.png
/usr/share/wok/ui/images/mstile-70x70.png
/usr/share/wok/ui/images/pl.png
/usr/share/wok/ui/images/safari-pinned-tab.svg
/usr/share/wok/ui/images/theme-default/edit-alt.svg
/usr/share/wok/ui/images/theme-default/high.png
/usr/share/wok/ui/images/theme-default/high_disabled.png
/usr/share/wok/ui/images/theme-default/icon-centos.png
/usr/share/wok/ui/images/theme-default/icon-debian.png
/usr/share/wok/ui/images/theme-default/icon-fedora.png
/usr/share/wok/ui/images/theme-default/icon-gentoo.png
/usr/share/wok/ui/images/theme-default/icon-opensuse.png
/usr/share/wok/ui/images/theme-default/icon-red_hat.png
/usr/share/wok/ui/images/theme-default/icon-ubuntu.png
/usr/share/wok/ui/images/theme-default/icon-unknown.png
/usr/share/wok/ui/images/theme-default/logo-flat.svg
/usr/share/wok/ui/images/theme-default/logo-white.png
/usr/share/wok/ui/images/theme-default/low.png
/usr/share/wok/ui/images/theme-default/low_disabled.png
/usr/share/wok/ui/images/theme-default/med.png
/usr/share/wok/ui/images/theme-default/med_disabled.png
/usr/share/wok/ui/images/theme-default/spin5.svg
/usr/share/wok/ui/images/wok-logo.png
/usr/share/wok/ui/images/wok.png
/usr/share/wok/ui/images/wok.svg
/usr/share/wok/ui/js/wok.bootgrid.js
/usr/share/wok/ui/js/wok.min.js
/usr/share/wok/ui/js/wok.peers.js
/usr/share/wok/ui/js/wok.settings.js
/usr/share/wok/ui/js/wok.user-log.js
/usr/share/wok/ui/libs/bootstrap-editable/dist/css/bootstrap-editable.css
/usr/share/wok/ui/libs/bootstrap-editable/dist/js/bootstrap-editable.min.js
/usr/share/wok/ui/libs/bootstrap-select/dist/css/bootstrap-select.min.css
/usr/share/wok/ui/libs/bootstrap-select/dist/js/bootstrap-select.min.js
/usr/share/wok/ui/libs/bootstrap-switch/dist/css/bootstrap-switch.min.css
/usr/share/wok/ui/libs/bootstrap-switch/dist/js/bootstrap-switch.min.js
/usr/share/wok/ui/libs/bootstrap/bootstrap.min.js
/usr/share/wok/ui/libs/datatables/css/datatables.min.css
/usr/share/wok/ui/libs/datatables/js/datatables.min.js
/usr/share/wok/ui/libs/datatables/js/plugins/ip-address/ip-address.js
/usr/share/wok/ui/libs/es5-shim/es5-shim.min.js
/usr/share/wok/ui/libs/jquery-bootgrid/dist/css/jquery.bootgrid.min.css
/usr/share/wok/ui/libs/jquery-bootgrid/dist/js/jquery.bootgrid.min.js
/usr/share/wok/ui/libs/jquery-containsNC/jquery.containsNC.js
/usr/share/wok/ui/libs/jquery-i18n/jquery.i18n.min.js
/usr/share/wok/ui/libs/jquery-ui/jquery-ui-i18n.min.js
/usr/share/wok/ui/libs/jquery-ui/jquery-ui.min.js
/usr/share/wok/ui/libs/jquery-ui/themes/base/images/ui-bg_diagonals-thick_18_b81900_40x40.png
/usr/share/wok/ui/libs/jquery-ui/themes/base/images/ui-bg_diagonals-thick_20_666666_40x40.png
/usr/share/wok/ui/libs/jquery-ui/themes/base/images/ui-bg_flat_10_000000_40x100.png
/usr/share/wok/ui/libs/jquery-ui/themes/base/images/ui-bg_glass_100_f6f6f6_1x400.png
/usr/share/wok/ui/libs/jquery-ui/themes/base/images/ui-bg_glass_100_fdf5ce_1x400.png
/usr/share/wok/ui/libs/jquery-ui/themes/base/images/ui-bg_glass_65_ffffff_1x400.png
/usr/share/wok/ui/libs/jquery-ui/themes/base/images/ui-bg_gloss-wave_35_f6a828_500x100.png
/usr/share/wok/ui/libs/jquery-ui/themes/base/images/ui-bg_highlight-soft_100_eeeeee_1x100.png
/usr/share/wok/ui/libs/jquery-ui/themes/base/images/ui-bg_highlight-soft_75_ffe45c_1x100.png
/usr/share/wok/ui/libs/jquery-ui/themes/base/images/ui-icons_222222_256x240.png
/usr/share/wok/ui/libs/jquery-ui/themes/base/images/ui-icons_228ef1_256x240.png
/usr/share/wok/ui/libs/jquery-ui/themes/base/images/ui-icons_ef8c08_256x240.png
/usr/share/wok/ui/libs/jquery-ui/themes/base/images/ui-icons_ffd27a_256x240.png
/usr/share/wok/ui/libs/jquery-ui/themes/base/images/ui-icons_ffffff_256x240.png
/usr/share/wok/ui/libs/jquery-ui/themes/base/jquery-ui.min.css
/usr/share/wok/ui/libs/jquery/jquery.min.js
/usr/share/wok/ui/libs/list-js/list.min.js
/usr/share/wok/ui/libs/lodash/lodash.min.js
/usr/share/wok/ui/libs/moment/moment-with-locales.min.js
/usr/share/wok/ui/libs/typeahead/typeahead.bundle.min.js
/usr/share/wok/ui/pages/error.html.tmpl
/usr/share/wok/ui/pages/help/en_US/settings.html
/usr/share/wok/ui/pages/help/en_US/user-log.html
/usr/share/wok/ui/pages/help/wok.css
/usr/share/wok/ui/pages/i18n.json.tmpl
/usr/share/wok/ui/pages/login.html.tmpl
/usr/share/wok/ui/pages/tabs/settings.html.tmpl
/usr/share/wok/ui/pages/tabs/user-log-search.html.tmpl
/usr/share/wok/ui/pages/tabs/user-log.html.tmpl
/usr/share/wok/ui/pages/wok-ui.html.tmpl
/usr/share/wok/ui/robots.txt

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/wok/COPYING.ASL2
/usr/share/package-licenses/wok/COPYING.LGPL
/usr/share/package-licenses/wok/ui_css_src_vendor_bootstrap-sass_LICENSE
/usr/share/package-licenses/wok/ui_css_src_vendor_compass-mixins_LICENSE
/usr/share/package-licenses/wok/ui_libs_bootstrap-editable_LICENSE
/usr/share/package-licenses/wok/ui_libs_bootstrap-select_LICENSE
/usr/share/package-licenses/wok/ui_libs_bootstrap-switch_LICENSE
/usr/share/package-licenses/wok/ui_libs_bootstrap_LICENSE
/usr/share/package-licenses/wok/ui_libs_datatables_LICENSE
/usr/share/package-licenses/wok/ui_libs_datatables_js_plugins_ip-address_LICENSE
/usr/share/package-licenses/wok/ui_libs_es5-shim_LICENSE
/usr/share/package-licenses/wok/ui_libs_jquery-bootgrid_LICENSE
/usr/share/package-licenses/wok/ui_libs_jquery-containsNC_LICENSE
/usr/share/package-licenses/wok/ui_libs_jquery-i18n_LICENSE
/usr/share/package-licenses/wok/ui_libs_jquery-ui_LICENSE
/usr/share/package-licenses/wok/ui_libs_jquery_LICENSE
/usr/share/package-licenses/wok/ui_libs_list-js_LICENSE
/usr/share/package-licenses/wok/ui_libs_lodash_LICENSE
/usr/share/package-licenses/wok/ui_libs_moment_LICENSE
/usr/share/package-licenses/wok/ui_libs_typeahead_LICENSE

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/wokd.8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/wokd.service

%files locales -f wok.lang
%defattr(-,root,root,-)

