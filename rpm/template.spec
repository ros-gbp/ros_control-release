Name:           ros-indigo-rqt-controller-manager
Version:        0.9.7
Release:        0%{?dist}
Summary:        ROS rqt_controller_manager package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rqt_controller_manager
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-controller-manager
Requires:       ros-indigo-rqt-gui
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-controller-manager
BuildRequires:  ros-indigo-rqt-gui

%description
The rqt_controller_manager package

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
        -DCMAKE_INSTALL_LIBDIR="lib" \
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
* Sat May 19 2018 Kelsey Hawkins <kphawkins@gatech.edu> - 0.9.7-0
- Autogenerated by Bloom

* Mon Apr 16 2018 Kelsey Hawkins <kphawkins@gatech.edu> - 0.9.6-0
- Autogenerated by Bloom

* Mon Mar 26 2018 Kelsey Hawkins <kphawkins@gatech.edu> - 0.9.5-0
- Autogenerated by Bloom

* Fri Feb 12 2016 Kelsey Hawkins <kphawkins@gatech.edu> - 0.9.4-0
- Autogenerated by Bloom

* Tue May 05 2015 Kelsey Hawkins <kphawkins@gatech.edu> - 0.9.3-0
- Autogenerated by Bloom

* Mon May 04 2015 Kelsey Hawkins <kphawkins@gatech.edu> - 0.9.2-0
- Autogenerated by Bloom

