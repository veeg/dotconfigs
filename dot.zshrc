###
### Environment
###

# Configure starship command line prompt
eval "$(starship init zsh)"

export PATH="$HOME/bin:/usr/local/bin:/usr/bin:/bin:/usr/bin/X11:/usr/games:$HOME/.rvm/bin:$HOME/.rvm/bin"
# rustlang
export PATH="$PATH:/$HOME/.cargo/bin"
export STARSHIP_CONFIG="$HOME/.starship.toml"


###
### Alias
###

alias open="open_command"
alias vim="gvim -v"

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
