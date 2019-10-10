# Intro

[![Build Status](https://travis-ci.com/cmsax/pyqt-ci-demo.svg?branch=master)](https://travis-ci.com/cmsax/pyqt-ci-demo)

PyQt5 / PySide2 continuous deployment demo. Build PyQt application on macOS and Windows.

## Usage

- Fork this project and install travis-ci on your project.
- Generate a personal access token in GitHub and set GITHUB_OATU_TOKEN variable in travis-ci project setting.
- Create a tag then travis-ci will build your app and push binaries to release.
