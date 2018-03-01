#!/usr/bin/env bash


for f in $(ls data); do
    python3 main.py data/$f > output/$f
done