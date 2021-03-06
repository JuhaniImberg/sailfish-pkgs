# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       love

# >> macros
# << macros

Summary:    2D game framework
Version:    0.10.0
Release:    1
Group:      Development/Libraries
License:    zlib
URL:        https://love2d.org/
Source0:    https://bitbucket.org/rude/love/downloads/%{name}-%{version}-linux-src.tar.gz
Source100:  love.yaml
Requires:   lua
Requires:   freetype
Requires:   libvorbis
Requires:   libtheora
Requires:   libmodplug
Requires:   physfs
Requires:   OpenAL
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(theora)
BuildRequires:  SDL2-devel
BuildRequires:  libmodplug-devel
BuildRequires:  physfs-devel
BuildRequires:  OpenAL-devel

%description
%{summary}.

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static \
    --disable-mpg123 \
    --with-lua=lua

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

%files
%defattr(-,root,root,-)
%{_bindir}/love
%{_libdir}/liblove*
%{_datadir}/*
# >> files
# << files
