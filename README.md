# sshz

Connects to a server without the necessity of cleaning url.

As I once heard from an old wise dude: "Life is too short to clean the urls by your own." FURLAN, Arthur (20XX)

### Installation

	$ cd ~/Downloads
	$ git clone https://github.com/sergiomafra/sshz
	$ cd sshz
	$ sudo chmod 0500 sshz && sudo cp sshz /usr/local/bin/sshz
	
### Usage

Login by default with root user

Normal:

	sshz 8.8.8.8
	sshz domain.com
	sshz subdomain.domain.com
	sshz http://domain.com
	sshz https://www.subdomain.domain.com/foo/bar
	
With MOSH instead of SSH:

	sshz -m domain.com
