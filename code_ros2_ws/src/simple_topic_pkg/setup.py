from setuptools import setup

package_name = 'simple_topic_pkg'

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
    maintainer='ksh3717',
    maintainer_email='ksh3717@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'publisher_script = simple_topic_pkg.publisher:main',
        	'subscriber_script = simple_topic_pkg.subscriber:main'
        ],
    },
)
