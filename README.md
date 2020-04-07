## openplotter-myapp

This is a template to help create apps for OpenPlotter. 

### Installing

Install [openplotter-settings](https://github.com/openplotter/openplotter-settings) for **production**.

#### For production

Download the latest [openplotter-myapp deb package](https://cloudsmith.io/~openplotter/repos/openplotter-external/packages/) and install it:

`sudo dpkg -i openplotter-myapp_x.x.x-xxx_all.deb` 

#### For development

Clone the repository:

`git clone https://github.com/openplotter/openplotter-myapp`

Create the package:

```
cd openplotter-myapp
dpkg-buildpackage -b
```

Install the package:

```
cd ..
sudo dpkg -i openplotter-myapp_x.x.x-xxx_all.deb
```

Run post installation script:

`sudo myappPostInstall`

Run:

`openplotter-myapp`

Make your changes and repeat packaging and installation steps to test. Pull request your changes to github and we will check and add them to the next version of the [Debian package](https://cloudsmith.io/~openplotter/repos/openplotter-external/packages/).

### Documentation

https://openplotter.readthedocs.io

### Support

http://forum.openmarine.net/forumdisplay.php?fid=1