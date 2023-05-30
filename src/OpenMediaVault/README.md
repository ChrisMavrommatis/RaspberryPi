# OpenMediaVault

## Installation on Raspberry Pi

- Needs Lite Os image
- Has Specific Script Install
  https://github.com/OpenMediaVault-Plugin-Developers/installScript

## Mounting ExFat Dive and resolving the user permisison issue

- Install exfat-fuse
- Make new user
- Mount the filesystem through OMV
- Edit the fstab '/etc/fstab' to mount the drive using exfat-fuse insteead of exfat and add the user and group id
  The final entry will look comething like this
  ```
  # >>> [openmediavault]
  /dev/disk/by-uuid/[DISKUUID]             /srv/dev-disk-by-uuid-[DISKUUID] exfat      defaults,nofail,uid={USERID},gid={GROUPID}        0 2
  # <<< [openmediavault]
  ```
- Procceed with making the shared folder with permission access to everyone.
- Add the smb share and enable



