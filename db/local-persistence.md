
# Local Persistence


## Web Apps


## Local Apps


#### Python


##### Pickle

```bash
pip install pickle5
```


```python
import pickle5 as pickle

pb = pickle.PickleBuffer(b"foo")
data = pickle.dumps(pb, protocol=5)
assert pickle.loads(data) == b"foo"
```