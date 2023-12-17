# shellcheck disable=2148
# shellcheck disable=2154
# shellcheck disable=1090
# shellcheck disable=2312
[[ "${TERM_PROGRAM}" == "vscode" ]] && . "$(code --locate-shell-integration-path zsh)"
export ZSH_THEME="devcontainers"
export ZSH=${HOME}/.oh-my-zsh

# shellcheck disable=2034
plugins=(
  git
  zsh-syntax-highlighting
  fasd
  zsh-autosuggestions
  colored-man-pages
)

alias tf='terraform'
alias tfa="terraform apply"
alias tfi="terraform init"
alias tfr="terraform refresh"
alias tfip="terraform init && terraform plan"
alias tfia="terraform init && terraform apply"
alias tfp="terraform plan"
alias tfo="terraform output"
alias tfiru="terraform init --upgrade=true -reconfigure"
alias tfirup="terraform init --upgrade=true -reconfigure && terraform plan"
alias tfd="terraform destroy"
alias tfsl="terraform state list"
tfgrep() {
    grep --include="*.tf" -rl "$1" .
}
tfat() {
    terraform apply --target "$1"
}

# shellcheck disable=2312
eval "$(fasd --init auto)"

alias fzf="fzf --bind 'ctrl-a:select-all+accept' -m"

# shellcheck disable=1091
source "${ZSH}/oh-my-zsh.sh"
export DISABLE_AUTO_UPDATE=true
export DISABLE_UPDATE_PROMPT=true
