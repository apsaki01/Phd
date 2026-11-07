# Rehearsal feedback — iteration 172 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 4.94, 'damp': 0.8, 'tol': 0.33, 'offset': 0.24, 'seg_timeout': 38.83}
  role0 prep: grab box to door_block[align,door] | play: segments then [when ramp_inside] grab box to quadrant_interior[yaw3,direct] lock -> grab box to outside_wall[yaw2,door] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to door_block[align,door] | play: segments then [when ramp_inside] grab box to quadrant_interior[yaw3,direct] lock -> grab box to outside_wall[yaw2,door] -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.393
- hider win-rate: 0.35
- behaviour detection rates: {"chasing": 0.05, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 37.4
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.20
- seekers entered quadrant: 0.68, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=1.00 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.27, 0.48] | seeker 3 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@13; prep0/0:done@23; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; play0/1:no_object@71; play0/2:no_object@72; prep1/0:no_target@18; play1/0:dropped@32; play1/0:done@43
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.71, 0.79] | seeker 3 saw hider 0 at play step 37 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@6; play0/0:timeout@70; play0/1:dropped@71; prep1/0:no_target@15; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.57, 0.54] | seeker 3 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@15; play0/0:timeout@70; play0/1:dropped@71; prep1/0:done@12; play1/0:timeout@70; play1/1:dropped@71
- p_door=1.00 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.0, 0.74] | seeker 3 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@25; play0/0:dropped@32; play0/0:done@36; play0/1:timeout@75; play0/2:dropped@76; play0/2:no_object@76; prep1/0:dropped@2; prep1/0:dropped@10; prep1/0:done@14; play1/0:dropped@32; play1/0:done@35; play1/1:timeout@74; play1/2:dropped@75
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.93, 1.12] | seeker 2 saw hider 1 at play step 38 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:done@16; play0/0:timeout@70; play0/1:dropped@71; prep1/0:done@17; play1/0:timeout@70; play1/1:dropped@71; play1/1:dropped@78
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.91, 2.12] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@19; play0/0:timeout@70; prep1/0:done@20; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.77, 0.83] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@15; play0/0:timeout@70; play0/1:dropped@71; prep1/0:done@14; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[2.1, 2.33] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@31; play0/0:done@39; play0/1:timeout@78; play0/2:dropped@79; play0/2:no_object@79; prep1/0:dropped@19; prep1/0:done@29; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@72