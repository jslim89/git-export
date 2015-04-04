# Git export
Everytime, when comes to manual deployment, I always refer to BitBucket repo to see which files I have changed, which not very efficient. This small script can helps to export those commited file(s) from a revision to a revision to an external folder.

## Usage

```sh
$ python git-export.py -f 977b5d1
$ python git-export.py -f 977b5d1 -t 8e5ad17
$ python git-export.py -n 4 -o ~/Desktop
```

### Options

- `-f` or `--from-revision`: from revision
- `-t` or `--to-revision`: to revision
- `-n` or `--num-of-revisions`: number of revisions (integer) start from the last revision
- `-o` or `--output`: output destination

## License
Released under [GPL](http://www.gnu.org/licenses/gpl.html)
