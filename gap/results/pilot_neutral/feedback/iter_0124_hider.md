# Rehearsal feedback — iteration 124 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 4.7, 'damp': 0.52, 'tol': 0.33, 'offset': 0.16, 'seg_timeout': 38.83}
  role0 prep: [when ramp_inside] grab ramp to climb[align,door] release | play: segments then to stay[yaw0,door] release -> grab box to stay[yaw3,door] lock
  role1 prep: [when ramp_inside] grab ramp to climb[align,door] release | play: segments then to stay[yaw0,door] release -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.396
- hider win-rate: 0.40
- behaviour detection rates: {"chasing": 0.15, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 34.3
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.23
- seekers entered quadrant: 0.85, mean max seeker z: 0.20

## Failure analysis (lost instances)
- p_door=0.75 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.71, 0.04] | seeker 3 saw hider 1 at play step 34 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@16; play0/0:dropped@32; play0/0:done@32; play0/1:timeout@71; prep1/0:no_object@0; play1/0:done@32; play1/1:timeout@71
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 34 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@32; play0/1:dropped@47; play0/1:timeout@71; play1/0:done@32; play1/1:dropped@47; play1/1:timeout@71
- p_door=1.00 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@19; play0/0:dropped@32; play0/0:done@32; play0/1:timeout@71; prep1/0:no_object@0; play1/0:done@32; play1/1:timeout@71
- p_door=0.75 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.32, 0.52] | seeker 2 saw hider 1 at play step 48 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:dropped@6; prep0/0:done@14; play0/0:dropped@32; play0/0:done@32; play0/1:timeout@71; prep1/0:no_object@0; play1/0:done@32; play1/1:timeout@71
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@32; play0/1:timeout@71; play1/0:done@32; play1/1:timeout@71
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[1.12, 0.0] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@11; play0/0:dropped@32; play0/0:done@32; play0/1:timeout@71; prep1/0:no_object@0; play1/0:done@32; play1/1:timeout@71
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@32; play0/1:timeout@71; play1/0:done@32; play1/1:dropped@46; play1/1:timeout@71
- p_door=0.75 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.29, 0.05] | seeker 2 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@25; play0/0:dropped@32; play0/0:done@32; play0/1:timeout@71; prep1/0:no_object@0; play1/0:done@32; play1/1:timeout@71