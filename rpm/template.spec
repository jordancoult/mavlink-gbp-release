Name:           ros-indigo-mavlink
Version:        2016.1.2
Release:        1%{?dist}
Summary:        ROS mavlink package

Group:          Development/Libraries
License:        LGPLv3
URL:            http://qgroundcontrol.org/mavlink/
Source0:        %{name}-%{version}.tar.gz

Requires:       python-devel
Requires:       ros-indigo-catkin
BuildRequires:  cmake
BuildRequires:  python-devel

%description
MAVLink message marshaling library. This package provides C-headers and
pymavlink library.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sat Jan 02 2016 Vladimir Ermakov <vooon341@gmail.com> - 2016.1.2-1
- Autogenerated by Bloom

* Sat Jan 02 2016 Vladimir Ermakov <vooon341@gmail.com> - 2016.1.2-0
- Autogenerated by Bloom

* Sat Dec 12 2015 Vladimir Ermakov <vooon341@gmail.com> - 2015.12.12-0
- Autogenerated by Bloom

* Wed Nov 25 2015 Vladimir Ermakov <vooon341@gmail.com> - 2015.11.25-0
- Autogenerated by Bloom

* Wed Nov 11 2015 Vladimir Ermakov <vooon341@gmail.com> - 2015.11.11-0
- Autogenerated by Bloom

* Sat Oct 10 2015 Vladimir Ermakov <vooon341@gmail.com> - 2015.10.10-0
- Autogenerated by Bloom

* Wed Sep 09 2015 Vladimir Ermakov <vooon341@gmail.com> - 2015.9.9-0
- Autogenerated by Bloom

* Sat Aug 08 2015 Vladimir Ermakov <vooon341@gmail.com> - 2015.8.8-0
- Autogenerated by Bloom

* Tue Jul 07 2015 Vladimir Ermakov <vooon341@gmail.com> - 2015.7.7-0
- Autogenerated by Bloom

* Fri Jun 12 2015 Vladimir Ermakov <vooon341@gmail.com> - 2015.6.12-0
- Autogenerated by Bloom

* Sat Jun 06 2015 Vladimir Ermakov <vooon341@gmail.com> - 2015.6.6-0
- Autogenerated by Bloom

* Mon May 18 2015 Vladimir Ermakov <vooon341@gmail.com> - 2015.5.18-0
- Autogenerated by Bloom

* Tue May 05 2015 Vladimir Ermakov <vooon341@gmail.com> - 2015.5.5-0
- Autogenerated by Bloom

* Sat Apr 04 2015 Vladimir Ermakov <vooon341@gmail.com> - 2015.4.4-0
- Autogenerated by Bloom

* Wed Mar 11 2015 Vladimir Ermakov <vooon341@gmail.com> - 2015.3.11-0
- Autogenerated by Bloom

* Tue Mar 03 2015 Vladimir Ermakov <vooon341@gmail.com> - 2015.3.3-0
- Autogenerated by Bloom

* Wed Feb 25 2015 Vladimir Ermakov <vooon341@gmail.com> - 2015.2.25-0
- Autogenerated by Bloom

* Mon Feb 02 2015 Vladimir Ermakov <vooon341@gmail.com> - 2015.2.2-0
- Autogenerated by Bloom

* Wed Jan 21 2015 Vladimir Ermakov <vooon341@gmail.com> - 2015.1.21-1
- Autogenerated by Bloom

* Wed Jan 21 2015 Vladimir Ermakov <vooon341@gmail.com> - 2015.1.21-0
- Autogenerated by Bloom

* Fri Dec 12 2014 Vladimir Ermakov <vooon341@gmail.com> - 2014.12.12-1
- Autogenerated by Bloom

* Fri Dec 12 2014 Vladimir Ermakov <vooon341@gmail.com> - 2014.12.12-0
- Autogenerated by Bloom

* Tue Nov 11 2014 Vladimir Ermakov <vooon341@gmail.com> - 2014.11.11-3
- Autogenerated by Bloom

* Tue Nov 11 2014 Vladimir Ermakov <vooon341@gmail.com> - 2014.11.11-2
- Autogenerated by Bloom

* Tue Nov 11 2014 Vladimir Ermakov <vooon341@gmail.com> - 2014.11.11-1
- Autogenerated by Bloom

* Tue Nov 11 2014 Vladimir Ermakov <vooon341@gmail.com> - 2014.11.11-0
- Autogenerated by Bloom

* Wed Oct 01 2014 Vladimir Ermakov <vooon341@gmail.com> - 2014.10.01-0
- Autogenerated by Bloom

* Mon Sep 22 2014 Vladimir Ermakov <vooon341@gmail.com> - 2014.09.22-0
- Autogenerated by Bloom

* Wed Sep 10 2014 Vladimir Ermakov <vooon341@gmail.com> - 2014.09.10-0
- Autogenerated by Bloom

* Mon Aug 25 2014 Vladimir Ermakov <vooon341@gmail.com> - 1.0.9-10
- Autogenerated by Bloom

* Sat Aug 09 2014 Vladimir Ermakov <vooon341@gmail.com> - 1.0.9-9
- Autogenerated by Bloom

* Fri Aug 08 2014 Vladimir Ermakov <vooon341@gmail.com> - 1.0.9-8
- Autogenerated by Bloom

