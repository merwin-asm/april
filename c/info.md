You can install Jansson on Linux with:
```
sudo apt-get install libjansson-dev
```
Or on macOS with:
```
brew install jansson
```

And then compile the C code with:
```
gcc -o main example.c connect_april.c -ljansson
```
Please note that you may need to adjust the Jansson library link depending on your operating system. The provided example assumes a UNIX-like environment.
