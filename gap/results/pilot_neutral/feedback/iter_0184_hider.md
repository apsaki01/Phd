# Rehearsal feedback — iteration 184 — learning team: hider

## Current graph
```
assign=nearest_object params={'gain': 4.94, 'damp': 0.8, 'tol': 0.26, 'offset': 0.24, 'seg_timeout': 38.83}
  role0 prep: grab box to door_block[align,door] | play: segments then grab box to outside_wall[yaw2,door] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to door_block[align,door] | play: segments then grab box to outside_wall[yaw2,door] -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.521
- hider win-rate: 0.50
- behaviour detection rates: {"chasing": 0.17, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 40.0
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.15
- seekers entered quadrant: 0.50, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.25 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.99, 0.52] | seeker 2 saw hider 1 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@19; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; prep1/0:no_target@18; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.81, 1.45] | seeker 2 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@6; prep0/0:dropped@11; prep0/0:done@18; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; prep1/0:dropped@12; prep1/0:done@15; play1/0:dropped@32; play1/0:done@40; play1/1:timeout@79
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.09, 2.11] | seeker 3 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.95, 0.25] | seeker 2 saw hider 1 at play step 48 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@25; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; prep1/0:dropped@15; prep1/0:done@25; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.37, 1.76] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@15; prep0/0:done@19; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; prep1/0:done@11; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.88, 0.23] | seeker 2 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; prep1/0:done@29; play1/0:dropped@32; play1/0:done@37; play1/1:timeout@76
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[2.07, 1.37] | seeker 2 saw hider 0 at play step 36 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@18; play0/0:dropped@32; play0/0:done@35; play0/1:timeout@74; prep1/0:dropped@17; prep1/0:dropped@24; prep1/0:done@29; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.14, 1.03] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@13; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; prep1/0:done@16; play1/0:dropped@32; play1/0:done@40; play1/1:dropped@43; play1/1:timeout@79