# Rehearsal feedback — iteration 226 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.2, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 34.2}
  role0 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock | play: segments then grab box to stay[yaw3,door] lock -> to door_inside[yaw2,direct] release
  role1 prep: grab box to door_block[align,door] -> grab box to door_block[target,door] lock | play: segments then grab box to stay[yaw3,door] lock -> to door_inside[yaw2,direct] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.715
- hider win-rate: 0.72
- behaviour detection rates: {"chasing": 0.3, "door_blocking": 0.72, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 37.3
- doors sealed+locked at prep end: 0.78, ramp inside quadrant at prep end: 0.15
- seekers entered quadrant: 0.23, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.50 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[0.84, 1.52] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@66; play0/1:dropped@67; prep1/0:done@27; prep1/1:done@30; play1/0:dropped@32; play1/0:no_object@32; play1/1:done@36
- p_door=0.25 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.77, 1.57] | seeker 3 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@12; prep0/1:dropped@13; prep0/1:dropped@21; prep0/1:done@30; play0/0:dropped@32; play0/0:timeout@66; play0/1:dropped@67; play0/1:done@68; prep1/0:no_target@13; prep1/1:dropped@14; prep1/1:no_target@16; play1/0:dropped@32; play1/0:dropped@34; play1/0:timeout@66; play1/1:dropped@67; play1/1:no_target@67
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.92, 0.33] | seeker 2 saw hider 0 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@9; prep0/0:dropped@15; prep0/0:dropped@19; play0/0:timeout@66; play0/1:dropped@67; play0/1:done@74; prep1/0:no_target@24; prep1/1:dropped@25; prep1/1:no_target@26; play1/0:dropped@32; play1/0:dropped@35; play1/0:timeout@66; play1/1:dropped@67; play1/1:no_target@67
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.21, 1.68] | seeker 3 saw hider 1 at play step 39 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@26; prep0/1:dropped@27; prep0/1:done@30; play0/0:dropped@32; play0/0:no_object@32; play0/1:timeout@67; prep1/0:done@24; prep1/1:done@29; play1/0:dropped@32; play1/0:no_object@32; play1/1:done@34
- p_door=0.75 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[1.93, 2.59] | seeker 3 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.25) | segments: prep0/0:done@10; prep0/1:dropped@11; prep0/1:done@14; play0/0:dropped@32; play0/0:no_object@32; play0/1:done@38; play1/0:timeout@66; play1/1:dropped@67
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.15, 0.88] | seeker 2 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@9; play0/0:timeout@66; play0/1:dropped@67; play0/1:done@68; play1/0:timeout@66; play1/1:dropped@67
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.2, 1.02] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@14; prep0/1:dropped@15; play0/0:timeout@66; play0/1:dropped@67; play0/1:done@68; prep1/0:no_target@17; prep1/1:dropped@18; prep1/1:no_target@19; play1/0:dropped@32; play1/0:no_object@32; play1/1:no_target@33
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.34, 1.28] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@15; prep0/1:dropped@16; prep0/1:done@20; play0/0:dropped@32; play0/0:no_object@32; play0/1:done@34; prep1/0:dropped@14; prep1/0:done@24; prep1/1:done@27; play1/0:dropped@32; play1/0:no_object@32; play1/1:timeout@67