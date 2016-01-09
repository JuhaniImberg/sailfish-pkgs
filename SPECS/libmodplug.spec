# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       libmodplug

# >> macros
# << macros

Summary:    A MOD rendering library
Version:    0.8.8.5
Release:    1
Group:      Development/Libraries
License:    Public Domain
URL:        http://modplug-xmms.sourceforge.net/
Source0:    https://downloads.sourceforge.net/project/modplug-xmms/%{name}/%{version}/%{name}-%{version}.tar.gz
Source100:  libmodplug.yaml
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
%{summary}.

%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Development files for %{name}.

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static
make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libmodplug.so*
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/libmodplug.pc
%{_includedir}/%{name}/
# >> files devel
# << files devel
