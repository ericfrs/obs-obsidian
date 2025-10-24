#!/bin/bash

OBSIDIAN_USER_FLAGS_FILE="${XDG_CONFIG_HOME:-$HOME/.config}/obsidian/user-flags.conf"

if [[ -f "${OBSIDIAN_USER_FLAGS_FILE}" ]]; then
    OBSIDIAN_USER_FLAGS=$(grep -v '^#' "$OBSIDIAN_USER_FLAGS_FILE")
fi

exec electron /usr/lib64/obsidian/app.asar $OBSIDIAN_USER_FLAGS "$@"
