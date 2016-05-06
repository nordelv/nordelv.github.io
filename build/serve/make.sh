#!/bin/bash
jekyll build
git add --all
git commit -m 'test'
git push
