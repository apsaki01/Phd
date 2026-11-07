# Rehearsal feedback — iteration 64 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 6.0, 'damp': 0.47, 'tol': 0.32, 'offset': 0.16, 'seg_timeout': 36.09}
  role0 prep: grab ramp to ramp_inside[yaw3,direct] release | play: segments then grab box to stay[yaw3,door] lock
  role1 prep: grab ramp to ramp_inside[yaw3,direct] release | play: segments then grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.357
- hider win-rate: 0.35
- behaviour detection rates: {"chasing": 0.2, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 36.9
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.25
- seekers entered quadrant: 0.75, mean max seeker z: 0.21

## Failure analysis (lost instances)
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@24; play0/0:timeout@68; prep1/0:no_object@0; play1/0:timeout@68
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 3 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@68; prep1/0:no_object@0; play1/0:timeout@68
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 3 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@68; prep1/0:no_object@0; play1/0:timeout@68
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.0, 0.0] | seeker 2 saw hider 1 at play step 34 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@68; prep1/0:no_object@0; play1/0:dropped@42; play1/0:timeout@68
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@68; prep1/0:no_object@0; play1/0:timeout@68
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@68; prep1/0:no_object@0; play1/0:dropped@50; play1/0:timeout@68
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 34 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@68; prep1/0:no_object@0; play1/0:timeout@68
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 3 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:dropped@36; play0/0:timeout@68; prep1/0:no_object@0; play1/0:timeout@68