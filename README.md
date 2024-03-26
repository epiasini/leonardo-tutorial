# Scripts for Leonardo tutorial

This repository contains a few example scripts that can be useful to understand how to run embarassingly parallel computation on Leonardo@CINECA. These are adapted from [a very useful guide on the Stony Brook website](https://it.stonybrook.edu/help/kb/a-guide-to-embarrassingly-parallel-workflows-on-seawulf), which you should read to understand better the context and also how to easily run this same type of computations on regular computers (such as workstations and laptops), for instance by using [gnu parallel](https://www.gnu.org/software/parallel/).

The computational task we want to solve with the code in this repo is to compute the square of a bunch of numbers in a certain range, and to plot the resulting curve. To do this, we split the problem in many sub-problems, where the square of each individual value is computed in parallel with a job array. This is done by submitting the job described by `raise_to_power_array_jobscript.sh` to the slirm queue, with something like
```
sbatch raise_to_power_array_jobscript.sh
```
If you look inside the jobscript, you will see that to run the actual computation is described within a separate script, `raise_to_power_array.py`. Note that the code is written in such a way that the result of the computation is written on the standard output (that is, we just `print()` it from Python), which we save in a file named with a specific pattern. This pattern is specified with the following directive in the jobscript:
```
#SBATCH --output=/leonardo/home/<...etc etc...>/%3a.out
```
Apart from the file location, the `%3a.out` template means that the job number 0 in the job array will save its standard output in `000.out`, job number 1 in `001.out`, etc. There is a flexible mechanism for constructing file names with various variables of interest (such as the job id, job name, etc); you can find all the variables listed in the [documentation](https://slurm.schedmd.com/sbatch.html#SECTION_%3CB%3Efilename-pattern%3C/B%3E) for slurm. Note that an alternative way of saving the output of the individual processes would be to arrange for each of them to write a file to a specific location unique to that process (there are more sophisticated things you could do, but these are outside the scope of this tutorial).

After this is done and the jobs are over, using `parse_and_plot.py` we load all results of the embarassingly parallel computation and we put them together to make a plot. This is performed inside `parse_and_plot.py`.

This task, although trivial, hopefully highlights a very common and powerful pattern, where we take a big problem, break it down in a long list of smaller independent problems, solve them all independently in parallel, arrange for each sub-solution to be written in a specific place on disk, and finally run a script that reads back in all solutions to the sub-problems and assembles the solution to the original problem. This is very common, for instance when doing parameter sweeps when fitting or simulating models, or when - say - fitting statistical models to many subjects or replicates of the data that can be treated independently.