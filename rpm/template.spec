Name:           ros-lunar-rqt-controller-manager
Version:        0.13.2
Release:        0%{?dist}
Summary:        ROS rqt_controller_manager package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rqt_controller_manager
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-lunar-controller-manager
Requires:       ros-lunar-rqt-gui
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-controller-manager
BuildRequires:  ros-lunar-rqt-gui

%description
The rqt_controller_manager package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Mon Apr 16 2018 Kelsey Hawkins <kphawkins@gatech.edu> - 0.13.2-0
- Autogenerated by Bloom

* Mon Mar 26 2018 Kelsey Hawkins <kphawkins@gatech.edu> - 0.13.1-0
- Autogenerated by Bloom

* Sat Dec 23 2017 Kelsey Hawkins <kphawkins@gatech.edu> - 0.13.0-0
- Autogenerated by Bloom

* Sat Aug 05 2017 Kelsey Hawkins <kphawkins@gatech.edu> - 0.12.0-0
- Autogenerated by Bloom

* Wed Jun 28 2017 Kelsey Hawkins <kphawkins@gatech.edu> - 0.11.5-0
- Autogenerated by Bloom

* Tue Apr 11 2017 Kelsey Hawkins <kphawkins@gatech.edu> - 0.11.4-0
- Autogenerated by Bloom

