# Rehearsal feedback — iteration 218 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.37, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 38.83}
  role0 prep: grab box to door_block[target,door] lock | play: segments then grab box to stay[yaw3,door] lock -> to door_inside[yaw2,direct] release
  role1 prep: grab box to door_block[target,door] lock | play: segments then grab box to stay[yaw3,door] lock -> to door_inside[yaw2,direct] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.497
- hider win-rate: 0.45
- behaviour detection rates: {"chasing": 0.25, "door_blocking": 0.6, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 37.9
- doors sealed+locked at prep end: 0.68, ramp inside quadrant at prep end: 0.12
- seekers entered quadrant: 0.33, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.18, 1.5] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; prep1/0:no_target@11; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71; play1/1:no_target@71
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.14, 0.94] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@23; play0/0:dropped@32; play0/0:no_object@32; play0/1:done@34; prep1/0:dropped@14; prep1/0:done@25; play1/0:dropped@32; play1/0:no_object@32; play1/1:timeout@71
- p_door=0.00 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[0.82, 1.35] | seeker 2 saw hider 0 at play step 41 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; prep1/0:done@30; play1/0:dropped@32; play1/0:no_object@32; play1/1:done@34
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.37, 0.0] | seeker 3 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; play0/1:no_target@71; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[2.06, 0.02] | seeker 2 saw hider 0 at play step 34 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; prep1/0:dropped@31; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.67, 1.06] | seeker 2 saw hider 0 at play step 39 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@19; play0/0:dropped@32; play0/0:no_object@32; play0/1:done@34; prep1/0:done@25; play1/0:dropped@32; play1/0:no_object@32; play1/1:timeout@71
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.58, 1.81] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@21; play0/0:dropped@32; play0/0:no_object@32; play0/1:done@34; prep1/0:dropped@11; prep1/0:done@23; play1/0:dropped@32; play1/0:no_object@32; play1/1:timeout@71
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.0, 0.44] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@11; play0/0:dropped@32; play0/0:no_object@32; play0/1:done@34; play1/0:timeout@70; play1/1:no_target@71