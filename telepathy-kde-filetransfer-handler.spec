%define rel 1

Summary:	Telepathy KDE File transfer handler
Name:		telepathy-kde-filetransfer-handler
Version:	0.2.0
Release:	%mkrel %{rel}
Url:		https://projects.kde.org/projects/playground/network/telepathy/telepathy-filetransfer-handler
Source0:	ftp://ftp.gtlib.cc.gatech.edu/pub/kde/unstable/telepathy-kde/%version/src/%name-%version.tar.bz2
License:	GPLv2+
Group:		Graphical desktop/KDE
BuildRequires:	kdelibs4-devel
BuildRequires:	telepathy-qt4-devel

%description
Telepathy-KDE file transfer handler

%files -f telepathy-filetransfer-handler.lang
%{_kde_libdir}/kde4/libexec/telepathy-kde-filetransfer-handler
%{_kde_datadir}/telepathy/clients/KDE.FileTransferHandler.client
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.KDE.FileTransferHandler.service
#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build
%find_lang telepathy-filetransfer-handler


