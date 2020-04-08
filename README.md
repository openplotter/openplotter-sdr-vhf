## openplotter-sdr-vhf

Suite of applications for SDR reception in VHF range. 

### Installing

Install [openplotter-settings](https://github.com/openplotter/openplotter-settings) for **production**.

#### For production

Install SDR VHF from openplotter-settings app.

#### For development

Install openplotter-sdr-vhf dependencies:

`sudo apt install ...`

Clone the repository:

`git clone https://github.com/openplotter/openplotter-sdr-vhf`

Make your changes and create the package:

```
cd openplotter-sdr-vhf
dpkg-buildpackage -b
```

Install the package:

```
cd ..
sudo dpkg -i openplotter-sdr-vhf_x.x.x-xxx_all.deb
```

Run post-installation script:

`sudo sdrVhfPostInstall`

Run:

`openplotter-sdr-vhf`

Make your changes and repeat package, installation and post-installation steps to test. Pull request your changes to github and we will check and add them to the next version of the [Debian package](https://launchpad.net/~openplotter/+archive/ubuntu/openplotter).

### Documentation

https://openplotter.readthedocs.io

### Support

http://forum.openmarine.net/forumdisplay.php?fid=1