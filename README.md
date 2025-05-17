# Anoop Sarkar: Compilers class

Course website for the Compilers class called CMT 379 taught by Anoop Sarkar at SFU School of Computing Science

http://anoopsarkar.github.io/compilers-class

Cloned from https://github.com/mt-class/jhu and then modified.

## Installation

Follow the instructions here:

    https://jekyllrb.com/docs/installation/macos/

In particular:

    brew install chruby ruby-install
    ruby-install ruby 3.4.1
    source /opt/homebrew/opt/chruby/share/chruby/chruby.sh
    source /opt/homebrew/opt/chruby/share/chruby/auto.sh
    chruby ruby-3.4.1
    ruby -v

Then:

    gem install jekyll bundler
    bundle add webrick
    bundle install

## Deploy

    bundle exec jekyll serve
