#!/bin/sh

WORD="collecting" # word that the student mis-pronounced. (main.py has a function create_intervention which can be used in an automated pipeline)
CONTEXT="New tools, like data collecting robots, helped the ship be discovered." # the context in which the above word is used.
WRITE_PATH="./dynamic_interventions/" # path to save the interventions
LLM_CONF_PATH="llm_config.json" # this is the config path

python main.py \
    --write_path "$WRITE_PATH" \
    --llm_conf_path "$LLM_CONF_PATH" \
    --word="$WORD" \
    --context="$CONTEXT" \
    --static "True" # remove this flag for dynamic interventions

python read_interventions.py \
    --read_path "$WRITE_PATH" 