Name:		brlaser
Version:	6.2.6
Release:	1
Source0:	https://github.com/Owl-Maintain/brlaser/archive/refs/tags/v%{version}.tar.gz
Summary:	Driver for Brother monochrome laster printers
URL:		https://github.com/Owl-Maintain/brlaser
License:	GPL-2.0
Group:		Drivers
BuildRequires:	cmake
BuildSystem:	cmake

%description
brlaser is an open-source CUPS driver designed specifically for Brother
monochrome laser printers and multi-function devices.

While most Brother printers can use standard printer languages like PCL
or PostScript, some models do not. If you have a monochrome Brother laser
printer (or multi-function device) and the other open-source drivers are not
working, brlaser might be able to help. Additionally, there have been reports
of some non-Brother printers working with this driver.

%prep
%autosetup -p1

%files
%{_prefix}/lib/cups/filter/rastertobrlaser
%{_datadir}/cups/drv/brlaser.drv
