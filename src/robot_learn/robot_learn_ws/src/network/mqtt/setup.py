from setuptools import setup

package_name = 'mqtt'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='htc',
    maintainer_email='htc@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "mqtt_test_node = mqtt.mqtt_test:main",
            "subscriber_node = mqtt.subscriber_node:main"
        ],
    },
)
