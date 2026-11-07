# Rehearsal feedback — iteration 190 — learning team: hider

## Current graph
```
assign=nearest_object params={'gain': 4.94, 'damp': 0.8, 'tol': 0.26, 'offset': 0.06, 'seg_timeout': 38.83}
  role0 prep: grab box to door_block[align,door] | play: segments then grab box to stay[yaw3,door] lock
  role1 prep: grab box to door_block[align,door] | play: segments then grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.599
- hider win-rate: 0.68
- behaviour detection rates: {"chasing": 0.17, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 43.1
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.25
- seekers entered quadrant: 0.85, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.68, 1.11] | seeker 3 saw hider 1 at play step 38 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:done@12; play0/0:dropped@32; play0/0:timeout@70; prep1/0:dropped@8; prep1/0:done@19; play1/0:dropped@32; play1/0:dropped@35; play1/0:timeout@70
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.37, 1.74] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; prep1/0:dropped@12; play1/0:timeout@70
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.38, 1.6] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play1/0:timeout@70
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.16, 1.03] | seeker 2 saw hider 1 at play step 42 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@16; play0/0:dropped@32; play0/0:timeout@70; prep1/0:dropped@12; prep1/0:done@30; play1/0:dropped@32; play1/0:timeout@70
- p_door=0.50 doors=1 sealed=[False] ramp_inside=True boxes_moved=[1.06, 0.07] | seeker 2 saw hider 1 at play step 43 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@16; play0/0:dropped@32; play0/0:timeout@70; prep1/0:no_target@21; play1/0:dropped@32; play1/0:timeout@70
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.25, 1.54] | seeker 2 saw hider 0 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@15; prep0/0:done@27; play0/0:dropped@32; play0/0:timeout@70; prep1/0:done@11; play1/0:dropped@32; play1/0:timeout@70
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.43, 0.11] | seeker 2 saw hider 0 at play step 43 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@10; prep0/0:done@20; play0/0:dropped@32; play0/0:timeout@70; prep1/0:no_target@13; play1/0:dropped@32; play1/0:timeout@70
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.58, 1.57] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@18; play0/0:dropped@32; play0/0:dropped@44; play0/0:timeout@70; prep1/0:dropped@15; prep1/0:dropped@18; prep1/0:done@23; play1/0:dropped@32; play1/0:timeout@70