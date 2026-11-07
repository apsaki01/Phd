# Rehearsal feedback — iteration 198 — learning team: hider

## Current graph
```
assign=nearest_object params={'gain': 4.94, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 38.83}
  role0 prep: grab box to door_block[align,door] | play: segments then grab box to stay[yaw3,door] lock
  role1 prep: grab box to door_block[align,door] | play: segments then grab box to stay[yaw3,door] lock -> to door_inside[yaw2,direct] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.572
- hider win-rate: 0.55
- behaviour detection rates: {"chasing": 0.12, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 42.1
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.28
- seekers entered quadrant: 0.78, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.94, 1.41] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@12; play0/0:dropped@32; play0/0:timeout@70; prep1/0:done@14; play1/0:dropped@32; play1/0:dropped@35; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.75 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.53, 1.35] | seeker 2 saw hider 1 at play step 39 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@11; play0/0:dropped@32; play0/0:timeout@70; prep1/0:dropped@10; prep1/0:dropped@13; prep1/0:done@24; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.56, 1.39] | seeker 3 saw hider 1 at play step 39 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@12; play0/0:dropped@32; play0/0:timeout@70; prep1/0:no_target@17; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71; play1/1:no_target@71
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.97, 2.53] | seeker 2 saw hider 1 at play step 53 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:done@22; play0/0:dropped@32; play0/0:timeout@70; prep1/0:done@16; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[1.3, 1.59] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@16; play0/0:dropped@32; play0/0:timeout@70; prep1/0:done@15; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@76
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.57, 0.9] | seeker 3 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@18; play0/0:dropped@32; play0/0:timeout@70; prep1/0:done@19; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.71, 0.21] | seeker 3 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@12; play0/0:dropped@32; play0/0:timeout@70; prep1/0:no_target@18; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71; play1/1:no_target@71
- p_door=0.75 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.83, 2.29] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@19; play0/0:dropped@32; play0/0:timeout@70; prep1/0:done@26; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@79