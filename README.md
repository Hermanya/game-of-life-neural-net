https://www.tensorflow.org/install/install_mac#installing_with_virtualenv

![ui for game of life neural net](https://media.giphy.com/media/xT0xeEh9PY3KVJn6ow/giphy.gif)

# Run ui
```
open http://localhost:8000
python -m SimpleHTTPServer
```

# Make a model
```
python synthesize_data.py
python make_model.py
./tf2dljs.sh # this requires you to clone deeplearnjs in the parent folder
# and deeplearnjs requires pytorch
```

# NDArray is disposed
```
deeplearn.js:8099 Uncaught (in promise) Error: NDArray is disposed.
    at Array1D.NDArray.throwIfDisposed (deeplearn.js:8099)
    at Array1D.NDArray.dataSync (deeplearn.js:8057)
    at Array1D.<anonymous> (deeplearn.js:8051)
    at step (deeplearn.js:7802)
    at Object.next (deeplearn.js:7783)
    at fulfilled (deeplearn.js:7774)
```
**Use dataSync inside scope**
