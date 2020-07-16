%global srcname socranop
%global underscored_srcname socranop

%global dbus_service_name io.github.socratools.socranop
%global gtk_app_id io.github.socratools.socranop

%global compdir %(pkg-config --variable=completionsdir bash-completion)

Name:           socranop
Version:        0.4.92
Release:        1%{?dist}
Summary:        Linux Utilities for Soundcraft Mixers

License:        MIT
URL:            https://github.com/socratools/socranop
# wget https://github.com/socratools/%%{name}/archive/v%%{version}.tar.gz
# Source0:      %%{name}-%%{version}.tar.gz
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  desktop-file-utils
# For %%{_udevrulesdir}
BuildRequires:  systemd-rpm-macros

BuildRequires:  python3-gobject-base
BuildRequires:  python3-pydbus
BuildRequires:  %{py3_dist pydbus}
BuildRequires:  %{py3_dist pyusb}
BuildRequires:  libgudev

BuildRequires:  bash-completion

Provides:       python3-socranop = %{version}-%{release}
%{?python_provide:%python_provide python3-socranop}

%description
Configure advanced features of Soundcraft Notepad mixers like the USB
routing for the capture channels.

%prep
%autosetup


%build
%py3_build


%install
rm -rf %{buildroot}
%py3_install

# Run installtool script, then remove it and its data files
env PYTHONPATH=%{buildroot}%{python3_sitelib} %{buildroot}%{_bindir}/socranop-installtool --chroot=%{buildroot} --post-install
rm -f  %{buildroot}%{_bindir}/socranop-installtool
rm -f  %{buildroot}%{_datadir}/bash-completion/completions/socranop-installtool
rm -f  %{buildroot}%{python3_sitelib}/socranop/installtool.py
rm -f  %{buildroot}%{python3_sitelib}/socranop/__pycache__/installtool.*.pyc
rm -rf %{buildroot}%{python3_sitelib}/socranop/data

# Move the service executable from %%{_bindir} to %%{_libexecdir}
%{__install} -m 0755    -d %{buildroot}%{_libexecdir}
mv %{buildroot}%{_bindir}/socranop-session-service %{buildroot}%{_libexecdir}/
%{__sed} -i 's|=%{_bindir}/|=%{_libexecdir}/|' %{buildroot}%{_datadir}/dbus-1/services/%{dbus_service_name}.service

# find %%{buildroot} -print0 | xargs -0 ls -dl | sed 's| %%{buildroot}/| /|'


%check
#{python3} setup.py test
desktop-file-validate %{buildroot}%{_datadir}/applications/%{gtk_app_id}.desktop


%files
%license LICENSE
%doc CONTRIBUTORS.md
%doc README.md
%doc PERMISSIONS.md
%{_bindir}/socranop-ctl
%{_bindir}/socranop-gui
%{_libexecdir}/socranop-session-service
%{_mandir}/man1/socranop-ctl.1*
%{_mandir}/man1/socranop-gui.1*
%{_mandir}/man1/socranop-session-service.1*
%{_mandir}/man7/socranop-permissions.7*
%{_datadir}/applications/%{gtk_app_id}.desktop
%{compdir}/socranop-ctl
%{compdir}/socranop-gui
%{compdir}/socranop-session-service
%{_datadir}/icons/hicolor/16x16/apps/%{gtk_app_id}.png
%{_datadir}/icons/hicolor/24x24/apps/%{gtk_app_id}.png
%{_datadir}/icons/hicolor/32x32/apps/%{gtk_app_id}.png
%{_datadir}/icons/hicolor/48x48/apps/%{gtk_app_id}.png
%{_datadir}/icons/hicolor/64x64/apps/%{gtk_app_id}.png
%{_datadir}/icons/hicolor/96x96/apps/%{gtk_app_id}.png
%{_datadir}/icons/hicolor/128x128/apps/%{gtk_app_id}.png
%{_datadir}/icons/hicolor/192x192/apps/%{gtk_app_id}.png
%{_datadir}/icons/hicolor/256x256/apps/%{gtk_app_id}.png
%{_datadir}/icons/hicolor/scalable/apps/%{gtk_app_id}.svg
%{_datadir}/dbus-1/services/%{dbus_service_name}.service
%{python3_sitelib}/%{underscored_srcname}-%{version}-*.egg-info/
%{python3_sitelib}/socranop/
%{_udevrulesdir}/70-socranop.rules


%changelog
* Sun Jul 25 2021 Hans Ulrich Niedermann <hun@n-dimensional.de> - 0.4.92-1
- Update to 0.4.92

* Thu Sep 10 2020 Hans Ulrich Niedermann <hun@n-dimensional.de> - 0.4.90-1
- Initial spec.
