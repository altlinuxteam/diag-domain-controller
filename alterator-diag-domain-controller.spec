%define _unpackaged_files_terminate_build 1
Name: diag-domain-controller
Version: 0.0.2
Release: alt1

Summary: Domain Controller Diagnostic Tool.
License: GPLv3
Group: Other
URL: https://github.com/Medovi/SambaDC-diag/tree/main
BuildArch: noarch
Source0: %name-%version.tar

%description
Domain Controller Diagnostic Tool.

%prep
%setup

%build
sed -i 's/^VERSION=.*/VERSION=%version/' %name

%install
mkdir -p %buildroot%_alterator_datadir/diagnostictools/%name

install -p -D -m755 %name %buildroot%_bindir/%name
install -p -D -m644 %name.backend %buildroot%_alterator_datadir/backends/%name.backend
install -p -D -m644 %name.diagnostictool %buildroot%_alterator_datadir/diagnostictools/%name/%name.diagnostictool
install -p -D %name.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg

%files
%_bindir/%name
%_alterator_datadir/backends/%name.backend
%_alterator_datadir/diagnostictools/%name/%name.diagnostictool
%_iconsdir/hicolor/scalable/apps/%name.svg

%changelog
* Thu Aug 08 2024 Sergey Savelev <savelevsa@basealt.ru> 0.0.2-alt1
- changes in the description of the tests

* Thu Aug 08 2024 Sergey Savelev <savelevsa@basealt.ru> 0.0.1-alt1
- initial build

