Name: librabbitmq
Summary: C-language AMQP client library
Version: 0.8.0
Release: 2%{?dist}
License: MIT
Group: System Environment/Libraries
URL: https://github.com/alanxz/rabbitmq-c
Source0: https://github.com/alanxz/rabbitmq-c/releases/download/v%{version}/rabbitmq-c-%{version}.tar.gz

BuildRequires: cmake > 2.8
BuildRequires: openssl-devel
BuildRequires: popt-devel
BuildRequires: xmlto
BuildRequires: doxygen

%description
This is a C-language AMQP client library for use with v2.0+ of
the RabbitMQ broker.

%package devel
Summary: Header files and development libraries for librabbitmq
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files and development libraries
for librabbitmq.

%package examples
Summary: Examples built using the librabbitmq
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description examples
This package contains examples built using librabbitmq.

%prep
%setup -q -n rabbitmq-c-%{version}

%build
%cmake -DBUILD_EXAMPLES:BOOL=ON \
       -DBUILD_TOOLS_DOCS:BOOL=ON \
       -DBUILD_STATIC_LIBS:BOOL=ON

make %{_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# drop static lib, it's only needed for tests
rm %{buildroot}%{_libdir}/*.a

%check
make test

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%license LICENSE-MIT
%{_libdir}/%{name}.so.*

%files devel
%doc AUTHORS THANKS TODO *.md
%{_libdir}/%{name}.so
%{_includedir}/amqp*
%{_libdir}/pkgconfig/%{name}.pc

%files examples
%{_bindir}/amqp-*
%doc %{_mandir}/man*/*

%changelog
* Mon Dec 04 2017 Than Ngo <than@redhat.com> - 0.8.0-2
- Related: #1363736 - fix explicit package version requirement

* Wed Nov 29 2017 Than Ngo <than@redhat.com> - 0.8.0-1
- Initial RPM
