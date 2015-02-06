%define srcname ktp-filetransfer-handler 

Summary:	Telepathy KDE File transfer handler
Name:		telepathy-kde-filetransfer-handler
Version:	0.5.1
Release:	2
Url:		https://projects.kde.org/projects/playground/network/telepathy/telepathy-filetransfer-handler
Source0:	ftp://ftp.gtlib.cc.gatech.edu/pub/kde/unstable/telepathy-kde/%version/src/%srcname-%version.tar.bz2
License:	GPLv2+
Group:		Networking/Instant messaging
BuildRequires:	telepathy-kde-common-internals-devel >= %{version}
Requires:	telepathy-kde-common-internals-core

%description
Telepathy-KDE file transfer handler

%files -f ktp-filetransfer-handler.lang
%{_kde_libdir}/kde4/libexec/ktp-filetransfer-handler
%{_datadir}/telepathy/clients/KTp.FileTransferHandler.client
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.KTp.FileTransferHandler.service

#------------------------------------------------------------------------------

%prep
%setup -q -n %srcname-%version

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build
%find_lang ktp-filetransfer-handler
