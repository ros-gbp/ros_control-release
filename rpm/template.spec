Name:           ros-jade-ros-control
Version:        0.10.0
Release:        0%{?dist}
Summary:        ROS ros_control package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/ros_control
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-jade-control-toolbox
Requires:       ros-jade-controller-interface
Requires:       ros-jade-controller-manager
Requires:       ros-jade-controller-manager-msgs
Requires:       ros-jade-controller-manager-tests
Requires:       ros-jade-hardware-interface
Requires:       ros-jade-joint-limits-interface
Requires:       ros-jade-realtime-tools
Requires:       ros-jade-transmission-interface
BuildRequires:  ros-jade-catkin

%description
A set of packages that include controller interfaces, controller managers,
transmissions, hardware_interfaces and the control_toolbox.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Fri Nov 20 2015 Adolfo Rodriguez Tsouroukdissian <adolfo.rodriguez@pal-robotics.com> - 0.10.0-0
- Autogenerated by Bloom

