# OneTrack

A simple library for evaluation of particle track reconstruction.

## Alpha Version!

This library is in a very early stage of development. It is only for testing with a narrow set of Pytorch Geometric data types. It is not recommended for production use.

## Example Usage

```
from onetrack import TrackingData 
from onetrack.file_utils import list_files
```

1. Load in files
```
file_list = list_files(os.path.join(config["graph_input_dir"], "train"))[:100]
```

2. Create a TrackingData object
```
tracking_data = TrackingData(file_list)
```

Currently, the only supported file configuration is as follows:

a) `file_list` contains a list of pickled Pytorch Geometric `Data` objects

b) Each `Data` object contains:
- a list of edges in `edge_index`, 
- a list of edge `scores`, 
- a list of hit IDs `hid` that can be used to map the nodes used in `edge_index` back to the original hits in the event
- a string `event_file` that can be used to load the original event files
- at least a truth tensor called `y`, and possibly more truth tensors with the format `y_{truth definition}`

c) The event files are assumed to be of the format:
- `{event_file}-particles.csv` and `{event_file}-truth.csv`
- The `-particles` file should contain at least `particle_id` and `pt` columns
- The `-truth` file should contain at least `particle_id` and `hit_id` columns

**Better compatibility is coming ASAP!**

3. Run a sanity check by building track candidates with the truth
```
tracking_data.build_candidates(building_method="CC", sanity_check=True)
```

4. Evaluate this sanity check 
```
tracking_data.evaluate_candidates(evaluation_method="matching")
tracking_data.plot_evaluation()
```

If all has worked, we should get very good efficiency and fake rates. We can then play around with candidate building (with `sanity_check=False`), and evaluating with different matching configurations:
```
matching_config = {
    "min_hits_truth": 9,
    "min_hits_reco": 5,
    "frac_reco_matched": 0.5,
    "frac_truth_matched": 0.5,
}
tracking_data.evaluate_candidates(evaluation_method="matching", **matching_config)
```