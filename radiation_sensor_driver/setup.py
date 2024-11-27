import os
from glob import glob
from setuptools import find_packages, setup

package_name = "radiation_sensor_driver"

setup(
    name=package_name,
    version="0.1.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        (
            os.path.join("share", package_name, "launch"),
            glob(os.path.join("launch", "*launch.[pxy][yma]*")),
        ),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Jakub Delicat",
    maintainer_email="delicat.kuba@gmail.com",
    description="ROS 2 driver for BG51 Radiation Sensor",
    license="Apache-2.0",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "radiation_sensor_driver = radiation_sensor_driver.radiation_sensor_driver:main"
        ],
    },
)
