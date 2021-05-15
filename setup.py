import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="graph_notes",
    version="0.0.1",
    author="Benjamin Black",
    author_email="benblack769@gmail.com",
    description="Graph based note display engine based on HTML",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/benblack769/graph-notes",
    keywords=["notes", "visualization"],
    packages=setuptools.find_packages(),
    install_requires=[],
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    scripts=['bin/generate-graph-notes'],
    include_package_data=True,
    package_data={'': ['*',"static/*","static/fonts/*","templates/*"]}
)
