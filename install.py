from subprocess import call
from os import chdir, getenv
from os.path import exists, realpath


def c(cmd):
    return call(cmd,shell=True,executable='/bin/bash')

def main():
    """Set up home dir.

    Creates directories, downloads conf, and creates appropriate
    symlinks.  It's idempotent, meaning you can rerun it to update an
    existing install.
    """

    source_dotconfig_directory = "dotconfigs"
    home = realpath(getenv('HOME'))
    chdir(home)

    for d in ('tmp', source_dotconfig_directory):
        if not exists(d):
            print "Creating directory.. %s" % d
            c('mkdir -p %s' % d)

    chdir(source_dotconfig_directory)

    # {ln -T} mean treat destination as a normal file, i.e. don't
    # create file *in* target if target is a dir.  this is needed for
    # the idempotence of {ln ~/v/conf/dot.zsh ~/.zsh}.
    for f in ('.vimrc', '.zshrc'
             ):
        from_ = '%(home)s/%(source_dotconfig_directory)s/dot%(f)s' % locals()
        to = '%(home)s/%(f)s' % locals()
        print "Linking dot config.. %s" % f
        c('ln -Tfs %(from_)s %(to)s'  % locals())

    # .config directory
    for localname, dest in [("terminator.config", "terminator/config")]:
        from_ = '%(home)s/%(source_dotconfig_directory)s/%(localname)s' % locals()
        to_ = '%(home)s/.config/%(dest)s' % locals()
        print "Linking %(localname)s to .config %(dest)s" % locals()
        c('ln -Tfs %(from_)s %(to_)s' %locals())

    # .oh-my-zsh directory
    for localname, dest in [("cobalt2.zsh-theme", "themes/cobalt2.zsh-theme")]:
        from_ = '%(home)s/%(source_dotconfig_directory)s/oh-my-zsh/%(localname)s' % locals()
        to_ = '%(home)s/.oh-my-zsh/%(dest)s' % locals()
        print "Linking %(localname)s to .config %(dest)s" % locals()
        c('ln -Tfs %(from_)s %(to_)s' %locals())

    # Installing fonts
    print "Installing powerline fonts"
    c('bash ./fonts/powerline_fonts/install.sh')


if __name__ == '__main__':
    main()

