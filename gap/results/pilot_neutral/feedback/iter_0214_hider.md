# Rehearsal feedback — iteration 214 — learning team: hider

## Current graph
```
assign=nearest_object params={'gain': 4.77, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 38.83}
  role0 prep: grab box to door_block[target,door] | play: segments then grab box to stay[yaw3,door] lock -> to door_inside[yaw2,direct] release
  role1 prep: grab box to door_block[target,door] lock | play: segments then grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.546
- hider win-rate: 0.53
- behaviour detection rates: {"chasing": 0.15, "door_blocking": 0.17, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 40.5
- doors sealed+locked at prep end: 0.35, ramp inside quadrant at prep end: 0.20
- seekers entered quadrant: 0.62, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.58, 1.6] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@28; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; prep1/0:no_target@24; play1/0:dropped@32; play1/0:timeout@70
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.41, 1.9] | seeker 2 saw hider 1 at play step 39 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@18; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; play0/1:done@79; prep1/0:no_target@21; play1/0:dropped@32; play1/0:timeout@70
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.46, 2.39] | seeker 2 saw hider 0 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@12; play0/0:dropped@32; play0/0:no_object@32; play0/1:timeout@71; prep1/0:done@24; play1/0:dropped@32; play1/0:no_object@32
- p_door=0.25 doors=2 sealed=[True, False] ramp_inside=True boxes_moved=[0.95, 1.67] | seeker 3 saw hider 1 at play step 49 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@14; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; prep1/0:done@14; play1/0:dropped@32; play1/0:no_object@32
- p_door=0.25 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[1.32, 1.19] | seeker 3 saw hider 1 at play step 42 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@12; prep0/0:done@19; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; prep1/0:done@12; play1/0:dropped@32; play1/0:no_object@32
- p_door=0.50 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[1.22, 1.24] | seeker 3 saw hider 1 at play step 40 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@18; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; prep1/0:dropped@2; prep1/0:done@14; play1/0:dropped@32; play1/0:no_object@32
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.69, 0.07] | seeker 3 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; play0/1:no_target@71; play1/0:timeout@70
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.0, 0.6] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; play1/0:timeout@70