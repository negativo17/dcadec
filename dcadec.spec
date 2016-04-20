Name:           dcadec
Version:        0.2.0
Release:        2%{?dist}
Summary:        DTS Coherent Acoustics decoder with support for HD extensions
License:        LGPLv2+
URL:            https://github.com/foo86/dcadec

Source0:        https://github.com/foo86/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

%description
dcadec is a free DTS Coherent Acoustics decoder with support for HD extensions.

Supported features:
- Decoding of standard DTS core streams with up to 5.1 channels
- Decoding of DTS-ES streams with discrete back channel
- Decoding of High Resolution streams with up to 7.1 channels and ext. bit rate
- Decoding of 96/24 core streams
- Lossless decoding of Master Audio streams with up to 7.1 channels, 192 kHz
- Downmixing to stereo and 5.1 using embedded coefficients

Features not implemented:
- Decoding of DTS Express streams
- Applying dynamic range compression and dialog normalization

%package        libs
Summary:        DTS Coherent Acoustics decoder library

%description    libs
dcadec is a free DTS Coherent Acoustics decoder with support for HD extensions.

Supported features:
- Decoding of standard DTS core streams with up to 5.1 channels
- Decoding of DTS-ES streams with discrete back channel
- Decoding of High Resolution streams with up to 7.1 channels and ext. bit rate
- Decoding of 96/24 core streams
- Lossless decoding of Master Audio streams with up to 7.1 channels, 192 kHz
- Downmixing to stereo and 5.1 using embedded coefficients

Features not implemented:
- Decoding of DTS Express streams
- Applying dynamic range compression and dialog normalization

This package contains the shared library.

%package        devel
Summary:        DTS Coherent Acoustics decoder library development files
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
Supported features:
- Decoding of standard DTS core streams with up to 5.1 channels
- Decoding of DTS-ES streams with discrete back channel
- Decoding of High Resolution streams with up to 7.1 channels and ext. bit rate
- Decoding of 96/24 core streams
- Lossless decoding of Master Audio streams with up to 7.1 channels, 192 kHz
- Downmixing to stereo and 5.1 using embedded coefficients

Features not implemented:
- Decoding of DTS Express streams
- Applying dynamic range compression and dialog normalization

This package contains the shared library development files.

%prep
%setup -q
sed -i \
    -e 's/CFLAGS :=.*/CFLAGS := $(CFLAGS)/g' \
    -e 's/install -m 644 $(OUT_LIB)/install -m 755 $(OUT_LIB)/g' \
    Makefile

%build
export CFLAGS="%{optflags} -std=gnu99"
export CONFIG_DEBUG=1
export CONFIG_SHARED=1
#export LDFLAGS="-fPIC"
make %{?_smp_mflags}

%install
export PREFIX=%{_prefix}
export LIBDIR=%{_libdir}
export CONFIG_SHARED=1
%make_install

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%{_bindir}/%{name}

%files libs
%{!?_licensedir:%global license %%doc}
%license COPYING.LGPLv2.1
%doc README.md
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/lib%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Mon Mar 14 2016 Simone Caronni <negativo17@gmail.com> - 0.2.0-2
- Fix compilation on CentOS/RHEL 7

* Fri Mar  4 2016 Simone Caronni <negativo17@gmail.com> - 0.2.0-1
- First build.
