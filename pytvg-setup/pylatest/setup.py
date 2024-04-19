import setuptools

setuptools.setup(
    name='python-text-vector-graphics',
    version='0.0.1',
    author='Qiong-Mengzi',
    packages=['TVG'],
    python_requires='>=3.9',
    description='TVG(Text Vector Graphics)',
    license = "MIT Licence",

    entry_points = {
        'console_scripts': [
            'pytvg = TVG.pytvg:curse'
        ]
    }
)
