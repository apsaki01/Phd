# Rehearsal feedback — iteration 44 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 6.0, 'damp': 0.47, 'tol': 0.32, 'offset': 0.16, 'seg_timeout': 36.09}
  role0 prep: [when teammate_inside] grab box to climb[align,door] lock | play: go(teammate,door)
  role1 prep: grab ramp to ramp_inside[yaw3,direct] release -> [when doors_sealed] grab box to box[align,direct] lock release | play: segments then grab box to door_block[yaw3,door] lock release -> [when teammate_inside] grab box to teammate[align,direct]
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.232
- hider win-rate: 0.17
- behaviour detection rates: {"chasing": 0.0, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.13}
- mean first-seen play step: 36.7
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.33
- seekers entered quadrant: 0.82, mean max seeker z: 0.22

## Failure analysis (lost instances)
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[1.18, 0.3] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@28; play1/0:done@54; play1/1:dropped@55
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play1/0:done@40; play1/1:dropped@41; play1/1:timeout@77
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.7, 1.37] | seeker 2 saw hider 0 at play step 42 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@25; prep1/0:done@22; play1/0:dropped@32; play1/0:timeout@68; play1/1:dropped@69; play1/1:no_object@69
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play1/0:timeout@68; play1/1:dropped@69
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.17, 0.3] | seeker 2 saw hider 0 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@11; play1/0:timeout@68; play1/1:dropped@69; play1/1:no_object@69
- p_door=0.75 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.0, 0.0] | seeker 2 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play1/0:timeout@68; play1/1:dropped@69
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play1/0:timeout@68
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.58, 1.45] | seeker 2 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play1/0:done@39; play1/1:dropped@40; play1/1:timeout@76