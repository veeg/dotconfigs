###
### Environment
###

# Bring in all rust paths
source "$HOME/.cargo/env"

# Configure starship command line prompt
eval "$(starship init zsh)"

export EDITOR=vim

export PATH="$HOME/bin:/usr/local/bin:/usr/bin:/bin:/usr/bin/X11:/usr/games"
# rustlang
export PATH="$PATH:/$HOME/.cargo/bin"
export STARSHIP_CONFIG="$HOME/.starship.toml"

# NOTE: This requires the rust-src component (rustup component add rust-src)
export RUST_SRC_PATH="$(rustc --print sysroot)/lib/rustlib/src/rust/src"


###
### Alias
###

alias open="xdg-open"
alias vim="gvim -v"
alias less="less -S"

function ws-replace {
    sed --in-place 's/[[:space:]]\+$//' $1
}
function ws-rreplace {
    find $1 -type f -exec sed --in-place 's/[[:space:]]\+$//' {} \+
}

###
### Enter TMUX
###

if command -v tmux &> /dev/null && [ -n "$PS1" ] && [[ ! "$TERM" =~ screen ]] && [[ ! "$TERM" =~ tmux ]] && [ -z "$TMUX" ]; then
  exec tmux
fi
