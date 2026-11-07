# Rehearsal feedback — iteration 52 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 6.0, 'damp': 0.47, 'tol': 0.32, 'offset': 0.16, 'seg_timeout': 36.09}
  role0 prep: to door_inside[target,direct] release -> [when teammate_inside] grab box to climb[align,door] lock | play: search
  role1 prep: grab ramp to ramp_inside[yaw3,direct] release | play: segments then grab box to door_block[yaw3,door] lock release -> [when teammate_inside] grab box to teammate[align,direct]
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.209
- hider win-rate: 0.12
- behaviour detection rates: {"chasing": 0.05, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.23}
- mean first-seen play step: 35.4
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.33
- seekers entered quadrant: 0.80, mean max seeker z: 0.20

## Failure analysis (lost instances)
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[1.0, 0.12] | seeker 2 saw hider 1 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@8; prep0/1:dropped@22; prep0/1:done@27; prep1/0:done@24; play1/0:dropped@32; play1/0:timeout@68; play1/1:dropped@69; play1/1:no_object@69
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play1/0:no_target@32; play1/1:dropped@38; play1/1:timeout@69
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.02, 0.11] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@11; prep0/1:done@17; play1/0:dropped@37; play1/0:done@46; play1/1:dropped@47; play1/1:no_object@47
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play1/0:no_target@32; play1/1:dropped@40; play1/1:timeout@69
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 3 saw hider 1 at play step 40 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@9; play1/0:no_target@32; play1/1:dropped@33; play1/1:timeout@69
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.65, 0.19] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@3; play1/0:timeout@68; play1/1:dropped@78
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 1 at play step 43 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@0; play1/0:no_target@32; play1/1:dropped@33; play1/1:timeout@69
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 1 at play step 41 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@13; play1/0:done@56; play1/1:dropped@68