## Plain Clustering

*For generating data and then trying basic clustering algorithm.*

***Outline***

- [Code](#code)
- [Snapshots](#snapshots)
  - [Uniform](#uniform)
  - [Discrete Squares](#discrete-squares)
  - [Discrete Circles](#discrete-circles)

****

### Code

- ```distribution.py```

  Generates data with different distributions. Currently, three different distributions are included, namely, *uniform, discrete-squares* and *discrete-circles*. The command line execution of these are...

  - *Uniform* : ```python3 distribution.py 0 [size]```
  - *Discrete-Squares* : ```python3 distribution.py 1 [size] [square_count] [square_size]```
  - *Discrete-Circles* : ```python3 distribution.py 2 [size] [circle_count] [circle_radius]```



- ```clustering.py```

  Takes in input file and plots the data colored in different clusters. Reads from the distribution file generated bby above program. The command line execution of this is...

  - *Clustering* : ```python3 clustering.py [no_clusters_required] <same arguments as above>```

****

An example execution could be...

```python3
python3 distribution.py 1 10000 8 100; python3 clustering.py 4 1 10000 8 100

```

****

### Snapshots

Results of executing some code sequences have been attached.

If (not in uniform) no. of clusters required is same as the no. generated then, mostly, we get the desired clustering (each on its own). But we can even force more or less clusters at our freedom.

For uniform distribution, the clustering yields a very suitable map for distribution of uniform set.

#### Uniform

<p align="center">
        <img src = "https://github.com/jaymalk/Basic-Clustering/blob/master/Plots/uniform100000_1.png">
</p>
<p align="center">
        <img src = "https://github.com/jaymalk/Basic-Clustering/blob/master/Plots/uniform100000_2.png">
</p>
<p align="center">
        <img src = "https://github.com/jaymalk/Basic-Clustering/blob/master/Plots/uniform100000_3.png">
</p>
<p align="center">
        <img src = "https://github.com/jaymalk/Basic-Clustering/blob/master/Plots/uniform100000_4.png">
</p>
<p align="center">
        <img src = "https://github.com/jaymalk/Basic-Clustering/blob/master/Plots/uniform100000_5.png">
</p>
<p align="center">
        <img src = "https://github.com/jaymalk/Basic-Clustering/blob/master/Plots/uniform100000_6.png">
</p>
<p align="center">
        <img src = "https://github.com/jaymalk/Basic-Clustering/blob/master/Plots/uniform100000_7.png">
</p>
<p align="center">
        <img src = "https://github.com/jaymalk/Basic-Clustering/blob/master/Plots/uniform100000_8.png">
</p>
<p align="center">
        <img src = "https://github.com/jaymalk/Basic-Clustering/blob/master/Plots/uniform100000_9.png">
</p>
<p align="center">
        <img src = "https://github.com/jaymalk/Basic-Clustering/blob/master/Plots/uniform100000_10_h.png">
</p>

#### Discrete Squares
<p align="center">
        <img src = "https://github.com/jaymalk/Basic-Clustering/blob/master/Plots/plain_3_3_b.png">
</p>
<p align="center">
        <img src = "https://github.com/jaymalk/Basic-Clustering/blob/master/Plots/plain_5_5_b.png">
</p>
<p align="center">
        <img src = "https://github.com/jaymalk/Basic-Clustering/blob/master/Plots/plain_10_10_d.png">
</p>
<p align="center">
        <img src = "https://github.com/jaymalk/Basic-Clustering/blob/master/Plots/plain_10_10_e.png">
</p>

#### Discrete Circles
<p align="center">
        <img src = "https://github.com/jaymalk/Basic-Clustering/blob/master/Plots/plain_3_3_a.png">
</p>
<p align="center">
        <img src = "https://github.com/jaymalk/Basic-Clustering/blob/master/Plots/plain_5_5_c.png">
</p>
<p align="center">
        <img src = "https://github.com/jaymalk/Basic-Clustering/blob/master/Plots/plain_10_10_a.png">
</p>
<p align="center">
        <img src = "https://github.com/jaymalk/Basic-Clustering/blob/master/Plots/plain_10_10_c.png">
</p>

#### Forced
- Circular 6 on 3
<p align="center">
        <img src = "https://github.com/jaymalk/Basic-Clustering/blob/master/Plots/forced_6_3.png">
</p>
