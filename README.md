# DeadDNS
 Multi-threaded **DNS hijacking** via **dead records** automation tool

## How it works
```
1) Dig provided subdomains file for dead DNS records.
2) Dig the found dead DNS records for any interesting CNAME's. 
3) Show which dead record points to the given CNAME.
```

<<<<<<< HEAD
![](https://j.gifs.com/ANvnK3.gif)
=======
![](https://j.gifs.com/jZoEJB.gif)
>>>>>>> dev

## Features
- Multi-threading
- Completely Automated
- Takes list from file

## Installation:
One line installation:
```
$ git clone https://github.com/DreyAnd/DeadDNS.git && cd DeadDNS && pip3 install -r requirements.txt
```

Simple and quick installation:
```
$ git clone https://github.com/DreyAnd/DeadDNS.git
$ cd DeadDNS
$ pip3 install -r requirements.txt
```

## Usage:

Example usage:
```
<<<<<<< HEAD
$ python3 dead_records.py -w subdomains.txt -o1 dead.txt -o2 cname.txt -t 2
```
=======
$ python3 dead_records.py -w subdomains.txt -o1 dead.txt -o2 cname.txt
```

>>>>>>> dev
This will return all output to stdout without saving it.

Help: `$ python3 dead_records.py -h`

<<<<<<< HEAD
To check progress do `tail -f dead-temp.txt` and `tail -f cname-temp.txt`

## Current version:
### **1.2**

## What's new?

> Better UI

> Concurrent multithreading

> Fixed bugs

> Custom number of threads
=======
To check progess do `tail -f dead-temp.txt` and `tail -f cname-temp.txt`
>>>>>>> dev

## Made with :heart: by [DreyAnd](https://github.com/DreyAnd) and [inc0gnit0](https://github.com/iinc0gnit0)
