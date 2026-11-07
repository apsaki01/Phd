# Rehearsal feedback — iteration 48 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 6.0, 'damp': 0.47, 'tol': 0.32, 'offset': 0.16, 'seg_timeout': 36.09}
  role0 prep: to door_inside[target,direct] release -> [when teammate_inside] grab box to climb[align,door] lock | play: go(teammate,door)
  role1 prep: grab ramp to ramp_inside[yaw3,direct] release | play: segments then grab box to door_block[yaw3,door] lock release -> [when teammate_inside] grab box to teammate[align,direct]
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.161
- hider win-rate: 0.10
- behaviour detection rates: {"chasing": 0.05, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.12}
- mean first-seen play step: 34.7
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.30
- seekers entered quadrant: 0.78, mean max seeker z: 0.22

## Failure analysis (lost instances)
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:dropped@14; play1/0:no_target@32; play1/1:dropped@43; play1/1:timeout@69
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.0, 0.11] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@5; prep0/1:done@15; prep1/0:done@22; play1/0:dropped@32; play1/0:done@54; play1/1:dropped@55
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@1; play1/0:timeout@68; play1/1:dropped@69
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@12; play1/0:done@41; play1/1:dropped@42; play1/1:timeout@78
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.0, 0.0] | seeker 3 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play1/0:timeout@68; play1/1:dropped@69
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.26, 0.28] | seeker 3 saw hider 1 at play step 52 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:done@0; prep0/1:done@7; prep1/0:done@8; play1/0:dropped@32; play1/0:no_object@32; play1/1:no_object@33
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.36, 0.0] | seeker 3 saw hider 0 at play step 47 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@1; prep0/1:dropped@31; play1/0:done@42; play1/1:dropped@43; play1/1:timeout@79
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.37, 0.0] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@4; prep0/1:done@22; prep1/0:dropped@6; play1/0:no_target@32; play1/1:dropped@33; play1/1:timeout@69